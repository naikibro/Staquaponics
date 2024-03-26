#!/bin/bash

# Function to check if a package is installed
is_installed() {
    dpkg -s "$1" &> /dev/null
}

# Update package lists
sudo apt-get update

# Install packages if not already installed
packages=("apt-get" "curl" "scp" "ffmpeg" "docker" "nodejs" "npm")

for pkg in "${packages[@]}"; do
    if ! is_installed "$pkg"; then
        echo "Installing $pkg..."
        sudo apt-get install -y "$pkg"
    else
        echo "$pkg is already installed."
    fi
done

# Install Node Version Manager (nvm) if not already installed
if [ ! -d "$HOME/.nvm" ]; then
    echo "Installing nvm..."
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
else
    echo "nvm is already installed."
fi

exec bash