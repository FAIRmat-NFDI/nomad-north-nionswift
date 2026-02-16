#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

nionswift = NORTHTool(
    image='ghcr.io/FAIRmat-NFDI/nomad-north-nionswift:latest',
    description="""### **nionswift**: Software package for electron microscopy

    data analysis and visualization. [Homepage](https://nionswift.readthedocs.io/en/stable/).""",
    short_description='Jupyterlab with nionswift installed',
    external_mounts=[],
    file_extensions=['tiff, tif, dm3, dm4, hdf5, h5, nsproj'],
    icon='nionswift.png',
    image_pull_policy='Always',
    default_url='/lab',
    maintainer=[{'email': 'markus.kuehbach@physik.hu-berlin.de', 'name': 'Markus Kühbach'}],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='nionswift',
)

north_tool_entry_point = NorthToolEntryPoint(
    id_url_safe='nomad_north_nionswift', north_tool=nionswift
)
