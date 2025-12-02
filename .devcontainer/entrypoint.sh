#!/bin/bash

echo ""
echo "Starting Tome of Knowledge DevContainer..."
echo ""

# Load .env if it exists
if [ -f /workspace/.env ]; then
    echo "Loading environment variables from .env..."
    export $(grep -v '^#' /workspace/.env | xargs)
    echo "Environment variables loaded"
else
    echo "No .env file found (optional)"
fi

# Display system info
echo ""
echo "  System Information:"
echo "  • User: $(whoami)"
echo "  • Shell: $SHELL"
echo "  • Working Directory: $(pwd)"
echo ""

# Display installed languages
echo "Installed Languages & Tools:"

if command -v python3 &> /dev/null; then
    echo "  ✓ Python $(python3 --version 2>&1 | cut -d' ' -f2)"
fi

if command -v node &> /dev/null; then
    echo "  ✓ Node.js $(node --version)"
fi

if command -v npm &> /dev/null; then
    echo "  ✓ npm $(npm --version)"
fi

if command -v tsc &> /dev/null; then
    echo "  ✓ TypeScript $(tsc --version | cut -d' ' -f2)"
fi

if command -v go &> /dev/null; then
    echo "  ✓ $(go version | cut -d' ' -f3-4)"
fi

if command -v rustc &> /dev/null; then
    echo "  ✓ Rust $(rustc --version | cut -d' ' -f2)"
fi

if command -v cargo &> /dev/null; then
    echo "  ✓ Cargo $(cargo --version | cut -d' ' -f2)"
fi

echo ""
echo "Environment ready!"
echo ""

exit 0
