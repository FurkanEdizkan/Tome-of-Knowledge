#!/bin/bash

set -e

echo "Installing Node.js and npm..."

# Install Node.js 20.x LTS
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Verify installation
node --version
npm --version

# Install pnpm and yarn
sudo npm install -g pnpm yarn

echo "Node.js installed successfully!"
