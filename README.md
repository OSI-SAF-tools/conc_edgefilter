
# Edge-Filtered Sea Ice Concentration

Spurious ice can occur in the OSI SAF sea ice concentration fields, due to weather effects and the relatively high uncertainty
of the measurement over open water.

conc_edgefilter.py takes the sea ice-concentration and -edge OSI SAF products and produces a filtered sea
ice-concentration product. The ice concentration is set to zero where the sea ice edge product indicates no ice or
very open ice (i.e. where the flag_values variable is 1).

### Limitations
The filter removes *most* of the spurious sea ice; however, it has the following limitations:

    * In addition to removing spurious ice, the filter may remove valid sea ice.
    * The filter does not remove spurious ice near the coast.

[This notebook](docs/Masking_SIC_with_SIEdge.ipynb) shows an analysis of the ice that is removed by the filter.


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

