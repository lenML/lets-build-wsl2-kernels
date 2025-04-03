# WSL2 Kernel Builder

This repository automates building custom WSL2 kernels using GitHub Actions.

## Features

- Build any WSL2 kernel version from Microsoft's repository
- Manual trigger with custom version and config options
- Weekly automatic builds of the latest stable version
- Artifact with compiled kernel and config

## Usage

### Manual Build via GitHub UI

1. Go to "Actions" tab
2. Select "Build WSL2 Kernel"
3. Click "Run workflow"
4. Specify kernel version (e.g. `5.15.150.1`)
5. (Optional) Add extra config options (e.g. `CONFIG_USB_VIDEO_CLASS=y`)
6. Click "Run workflow"

### Download and Use Built Kernel

1. After build completes, download the artifact
2. Extract the `bzImage` file
3. Place it in your desired location (e.g. `C:\Windows\System32\lxss\tools`)
4. Create or modify `%USERPROFILE%\.wslconfig`:

```ini
[wsl2]
kernel=C:\\path\\to\\bzImage
```

5. Restart WSL: `wsl --shutdown`

### Local Build

To build locally, run:

```bash
./scripts/build.sh [version] [extra_config]
```

Example:
```bash
./scripts/build.sh 5.15.150.1 "CONFIG_USB_VIDEO_CLASS=y"
```

## Supported Versions

Check available versions at [Microsoft's WSL2-Linux-Kernel repository](https://github.com/microsoft/WSL2-Linux-Kernel/tags)
