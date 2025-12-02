#!/bin/bash

set -e

echo "Installing common development tools..."

sudo apt-get update
sudo apt-get install -y \
    vim \
    neovim \
    tmux \
    htop \
    btop \
    tree \
    jq \
    ripgrep \
    fd-find \
    bat \
    exa \
    fzf \
    unzip \
    zip \
    tar \
    gzip \
    postgresql-client \
    redis-tools \
    sqlite3 \
    net-tools \
    dnsutils \
    iputils-ping \
    telnet \
    netcat

# Install modern CLI tools
# bat (better cat)
sudo ln -s /usr/bin/batcat /usr/local/bin/bat 2>/dev/null || true

# fd (better find)
sudo ln -s /usr/bin/fdfind /usr/local/bin/fd 2>/dev/null || true

echo "Common tools installed successfully!"
