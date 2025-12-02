#!/bin/bash

set -e

echo "Installing Python3 and related tools..."

sudo apt-get update
sudo apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    python3-setuptools \
    python3-wheel

# Upgrade pip
python3 -m pip install --upgrade pip

# Install common Python packages
pip3 install --user \
    numpy \
    pandas \
    matplotlib \
    seaborn \
    scikit-learn \
    jupyter \
    jupyterlab \
    ipython \
    requests \
    pytest \
    black \
    flake8 \
    mypy \
    pylint

# Verify installation
python3 --version
pip3 --version

echo "Python3 installed successfully!"
