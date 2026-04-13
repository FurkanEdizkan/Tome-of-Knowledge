# Quick-App Desktop Wrapper

A simple terminal utility to create Linux desktop entries for downloaded AppImages and custom executables.

## Features

- Copies the downloaded app into `~/.local/share/quick-apps`
- Makes the app executable
- Creates a `.desktop` file in `~/.local/share/applications`
- Can use a custom icon file
- Prompts for app name and description when needed

## Usage

Run the script directly:

```bash
./quick-app.py --app /path/to/MyApp.AppImage --name "My App" --description "My custom app" --icon /path/to/icon.png
```

Or use the interactive prompts:

```bash
./quick-app.py
```

## Options

- `--app`: Path to the downloaded app file or executable
- `--name`: Application display name
- `--description`: Application description
- `--icon`: Icon file path (PNG or SVG)
- `--install-dir`: App install directory (default `~/.local/share/quick-apps`)
- `--desktop-dir`: Desktop entry directory (default `~/.local/share/applications`)
- `--categories`: Desktop categories (default `Utility`)
- `--terminal`: Run the app in a terminal
- `--exec-args`: Additional command-line arguments for the app
- `--no-copy`: Use the app in place without copying it
- `--no-icon-copy`: Keep the icon where it is instead of copying it
- `--force`: Overwrite an existing desktop entry

## Example

```bash
./quick-app.py --app ~/Downloads/qbittorrent-5.1.4_x86_64.AppImage \
  --name "qBittorrent" \
  --description "qBittorrent BitTorrent client" \
  --icon ~/Downloads/qbittorrent.png
```

## Updating an installed application

To update an app when you have a newer AppImage or a new executable, rerun the same command with the new file path and the same application name. Add `--force` to overwrite the existing copied app and desktop entry:

```bash
./quick-app.py --app ~/Downloads/qbittorrent-5.1.5_x86_64.AppImage \
  --name "qBittorrent" \
  --description "qBittorrent BitTorrent client" \
  --icon ~/Downloads/qbittorrent.png \
  --force
```

If you use the interactive command `./quick-app`, answer `y` when prompted to overwrite the existing desktop entry and app copy.

## Interactive terminal command

A Bubble Tea-powered interactive prompt is available via Go.

From the wrapper folder run:

```bash
cd "scripts/Quick-App Desktop Wrapper"
./quick-app
```

The command will ask for:
- App path
- Application name
- Description
- Icon path
- Install directory
- Desktop entry directory
- Categories
- Terminal execution
- Extra exec args
- Copy / overwrite options

Go must be installed to run the command. If Go is not available, install it and then run:

```bash
cd "scripts/Quick-App Desktop Wrapper"
go mod tidy
./quick-app
```

## Notes

- The script creates a desktop entry that should appear in Linux application menus.
- If the app does not show immediately, run:

```bash
update-desktop-database ~/.local/share/applications
```
