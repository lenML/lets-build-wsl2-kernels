# Let's build wsl2 kernels 🛠️

[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/lenML/lets-build-wsl2-kernels/build-kernel.yml?style=flat-square)](https://github.com/lenML/lets-build-wsl2-kernels/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)

This repository provides automated builds of Microsoft's official WSL2 kernel sources, compiling and releasing only the bzImage kernel files.

## Why This Exists ❓

Microsoft maintains the [WSL2-Linux-Kernel](https://github.com/microsoft/WSL2-Linux-Kernel) but:
- Doesn't provide pre-built historical kernel versions
- Only distributes kernels through Windows Update
- Makes it difficult to test different kernel versions

This project:
- Automates building official Microsoft kernel sources exactly as released
- Provides access to historical kernel versions
- Only distributes the compiled bzImage (kernel binary)
- Does NOT provide or modify any vhdx files

## Features ✨

- Builds any WSL2 kernel version from Microsoft's repository
- Manual trigger with version selection
- Weekly automatic builds of latest stable version
- Provides only the bzImage kernel file
- Clean builds with no modifications

## Usage 🚀

### Manual Build via GitHub UI

1. Go to "Actions" tab
2. Select "Build WSL2 Kernel"
3. Click "Run workflow"
4. Specify kernel version (e.g. `5.15.90.1`)
5. Click "Run workflow"

### Install Compiled Kernel

1. Download the bzImage artifact after build completes
2. Place it in your preferred location (e.g. `C:\Windows\System32\lxss\tools`)
3. Create/modify `%USERPROFILE%\.wslconfig`:

```ini
[wsl2]
kernel=C:\\path\\to\\bzImage
```

4. Restart WSL: `wsl --shutdown`

### Local Build

To build locally from official sources:

```bash
./scripts/build.sh [version]
```

Example:
```bash
./scripts/build.sh 5.15.90.1
```

## Supported Versions 📦

All versions from Microsoft's [WSL2-Linux-Kernel](https://github.com/microsoft/WSL2-Linux-Kernel/tags) can be built.

## License 📄

Kernel code is under Microsoft's original licenses. Build scripts are MIT licensed.