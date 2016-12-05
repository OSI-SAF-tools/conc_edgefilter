from conc_edgefilter import *
import os.path


def test_create_product():
    conc_file = 'tests/data/ice_conc_nh_polstere-100_multi_201611021200.nc'
    edge_file = 'tests/data/ice_edge_nh_polstere-100_multi_201611021200.nc'
    output_file = 'tests/data/out/ice_conc_nh_polstere-100_multi_201611021200.nc'

    file_check(conc_file, edge_file)
    water = water_mask(edge_file)
    filter_file(conc_file, output_file, water)

    assert os.path.isfile(output_file)


