import requests
import re
from collections import defaultdict


def get_latest_patches(repo_url):
    api_url = f"https://api.github.com/repos/microsoft/WSL2-Linux-Kernel/releases"
    response = requests.get(api_url)
    response.raise_for_status()
    releases = response.json()

    version_pattern = re.compile(r"linux-msft-wsl-(\d+)\.(\d+)\.(\d+)\.(\d+)")
    latest_patches = defaultdict(lambda: (0, 0))

    for release in releases:
        tag_name = release["tag_name"]
        match = version_pattern.match(tag_name)
        if match:
            major, minor, patch, subpatch = map(int, match.groups())
            current_max = latest_patches[(major, minor, patch)]
            latest_patches[(major, minor, patch)] = max(
                current_max, (subpatch, tag_name)
            )

    latest_patch_versions = [
        latest_patches[key][1] for key in sorted(latest_patches.keys())
    ]
    return latest_patch_versions


if __name__ == "__main__":
    repo_url = "https://github.com/microsoft/WSL2-Linux-Kernel/releases"
    latest_patches = get_latest_patches(repo_url)
    latest_patches.reverse()
    for version in latest_patches:
        print(f"- [ ] {version}")
