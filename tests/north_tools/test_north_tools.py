def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails
    from nomad_north_nionswift.north_tools import nionswift

    assert (
        nionswift.id_url_safe == 'nionswift' or nionswift.id == 'nomad-north-nionswift'
    ), 'NORTHTool entry point has incorrect id or id_url_safe'
