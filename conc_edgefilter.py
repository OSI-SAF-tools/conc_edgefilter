#!/usr/bin/env python

"""Ice edge filtered sea ice concentration
Takes the ice-concentration and -edge OSI SAF products and produces a filtered ice-concentration product, where the ice
-concentration is set to zero outside of the ice edge.

Usage:
  conc_edgefilter.py <conc_file> <edge_file> <output_file>

Description:
  <conc_file>   path to the ice concentration product NetCDF file
  <edge_file>   path to the ice edge product NetCDF file
  <output_file> path of the new, filtered, ice concentration file

Options:
  -h --help     Show this screen.
  --version     Show version..

Example:
Using the ice-concentration and -edge OSI SAF product NetCDF files downloaded from:
    ftp://osisaf.met.no/prod/ice/conc
    ftp://osisaf.met.no/prod/ice/edge,
the filtered sea ice concentration is produced with:
  $ python ice_conc_nh_polstere-100_multi_201611021200.nc ice_edge_nh_polstere-100_multi_201611021200.nc ice_conc_nh_polstere-100_multi_201611021200.nc
where ice_conc_filt_nh_polstere-100_multi_201611021200.nc is the ice concentration input file
      ice_conc_nh_polstere-100_multi_201611021200.nc      is the ice edge input file
      ice_edge_nh_polstere-100_multi_201611021200.nc.     is the ice concentration output file

__author__ "John Lavelle"
__email__ "jol@dmi.dk"
"""

from docopt import docopt
import shutil
import netCDF4
import re


def parse_filename(filename):
    try:
        file_parts = re.findall('ice_(conc|edge)_(nh|sh)_(.*)_(\d{12}).nc', filename)[0]
    except (TypeError, IndexError):
        raise TypeError('A filename given in the arguments is not as expected. Are you using the correct input files?')
    return file_parts


def file_check(conc_file, edge_file):
    conc_prod_type, conc_hemisphere, conc_grid, conc_datestr = parse_filename(conc_file)
    edge_prod_type, edge_hemisphere, edge_grid, edge_datestr = parse_filename(edge_file)
    try:
        assert conc_prod_type == 'conc'
    except AssertionError:
        raise AssertionError("The filename given in the first argument should contain 'conc'")
    try:
        assert edge_prod_type == 'edge'
    except AssertionError:
        raise AssertionError("The filename given in the second argument should contain 'edge'")
    try:
        assert conc_hemisphere == edge_hemisphere
    except AssertionError:
        raise AssertionError('The hemispheres of the input files are not the same')
    try:
        assert conc_hemisphere == edge_hemisphere
    except AssertionError:
        raise AssertionError('The grids of the input files are not the same')
    try:
        assert conc_datestr == edge_datestr
    except AssertionError:
        raise AssertionError('The dates of the input files are not the same')


def water_mask(edge_file):
    nc_edge = netCDF4.Dataset(edge_file, 'r')
    ice_edge = nc_edge.variables['ice_edge'][:]
    return ice_edge == 1


def new_nc_file(old_conc_file, new_conc_file):
    new_conc_file_tmp = new_conc_file + '.tmp'
    shutil.copy(old_conc_file, new_conc_file_tmp)
    return netCDF4.Dataset(new_conc_file_tmp, 'a')


def filter_file(old_conc_file, new_conc_file, water):
    with new_nc_file(old_conc_file, new_conc_file) as ds:

        ice_conc = ds.variables['ice_conc'][:]
        ice_conc[water & ~ice_conc.mask] = 0.0
        ds.variables['ice_conc'][:] = ice_conc
        del ice_conc

        status_flag = ds.variables['status_flag'][:]
        status_flag[water] = 10
        ds.variables['status_flag'][:] = status_flag
        del status_flag

        confidence_level = ds.variables['confidence_level'][:]
        confidence_level[water] = 0
        ds.variables['confidence_level'][:] = confidence_level
        del confidence_level

        for variable in ['algorithm_uncertainty', 'smearing_uncertainty', 'total_uncertainty']:
            uncertainty = ds.variables[variable][:]
            uncertainty.mask = (water | uncertainty.mask)
            ds.variables[variable][:] = uncertainty
            del uncertainty

        ds.comment = "The ice edge product has been used to filter this ice concentration product, " \
                     "to eliminate noise is open water regions. " \
                     "The ice concentration has been set to zero were the ice edge " \
                     "product indicates no ice or very open ice (i.e. where the flag_value is 1)" \

        shutil.move(ds.filepath(), ds.filepath().replace('.tmp', ''))

if __name__ == '__main__':
    args = docopt(__doc__, version='Ice edge filtered ice concentration v 1.0')
    file_check(args['<conc_file>'], args['<edge_file>'])
    water = water_mask(args['<edge_file>'])
    filter_file(args['<conc_file>'], args['<output_file>'], water)