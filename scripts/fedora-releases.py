#!/usr/bin/env python3

"""Print a GitHub Actions matrix for current Fedora RISC-V releases."""

from __future__ import annotations

import json
import re
from urllib.request import Request, urlopen


BODHI_URL = "https://bodhi.fedoraproject.org/releases/"

FEDORA_RELEASE_NAME = re.compile(r"^F[0-9]+$")


def fetch_releases(state: str) -> list[dict[str, object]]:
    """Fetch Bodhi releases by state."""

    url = f"{BODHI_URL}?state={state}&rows_per_page=100"
    request = Request(
        url,
        headers={
            "Accept": "application/json"
        },
    )
    with urlopen(request, timeout=30) as response:
        payload = json.load(response)
    return payload.get("releases", [])


def release_matrix() -> list[str]:
    """Return current Fedora release versions."""

    releases = fetch_releases("current")
    versions = []

    for release in releases:
        if release.get("id_prefix") == "FEDORA":
            versions.append(release["version"])

    if not versions:
        raise RuntimeError("Bodhi returned no Fedora releases")

    return sorted(versions, key=int)


if __name__ == "__main__":
    # Keep this JSON on one line: build.yml writes it directly to GITHUB_OUTPUT,
    # whose NAME=VALUE form cannot represent a multi-line value.
    print(json.dumps(release_matrix(), separators=(",", ":")))
