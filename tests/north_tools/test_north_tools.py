def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails for the north tool
    from nomad_north_nionswift.north_tools.nomad_north_nionswift import (
        north_tool_entry_point,
    )

    assert (
        north_tool_entry_point.id_url_safe == 'nomad_north_nionswift'
        or north_tool_entry_point.id == 'nomad-north-nionswift'
    ), 'NORTHtool entry point has incorrect id or id_url_safe'
