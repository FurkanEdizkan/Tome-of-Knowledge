package main

import (
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strings"

	"github.com/charmbracelet/bubbles/textinput"
	tea "github.com/charmbracelet/bubbletea"
)

type field struct {
	key          string
	label        string
	defaultValue string
	required     bool
	validator    func(string) error
}

type model struct {
	fields    []field
	step      int
	values    map[string]string
	input     textinput.Model
	err       string
	finished  bool
	result    string
}

func initialModel() model {
	input := textinput.New()
	input.Placeholder = ""
	input.Focus()
	input.CharLimit = 512
	input.Width = 60

	fields := []field{
		{
			key:          "app_path",
			label:        "Path to AppImage or executable",
			required:     true,
			validator:    validateExistingFile,
		},
		{
			key:          "name",
			label:        "Application display name",
			required:     true,
			validator:    validateNonEmpty,
		},
		{
			key:          "description",
			label:        "Application description (optional)",
			defaultValue: "",
			validator:    validateOptional,
		},
		{
			key:          "icon_path",
			label:        "Path to icon file (optional)",
			defaultValue: "",
			validator:    validateOptionalExistingFile,
		},
		{
			key:          "install_dir",
			label:        "Install directory",
			defaultValue: "~/.local/share/quick-apps",
			validator:    validateNonEmpty,
		},
		{
			key:          "desktop_dir",
			label:        "Desktop directory",
			defaultValue: "~/.local/share/applications",
			validator:    validateNonEmpty,
		},
		{
			key:          "categories",
			label:        "Desktop categories",
			defaultValue: "Utility",
			validator:    validateNonEmpty,
		},
		{
			key:          "terminal",
			label:        "Run in terminal? (y/N)",
			defaultValue: "n",
			validator:    validateYesNo,
		},
		{
			key:          "exec_args",
			label:        "Extra exec args (optional)",
			defaultValue: "",
			validator:    validateOptional,
		},
		{
			key:          "no_copy",
			label:        "Use app in place instead of copying? (y/N)",
			defaultValue: "n",
			validator:    validateYesNo,
		},
		{
			key:          "no_icon_copy",
			label:        "Keep icon where it is instead of copying? (y/N)",
			defaultValue: "n",
			validator:    validateYesNo,
		},
		{
			key:          "force",
			label:        "Overwrite existing desktop entry? (y/N)",
			defaultValue: "n",
			validator:    validateYesNo,
		},
	}

	return model{
		fields: fields,
		values: map[string]string{},
		input:  input,
	}
}

func (m model) Init() tea.Cmd {
	return textinput.Blink
}

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {
	case tea.KeyMsg:
		switch msg.String() {
		case "ctrl+c", "esc":
			return m, tea.Quit
		case "enter":
			value := strings.TrimSpace(m.input.Value())
			current := m.fields[m.step]
			if value == "" && current.defaultValue != "" {
				value = current.defaultValue
			}
			if current.required && value == "" {
				m.err = "This field is required."
				return m, nil
			}
			if err := current.validator(value); err != nil {
				m.err = err.Error()
				return m, nil
			}
			m.err = ""
			m.values[current.key] = value
			m.step++
			if m.step >= len(m.fields) {
				err := runInteractiveSetup(m.values)
				if err != nil {
					m.finished = true
					m.result = fmt.Sprintf("Error: %v", err)
					return m, tea.Quit
				}
				m.finished = true
				m.result = "Desktop entry created successfully."
				return m, tea.Quit
			}
			m.input.SetValue("")
			m.input.Placeholder = m.fields[m.step].defaultValue
			m.input.Focus()
			return m, nil
		}
	}

	var cmd tea.Cmd
	m.input, cmd = m.input.Update(msg)
	return m, cmd
}

func (m model) View() string {
	if m.finished {
		return fmt.Sprintf("%s\n\n", m.result)
	}
	current := m.fields[m.step]
	heading := fmt.Sprintf("%s\n\n", current.label)
	if current.defaultValue != "" {
		heading += fmt.Sprintf("(default: %s)\n\n", current.defaultValue)
	}
	if m.err != "" {
		heading += fmt.Sprintf("Error: %s\n\n", m.err)
	}
	return fmt.Sprintf("%s%s\n\n%s", heading, m.input.View(), "Press Enter to continue or Esc to quit.")
}

func validateNonEmpty(value string) error {
	if strings.TrimSpace(value) == "" {
		return fmt.Errorf("please enter a value")
	}
	return nil
}

func validateOptional(value string) error {
	return nil
}

func validateExistingFile(value string) error {
	if strings.TrimSpace(value) == "" {
		return fmt.Errorf("please enter a path")
	}
	expanded := expandPath(value)
	info, err := os.Stat(expanded)
	if err != nil {
		return fmt.Errorf("path does not exist")
	}
	if info.IsDir() {
		return fmt.Errorf("path must be a file, not a directory")
	}
	return nil
}

