#!/bin/bash

set -e

echo "Installing Go..."

GO_VERSION="1.21.5"

# Download and install Go
wget https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go${GO_VERSION}.linux-amd64.tar.gz
rm go${GO_VERSION}.linux-amd64.tar.gz

# Add to PATH (will be added to .zshrc)
export PATH=$PATH:/usr/local/go/bin
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin

# Verify installation
/usr/local/go/bin/go version

echo "Go installed successfully!"
