#!/usr/bin/env python3
"""Facts about the machine MO2-LINT runs on."""

import os
from pathlib import Path


def is_arm64() -> bool:
    """True on ARM64 Linux, where Steam runs ARM64 builds of Proton."""
    return os.uname().machine.lower() in ("aarch64", "arm64")


def is_steam_frame() -> bool:
    """
    True on SteamOS for the Valve Steam Frame (VARIANT_ID=vr in os-release).
    Steam runs the whole VR session there, so it must not be restarted.
    """
    try:
        text = Path("/etc/os-release").read_text(encoding="utf-8")
    except OSError:
        return False
    for line in text.splitlines():
        key, _, value = line.partition("=")
        if key.strip() == "VARIANT_ID":
            return value.strip().strip("\"'") == "vr"
    return False
