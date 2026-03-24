ARG IMAGE_TAG=main
ARG BASE_IMAGE=ghcr.io/fairmat-nfdi/nomad-north-desktop-base
ARG UV_VERSION=0.9
ARG PLUGIN_NAME=nomad-north-nionswift

# FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv_stage

FROM ${BASE_IMAGE}:${IMAGE_TAG} AS base

# Fix: https://github.com/hadolint/hadolint/wiki/DL4006
# Fix: https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# COPY --from=uv_stage /uv /uvx /bin/

ENV NS_VERSION=16.16.1-x86_64

USER root

# with pre-existing NB_USER="jovyan" and NB_UID=100, NB_GID=1000
ENV HOME=/home/${NB_USER}
# ENV CONDA_DIR=/opt/conda
# ENV CONDA_ENV_NAME=nionswift

RUN apt update \
    && apt-get install  --no-install-recommends -y \
        # git \
        # build-essential \
        xfce4 \
        xfce4-goodies \
        wget \
        libgl1 \
        libxkbcommon-x11-0 \
        libxcb-cursor0 \
        libxcb-icccm4 \
        libxcb-image0 \
        libxcb-keysyms1 \
 && rm -rf /var/lib/apt/lists/*

# COPY --chown=${NB_UID}:${NB_GID} src/nomad_north_nionswift/north_tools/nionswift/Nion "${HOME}/.local/share/Nion"
# COPY --chown=${NB_UID}:${NB_GID} src/nomad_north_nionswift/north_tools/nionswift/Documents "${HOME}/Documents"

RUN mkdir -p "${HOME}/Desktop" \
    && chown ${NB_UID}:${NB_GID} "${HOME}/Desktop" \
    && wget -O "${HOME}/Desktop/NionSwift-${NS_VERSION}.AppImage" "https://nion.com/swift/files/NionSwift-${NS_VERSION}.AppImage" \
    && chown -R ${NB_UID}:${NB_GID} "${HOME}/Desktop/NionSwift-${NS_VERSION}.AppImage" \
    && chmod +x "${HOME}/Desktop/NionSwift-${NS_VERSION}.AppImage" \
    && cd ${HOME}/Desktop \
    && ./NionSwift-${NS_VERSION}.AppImage --appimage-extract \
    && chown -R ${NB_UID}:${NB_GID} "${HOME}/Desktop/squashfs-root" \
    && ln -s "${HOME}/Desktop/squashfs-root/AppRun" "${HOME}/Desktop/NionSwift" \
    && rm "${HOME}/Desktop/NionSwift-${NS_VERSION}.AppImage"

# ENV UV_PROJECT_ENVIRONMENT="${CONDA_DIR}/envs/${CONDA_ENV_NAME}" \
#     UV_LINK_MODE=copy \
#     UV_NO_CACHE=1 \
#     UV_SYSTEM_PYTHON=1

# # Create the named environment with packages as mentioned in the environment.yml file, clear mamba cache
# RUN mamba create -y -n "${CONDA_ENV_NAME}" python=3.13 ipykernel pyqt=5 pyside6 \
#     && mamba clean -afy

# RUN UV_PROJECT_ENVIRONMENT=${CONDA_DIR}/envs/{CONDA_ENV_NAME} \
#     uv pip install --upgrade pip nionswift nionswift-tool

# Register environment as Jupyter kernel
# RUN ${CONDA_DIR}/envs/${CONDA_ENV_NAME}/bin/python -m ipykernel install --name "${CONDA_ENV_NAME}" \
#     && fix-permissions "${CONDA_DIR}" \
#     && fix-permissions "${HOME}"

# Switch back to jovyan to avoid accidental container runs as root
USER ${NB_UID}

# Optional: make env default for subsequent RUN commands
# SHELL ["conda", "run", "-n", "nionswift", "/bin/bash", "-c"]

WORKDIR "${HOME}"

RUN mkdir -p "${HOME}/.local/share/applications" \
    && chown -R ${NB_UID}:${NB_GID} "${HOME}/.local/share/applications"

COPY --chown=${NB_UID}:${NB_GID} "src/nomad_north_nionswift/north_tools/nionswift/config/nionswift.desktop" "${HOME}/.local/share/applications/nionswift.desktop"
COPY --chown=${NB_UID}:${NB_GID} "src/nomad_north_nionswift/north_tools/nionswift/config/nionswift.desktop" "${HOME}/.config/autostart/nionswift.desktop"
