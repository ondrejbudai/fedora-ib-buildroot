ARG FEDORA_BASE_TAG

FROM docker.io/fedorariscv/base:${FEDORA_BASE_TAG}

RUN dnf install -y \
        python3 \
        selinux-policy-targeted \
        policycoreutils \
        dosfstools \
        e2fsprogs \
        xfsprogs \
        btrfs-progs \
    && dnf clean all

RUN mkdir -p /ostree
