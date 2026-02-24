ARG IMAGE_TAG=main
ARG BASE_IMAGE=ghcr.io/fairmat-nfdi/nomad-north-desktop-base
ARG UV_VERSION=0.9
ARG PLUGIN_NAME=nomad-north-nionswift

FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv_stage

FROM ${BASE_IMAGE}:${IMAGE_TAG} AS base

# Fix: https://github.com/hadolint/hadolint/wiki/DL4006
# Fix: https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

COPY --from=uv_stage /uv /uvx /bin/

USER root

# with pre-existing NB_USER="jovyan" and NB_UID=100, NB_GID=1000
ENV HOME=/home/${NB_USER}
ENV CONDA_DIR=/opt/conda

RUN apt update \
    && apt-get install  --no-install-recommends -y \
        git \
        build-essential \
        libgl1 \
        libxkbcommon-x11-0 \
        libxcb-cursor0 \
        libxcb-icccm4 \
        libxcb-image0 \
        libxcb-keysyms1 \
 && rm -rf /var/lib/apt/lists/*

ENV UV_PROJECT_ENVIRONMENT=${CONDA_DIR} \
    UV_LINK_MODE=copy \
    UV_NO_CACHE=1 \
    # use python from conda which is default for base-notebook
    # so that uv pip and pip refer to the same python
    # If needed one can create another venv with 'uv venv'
    UV_SYSTEM_PYTHON=1

COPY --chown=${NB_UID}:${NB_GID} src/nomad_north_nionswift/north_tools/nionswift/Nion "${HOME}/.local/share/Nion"
COPY --chown=${NB_UID}:${NB_GID} src/nomad_north_nionswift/north_tools/nionswift/Documents "${HOME}/Documents"

# Create the named environment with packages as mentioned in the environment.yml file, clear mamba cache
ARG CONDA_ENV_NAME=nionswift

RUN mamba create -y -n ${CONDA_ENV_NAME} python=3.13 ipykernel pyqt=5 \
    && mamba clean -afy

ENV UV_PROJECT_ENVIRONMENT=${CONDA_DIR}/envs/{CONDA_ENV_NAME}
RUN uv pip install --upgrade pip nionswift nionswift-tool

# Install Python package from Git inside nionswift env
# RUN "${CONDA_DIR}/envs/${env_name}/bin/pip" install --no-cache-dir \
#     "git+https://git.physik.hu-berlin.de/kornilog/nionswift_frwr_plugin.git@08dc2c8b2a903e5e92e3c55fb4b9248ef5af60ec"

# Register environment as Jupyter kernel
RUN ${CONDA_DIR}/envs/${CONDA_ENV_NAME}/bin/python -m ipykernel install --name "${CONDA_ENV_NAME}" \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "${HOME}"

# Switch back to jovyan to avoid accidental container runs as root
USER ${NB_UID}

# Optional: make env default for subsequent RUN commands
SHELL ["conda", "run", "-n", "nionswift", "/bin/bash", "-c"]

WORKDIR "${HOME}"

RUN mkdir -p "${HOME}/.local/share/applications" \
    && chown -R ${NB_UID}:${NB_GID} "${HOME}/.local/share/applications"

COPY --chown=${NB_UID}:${NB_GID} "src/nomad_north_nionswift/north_tools/nionswift/config/nionswift.desktop" "${HOME}/.local/share/applications/nionswift.desktop"
COPY --chown=${NB_UID}:${NB_GID} "src/nomad_north_nionswift/north_tools/nionswift/config/nionswift.desktop" "${HOME}/.config/autostart/nionswift.desktop"