func validateOptionalExistingFile(value string) error {
	if strings.TrimSpace(value) == "" {
		return nil
	}
	return validateExistingFile(value)
}

func validateYesNo(value string) error {
	if strings.TrimSpace(value) == "" {
		return nil
	}
	value = strings.ToLower(strings.TrimSpace(value))
	if value == "y" || value == "yes" || value == "n" || value == "no" {
		return nil
	}
	return fmt.Errorf("enter y, yes, n, or no")
}

func expandPath(path string) string {
	if strings.HasPrefix(path, "~/") {
		home, err := os.UserHomeDir()
		if err != nil {
			return path
		}
		return filepath.Join(home, path[2:])
	}
	return os.ExpandEnv(path)
}

func boolFrom(value string) bool {
	value = strings.ToLower(strings.TrimSpace(value))
	return value == "y" || value == "yes"
}

func runInteractiveSetup(values map[string]string) error {
	appPath := expandPath(values["app_path"])
	name := values["name"]
	description := values["description"]
	iconPath := strings.TrimSpace(values["icon_path"])
	installDir := expandPath(values["install_dir"])
	desktopDir := expandPath(values["desktop_dir"])
	categories := values["categories"]
	terminal := boolFrom(values["terminal"])
	execArgs := strings.TrimSpace(values["exec_args"])
	noCopy := boolFrom(values["no_copy"])
	noIconCopy := boolFrom(values["no_icon_copy"])
	force := boolFrom(values["force"])

	if err := ensurePathExists(installDir); err != nil {
		return err
	}
	if err := ensurePathExists(desktopDir); err != nil {
		return err
	}

	appPathInfo, err := os.Stat(appPath)
	if err != nil {
		return err
	}
	if appPathInfo.IsDir() {
		return fmt.Errorf("app path must be a file")
	}

	if !noCopy {
		copied := filepath.Join(installDir, filepath.Base(appPath))
		if _, err := os.Stat(copied); err == nil && !force {
			return fmt.Errorf("file already exists in install directory: %s", copied)
		}
		if err := copyFile(appPath, copied); err != nil {
			return err
		}
		appPath = copied
	}

	if err := ensureExecutable(appPath); err != nil {
		return err
	}

	iconDest := ""
	if iconPath != "" {
		iconPath = expandPath(iconPath)
		if _, err := os.Stat(iconPath); err != nil {
			return err
		}
		if noIconCopy {
			iconDest = iconPath
		} else {
			iconDir := filepath.Join(os.Getenv("HOME"), ".local/share/icons/hicolor/256x256/apps")
			if err := ensurePathExists(iconDir); err != nil {
				return err
			}
			copiedIcon := filepath.Join(iconDir, filepath.Base(iconPath))
			if err := copyFile(iconPath, copiedIcon); err != nil {
				return err
			}
			iconDest = copiedIcon
		}
	}

	desktopFileName := strings.ReplaceAll(strings.TrimSpace(name), " ", "-") + ".desktop"
	desktopPath := filepath.Join(desktopDir, desktopFileName)
	if _, err := os.Stat(desktopPath); err == nil && !force {
		return fmt.Errorf("desktop file already exists: %s", desktopPath)
	}

	execCmd := fmt.Sprintf("\"%s\"", appPath)
	if execArgs != "" {
		execCmd = fmt.Sprintf("%s %s", execCmd, execArgs)
	}

	entry := map[string]string{
		"Type":        "Application",
		"Name":        name,
		"Comment":     description,
		"Exec":        execCmd,
		"Icon":        iconDest,
		"Terminal":    fmt.Sprintf("%t", terminal),
		"Categories":  categories,
		"StartupNotify": "true",
	}

	return writeDesktopFile(desktopPath, entry)
}

func ensurePathExists(path string) error {
	if err := os.MkdirAll(path, 0o755); err != nil {
		return err
	}
	return nil
}

func copyFile(src, dst string) error {
	input, err := os.Open(src)
	if err != nil {
		return err
	}
	defer input.Close()

	output, err := os.Create(dst)
	if err != nil {
		return err
	}
	defer output.Close()

	if _, err := io.Copy(output, input); err != nil {
		return err
	}
	return nil
}

func ensureExecutable(path string) error {
	info, err := os.Stat(path)
	if err != nil {
		return err
	}
	return os.Chmod(path, info.Mode()|0111)
}

func writeDesktopFile(path string, entry map[string]string) error {
	lines := []string{"[Desktop Entry]"}
	for key, value := range entry {
		if strings.TrimSpace(value) != "" {
			lines = append(lines, fmt.Sprintf("%s=%s", key, value))
		}
	}
	lines = append(lines, "")
	return os.WriteFile(path, []byte(strings.Join(lines, "\n")), 0o644)
}

func main() {
	p := tea.NewProgram(initialModel())
	if err := p.Start(); err != nil {
		fmt.Println("Failed to start prompt:", err)
		os.Exit(1)
	}
}
