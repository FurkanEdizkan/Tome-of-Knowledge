#!/bin/bash

set -e

echo "Installing Rust..."

# Install Rust using rustup
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Source cargo env
source "$HOME/.cargo/env"

# Install common Rust tools
rustup component add rustfmt clippy rust-analyzer

# Verify installation
rustc --version
cargo --version

echo "Rust installed successfully!"
