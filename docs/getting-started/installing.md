---
title: Installing MO2-LINT
layout: default
nav_order: 2
parent: Getting Started
---

# Installing MO2-LINT

Make sure you've covered the [Requirements](./requirements) page first.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 1. Download the binary

Grab the latest v7 release from the [GitHub Releases page](https://github.com/Furglitch/modorganizer2-linux-installer/releases). Download `mo2-lint` for x86_64 Linux (including Steam Deck), or `mo2-lint-aarch64` for ARM64 Linux (including Steam Frame). Both files have no extension.

{: .warning }
> Only versions 7.0.0 and above are supported. If you have an existing v6 instance, see [Uninstalling Legacy (v6) Instances](../uninstalling-legacy) first.

## 2. Make sure it's executable

```bash
chmod +x path/to/downloaded/mo2-lint
```

On ARM64:

```bash
chmod +x path/to/downloaded/mo2-lint-aarch64
```

## 3. Run it

```bash
path/to/downloaded/mo2-lint <command> [options]
```

On ARM64:

```bash
path/to/downloaded/mo2-lint-aarch64 <command> [options]
```

## 4. (Optional, recommended) Install to PATH

For convenience, you can move the binary to a directory on your `PATH` so you can run it from anywhere, instead of having to navigate to the download location or type the full path every time.

Check what's on your `PATH`:

```bash
echo "$PATH" | tr ':' '\n'
```

For example, if `/usr/local/bin` is on your `PATH`, you can move the binary there:

```bash
sudo mv path/to/downloaded/mo2-lint /usr/local/bin/mo2-lint
```

On ARM64, use the ARM64 file as the source and keep the installed command name `mo2-lint`:

```bash
sudo mv path/to/downloaded/mo2-lint-aarch64 /usr/local/bin/mo2-lint
```

Once moved, you can run MO2-LINT from anywhere:

```bash
mo2-lint <command> [options]
```

---

Continue to [Setting up Proton](./proton-setup). This is required before your first `install`.
