
# OSI SAF Ice Edge Filtered Sea Ice Concentration

conc_edgefilter.py takes the sea ice-concentration and -edge OSI SAF products and produces a filtered sea
ice-concentration product, with the ice concentration set to zero where the ice-edge product indicates no
ice or very open ice (i.e. where the flag_values variable is 1).

The latest OSI SAF sea ice concentration and edge products can be downloaded from here:

    ftp://osisaf.met.no/prod/ice/conc
    ftp://osisaf.met.no/prod/ice/edge

## Requirements
    * Tested with Python 2.7.11
    * docopt
    * netCDF4

## Usage
    $ python conc_edgefilter.py <conc_file> <edge_file> <output_file>

    <conc_file>   path to the ice concentration product NetCDF file
    <edge_file>   path to the ice edge product NetCDF file
    <output_file> path of the, new, filtered ice concentration file, that will be generated

