---
title: Requirements
layout: default
nav_order: 1
parent: Getting Started
---

# Requirements

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Operating System

{: .danger }
> **Linux only.** MO2-LINT does not work on Windows, MacOS, or any other operating system.

### ARM64 (e.g. Steam Frame)

ARM64 Linux support currently requires a source build; published ARM64 releases are not available yet. Steam only runs the ARM64 builds of Proton there, so MO2-LINT uses `Proton 11.0 (ARM64)` by default.

{: .note }
> On the Steam Frame, MO2-LINT doesn't restart Steam after installing (Steam runs the whole VR session there). Reboot the headset afterwards so Steam picks up the new compatibility tool.

{: .warning }
> With the USVFS version bundled in Mod Organizer 2.5.2, programs started from MO2 (the game, script extenders, tools) close immediately on ARM64. MO2 itself works. See [ModOrganizer2/usvfs#93](https://github.com/ModOrganizer2/usvfs/pull/93).

## Launchers

You need at least one of:

- Steam - for Steam games
- Heroic Games Launcher - for GOG and Epic Games Store games

{: .unsupported }
> MO2-LINT does not support Lutris or any other game launchers.

## Compatibility Layer

See [Setting up Proton](./proton-setup).

### Supported Versions

| Layer | Notes |
|:--|:--|
| **Proton 11.0** | The only officially tested and supported version. Early versions may work but aren't guaranteed to, and are not supported. |
| **Proton 10.0-4** | There are known issues with Mod Organizer 2 on this version, such as [#878](https://github.com/Furglitch/modorganizer2-linux-installer/issues/878) |
| **Proton 9.0-4** | Known to be incapable of launching games such as Fallout 4. |

## System Packages

| Package | Why it's needed | Distro Inclusion | Required? |
|:--|:--|:--|:--|
| xdg-mime | Sends Nexus Mods downloads to MO2 via the `nxm://` handler. Allows MO2 to use your default applications for folders and various file types. | Included by default on many distros. | Required |
| procps | Provides `pgrep`, used to auto-restart Steam/Heroic while adding launch options. | Included by default on many distros. Fedora known not to. | Required |
| cabextract | Used by *protontricks* to extract files for the `arial` font trick. Without it, MO2 may render with a visual bug. | Most distros don't include this by default. | Recommended |
| protontricks | Manages the Proton prefix and installs MO2 dependencies. | Bundled with MO2-LINT. | Optional |
| winetricks | Used to manage Heroic prefixes and other Wine-related tasks. | Bundled with MO2-LINT, but falls back to the system version if installed. | Optional |

---

Once these are in place, continue to [Installing MO2-LINT](./installing).
