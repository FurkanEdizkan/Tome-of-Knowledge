#!/bin/bash

set -e

echo "Setting up user environment..."

# Install Oh My Zsh
if [ -f /tmp/dependencies/install_ohmyzsh.sh ]; then
    echo "Installing Oh My Zsh..."
    /tmp/dependencies/install_ohmyzsh.sh
fi

# Install common tools
if [ -f /tmp/dependencies/install_common_tools.sh ]; then
    echo "Installing common tools..."
    /tmp/dependencies/install_common_tools.sh
fi

# Install Python3
if [ -f /tmp/dependencies/install_python3.sh ]; then
    echo "Installing Python3..."
    /tmp/dependencies/install_python3.sh
fi

# Install Node.js and TypeScript
if [ -f /tmp/dependencies/install_node.sh ]; then
    echo "Installing Node.js..."
    /tmp/dependencies/install_node.sh
fi

if [ -f /tmp/dependencies/install_typescript.sh ]; then
    echo "Installing TypeScript..."
    /tmp/dependencies/install_typescript.sh
fi

# Install Go (optional - comment out if not needed)
if [ -f /tmp/dependencies/install_go.sh ]; then
    echo "Installing Go..."
    /tmp/dependencies/install_go.sh
fi

# Install Rust (optional - comment out if not needed)
if [ -f /tmp/dependencies/install_rust.sh ]; then
    echo "Installing Rust..."
    /tmp/dependencies/install_rust.sh
fi

# Copy zshrc configuration
if [ -f /tmp/config/.zshrc ]; then
    echo "Configuring zsh..."
    cp /tmp/config/.zshrc $HOME/.zshrc
fi

echo "User setup complete!"
