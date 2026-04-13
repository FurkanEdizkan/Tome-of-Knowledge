#!/usr/bin/env python3
import argparse
import os
import shutil
import stat
import sys
from pathlib import Path

def prompt_text(prompt, default=None, required=False):
    if default:
        prompt = f"{prompt} [{default}]: "
    else:
        prompt = f"{prompt}: "
    value = input(prompt).strip()
    if not value and default is not None:
        return default
    if required and not value:
        print("This field is required.")
        return prompt_text(prompt, default, required)
    return value


def ensure_executable(path: Path):
    st = path.stat()
    path.chmod(st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def safe_mkdir(path: Path):
    path.mkdir(parents=True, exist_ok=True)
    return path


def copy_file(src: Path, dst_dir: Path) -> Path:
    safe_mkdir(dst_dir)
    dst = dst_dir / src.name
    shutil.copy2(src, dst)
    return dst


def write_desktop_file(path: Path, entry_data: dict):
    lines = ["[Desktop Entry]"]
    for key, value in entry_data.items():
        if value is not None and value != "":
            lines.append(f"{key}={value}")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
    path.chmod(0o644)
    return path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Create a Linux .desktop app entry for AppImages or custom executables.")
    parser.add_argument("--app", help="Path to the downloaded app file or executable.")
    parser.add_argument("--name", help="Display name of the application.")
    parser.add_argument("--description", help="Short description for the application.")
    parser.add_argument("--icon", help="Path to an icon file (png/svg). Optional.")
    parser.add_argument("--install-dir", default="~/.local/share/quick-apps",
                        help="Directory to copy the app into. Default is ~/.local/share/quick-apps.")
    parser.add_argument("--desktop-dir", default="~/.local/share/applications",
                        help="Directory where the .desktop file is created. Default is ~/.local/share/applications.")
    parser.add_argument("--categories", default="Utility",
                        help="Comma-separated desktop categories. Default is Utility.")
    parser.add_argument("--terminal", action="store_true",
                        help="Run the executable in a terminal window. Default is false.")
    parser.add_argument("--exec-args", default="",
                        help="Additional arguments to pass to the executable.")
    parser.add_argument("--no-copy", action="store_true",
                        help="Do not copy the app file into the install directory; use it in place.")
    parser.add_argument("--no-icon-copy", action="store_true",
                        help="Do not copy the icon file, use it from its current path.")
    parser.add_argument("--force", action="store_true",
                        help="Overwrite existing app and desktop entry if they already exist. Useful for updates.")
    return parser.parse_args()


def main():
    args = parse_args()

    app_path = Path(args.app).expanduser() if args.app else None
    if not app_path or not app_path.exists():
        app_path_input = prompt_text("Path to the downloaded app file (AppImage or executable)", required=True)
        app_path = Path(app_path_input).expanduser()
        if not app_path.exists():
            print(f"Error: file does not exist: {app_path}")
            sys.exit(1)

    name = args.name or prompt_text("Application name", required=True)
    description = args.description or prompt_text("Application description", default="", required=False)
    icon_path = Path(args.icon).expanduser() if args.icon else None
    if not icon_path and not args.no_icon_copy:
        icon_input = prompt_text("Path to an icon file (png/svg). Leave empty to skip", default="")
        if icon_input:
            icon_path = Path(icon_input).expanduser()

    install_dir = Path(args.install_dir).expanduser()
    desktop_dir = Path(args.desktop_dir).expanduser()
    categories = args.categories or "Utility"
    terminal = args.terminal
    exec_args = args.exec_args.strip()

    if not args.no_copy:
        safe_mkdir(install_dir)
        installed_app = install_dir / app_path.name
        if installed_app.exists() and not args.force:
            print(f"App already exists at {installed_app}. Use --force to overwrite.")
            sys.exit(1)
        shutil.copy2(app_path, installed_app)
        app_path = installed_app
    if not app_path.is_file():
        print(f"Error: app path is not a file: {app_path}")
        sys.exit(1)

    ensure_executable(app_path)

    icon_dest = None
    if icon_path:
        if not icon_path.exists():
            print(f"Error: icon file does not exist: {icon_path}")
            sys.exit(1)
        if args.no_icon_copy:
            icon_dest = str(icon_path)
        else:
            icon_dir = Path.home() / ".local/share/icons/hicolor/256x256/apps"
            safe_mkdir(icon_dir)
            icon_dest = str(icon_dir / icon_path.name)
            shutil.copy2(icon_path, icon_dest)

    safe_mkdir(desktop_dir)
    desktop_name = f"{name.strip().replace(' ', '-')}.desktop"
    desktop_file = desktop_dir / desktop_name
    if desktop_file.exists() and not args.force:
        print(f"Desktop file already exists at {desktop_file}. Use --force to overwrite.")
        sys.exit(1)

    exec_value = f'"{app_path}"'
    if exec_args:
        exec_value = f'{exec_value} {exec_args}'

    entry_data = {
        "Type": "Application",
        "Name": name,
        "Comment": description,
        "Exec": exec_value,
        "Icon": icon_dest or "",
        "Terminal": "true" if terminal else "false",
        "Categories": categories,
        "StartupNotify": "true",
    }

    write_desktop_file(desktop_file, entry_data)

    print("\nCreated desktop entry:")
    print(f"  {desktop_file}")
    print(f"  Exec: {exec_value}")
    if icon_dest:
        print(f"  Icon: {icon_dest}")
    print("\nIf the application does not appear immediately, run:")
    print("  update-desktop-database ~/.local/share/applications")
    print("or log out and log back in.")


if __name__ == "__main__":
    main()
