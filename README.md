
# OSI SAF Ice Edge Filtered Sea Ice Concentration

conc_edgefilter.py takes the sea ice-concentration and -edge OSI SAF products and produces a filtered sea
ice-concentration product. The ice concentration set to zero where the ice-edge product indicates no ice or
very open ice (i.e. where the flag_values variable is 1).

This filter removes *most* of the spurious sea ice.

### Limitations
    * In addition to removing spurious ice, the filter also removes a significant amount of valid sea ice.
    * The filter does not remove spurious ice near the coast.

## Requirements
    * Tested with Python 2.7.11
    * docopt
    * netCDF4

## Usage
The latest OSI SAF sea ice concentration and edge products can be downloaded from here:

    ftp://osisaf.met.no/prod/ice/conc
    ftp://osisaf.met.no/prod/ice/edge

Download the sea ice concentration and the corresponding sea ice edge products in NetCDF format.
(Note that the product files are only available for the last 31 days from this location.)
For example download &mdash; replacing 20161103 with the desired date:

    ftp://osisaf.met.no/prod/ice/conc/ice_conc_nh_polstere-100_multi_201611031200.nc
    ftp://osisaf.met.no/prod/ice/edge/ice_edge_nh_polstere-100_multi_201611031200.nc

Use conc_edgefilter.py to create a filtered product file from these, as follows:

    $ python conc_edgefilter.py <conc_file> <edge_file> <output_file>

        <conc_file>   path to the sea ice concentration product NetCDF file
        <edge_file>   path to the sea ice edge product NetCDF file
        <output_file> path of the, new, filtered ice concentration file, that will be generated

