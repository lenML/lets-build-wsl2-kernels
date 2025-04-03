#!/bin/bash

set -e

KERNEL_VERSION=${1:-"5.15.150.1"}
EXTRA_CONFIG=${2:-""}

# Install dependencies
sudo apt-get update
sudo apt-get install -y build-essential flex bison dwarves libssl-dev libelf-dev libncurses-dev

# Download kernel source
mkdir -p kernel
cd kernel
wget https://github.com/microsoft/WSL2-Linux-Kernel/archive/refs/tags/linux-msft-wsl-${KERNEL_VERSION}.tar.gz
tar -xzf linux-msft-wsl-${KERNEL_VERSION}.tar.gz
mv WSL2-Linux-Kernel-linux-msft-wsl-${KERNEL_VERSION} linux-${KERNEL_VERSION}
cd linux-${KERNEL_VERSION}

# Configure kernel
cp Microsoft/config-wsl .config

if [ -n "${EXTRA_CONFIG}" ]; then
    echo "${EXTRA_CONFIG}" >> .config
fi

make olddefconfig

# Build kernel
make -j$(nproc)

echo "Build completed successfully!"
echo "Kernel image: $(pwd)/arch/x86/boot/bzImage"