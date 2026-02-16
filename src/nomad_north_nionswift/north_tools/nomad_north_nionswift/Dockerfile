ARG IMAGE_TAG=main
ARG BASE_IMAGE=ghcr.io/fairmat-nfdi/nomad-north-desktop-base
ARG PLUGIN_NAME=nomad-north-nionswift

FROM ${BASE_IMAGE}:${IMAGE_TAG} AS base

USER root

RUN apt update \
 && apt-get install -y \
        git \
        build-essential \
 && rm -rf /var/lib/apt/lists/*

USER ${NB_UID}

COPY --chown=${NB_UID}:${NB_GID} src/nomad_north_nionswift/north_tools/nomad_north_nionswift/environment.yml "/tmp/environment.yml"
COPY --chown=${NB_UID}:${NB_GID} src/nomad_north_nionswift/north_tools/nomad_north_nionswift/Nion "${HOME}/.local/share/Nion"
COPY --chown=${NB_UID}:${NB_GID} src/nomad_north_nionswift/north_tools/nomad_north_nionswift/Documents "${HOME}/Documents"

# replace the previous three lines with this to eventually make the image slimmer
# COPY --chown=${NB_UID}:${NB_GID} \
#     environment.yml \
#     Nion \
#     Documents \
#     /tmp/docker-copy-temp/
# RUN mv /tmp/docker-copy-temp/environment.yml /tmp/environment.yml && \
#     mv /tmp/docker-copy-temp/Nion ${HOME}/.local/share/Nion && \
#     mv /tmp/docker-copy-temp/Documents ${HOME}/Documents && \
#     rm -rf /tmp/docker-copy-temp

# Create the named environment with packages as mentioned in the environment.yml file, clear mamba cache
ARG env_name=nionswift
RUN mamba env create -f "/tmp/environment.yml" \
    && mamba clean --all -f -y \
    && rm -rf "/tmp/environment.yml"

# Install Python package from Git inside nionswift env
RUN "${CONDA_DIR}/envs/${env_name}/bin/pip" install --no-cache-dir \
    "git+https://git.physik.hu-berlin.de/kornilog/nionswift_frwr_plugin.git@08dc2c8b2a903e5e92e3c55fb4b9248ef5af60ec"

# Register environment as Jupyter kernel
RUN conda run -n ${env_name} python -m ipykernel install --user --name="${env_name}" \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "/home/${NB_USER}"

# Optional: make env default for subsequent RUN commands
SHELL ["conda", "run", "-n", "nionswift", "/bin/bash", "-c"]

# Switch back to jovyan to avoid accidental container runs as root
USER ${NB_UID}
# why the previous line again, shouldnt we have switched way before already
WORKDIR "${HOME}"

# the next line should not work any longer as we moved from openbox to xfce4
# COPY --chown=${NB_UID}:${NB_GID} config/menu.xml ${HOME}/.config/openbox/menu.xml
# is the next line a possible replacement?
RUN mkdir -p "${HOME}/.local/share/applications" && \
    chown -R ${NB_UID}:${NB_GID} "${HOME}/.local/share/applications"
COPY --chown=${NB_UID}:${NB_GID} "src/nomad_north_nionswift/north_tools/nomad_north_nionswift/config/nionswift.desktop" "${HOME}/.local/share/applications/nionswift.desktop"

# the next line should not work any longer as we moved from openbox to xfce4
# COPY --chown=${NB_UID}:${NB_GID} config/autostart ${HOME}/.config/openbox/autostart
# is the next line a possible replacement?
COPY --chown=${NB_UID}:${NB_GID} "src/nomad_north_nionswift/north_tools/nomad_north_nionswift/config/nionswift.desktop" "${HOME}/.config/autostart/nionswift.desktop"
