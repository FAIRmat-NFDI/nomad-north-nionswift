from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

nionswift = NORTHTool(
    short_description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin nomad-north-nionswift.',
    image='ghcr.io/fairmat-nfdi/nomad-north-nionswift:main',
    description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin nomad-north-nionswift.',
    external_mounts=[],
    file_extensions=['ipynb'],
    icon='https://raw.githubusercontent.com/FAIRmat-NFDI/nomad-north-nionswift/main/src/nomad_north_nionswift/north_tools/nionswift/nionswift.png',
    image_pull_policy='Always',
    default_url='/lab',
    maintainer=[{'email': 'markus.kuehbach@physik.hu-berlin.de', 'name': 'Markus Kühbach'}],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='nionswift',
)

north_entry_point = NorthToolEntryPoint(
    id_url_safe='nomad-north-nionswift-nionswift',
    north_tool=nionswift,
)
