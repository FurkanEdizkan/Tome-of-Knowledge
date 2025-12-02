#!/bin/bash

set -e

echo "Installing TypeScript and related tools..."

# Install TypeScript globally
sudo npm install -g typescript ts-node

# Install common TypeScript tools
sudo npm install -g \
    @types/node \
    tsx \
    tsup \
    nodemon \
    prettier \
    eslint

# Verify installation
tsc --version
ts-node --version

echo "TypeScript installed successfully!"
