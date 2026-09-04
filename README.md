# Fedora RISC-V image-builder buildroots

This repository builds `riscv64` Fedora buildroot images needed for image-builder cross-arch builds for every current Fedora release. Images are published to GHCR as:

```text
ghcr.io/ondrejbudai/fedora-ib-buildroot
```

The build runs daily and can also be started with **Actions → Build Fedora RISC-V buildroots → Run workflow**.

## What is in the image?

It's just a base image (`docker.io/fedorariscv/base:<version>`) with some extra packages needed for image building (FS utils, selinux, python) and an empty `/ostree` directory to make some osbuild stages happy.

## Local build

Firstly, make sure you have `qemu-user-static` installed:

```bash
sudo dnf install -y qemu-user-static
```

Then, build the image:

```bash
podman build --arch riscv64 \
  --build-arg FEDORA_BASE_TAG=44 \
  --tag localhost/fedora-ib-buildroot:44 \
  .
```

The release discovery used by CI can be checked locally with:

```bash
python3 scripts/fedora-releases.py | python3 -m json.tool
```
