#!/bin/bash
# .devcontainer/dependencies/install_zsh.sh

set -e

echo "Installing zsh..."

apt-get update
apt-get install -y zsh

# Verify installation
zsh --version

echo "zsh installed successfully!"
