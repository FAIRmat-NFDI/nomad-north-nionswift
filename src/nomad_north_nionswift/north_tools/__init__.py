from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

nionswift = NORTHTool(
    short_description='Use Bruker nionswift to visualize and analyze electron microscopy data in NOMAD.',
    image='ghcr.io/fairmat-nfdi/nomad-north-nionswift:main',
    description="""### **nionswift**:

    [Software for electron microscopy data analysis and visualization](https://nionswift.readthedocs.io/en/stable/)

    [Conference proceedings about the software](https://doi.org/10.1017/S1431927614007272)""",
    external_mounts=[],
    file_extensions=['tiff, tif, dm3, dm4, hdf5, h5, nsproj'],
    icon='https://raw.githubusercontent.com/FAIRmat-NFDI/nomad-north-nionswift/main/src/nomad_north_nionswift/north_tools/nionswift/nionswift.png',
    image_pull_policy='Always',
    default_url='/desktop',
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
