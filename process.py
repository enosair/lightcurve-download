""" Extract data from light curve fits files and dump to json

A dictionary will be saved to the output json file, where the name of
lightcurves (key) will be mapped to a dictionary with the following fields:

  - TIME:        Barycenter corrected Julian date
  - SAP_FLUX:    raw flux
  - PDCSAP_FLUX: flux processed by PDC, systematic error corrected
  - other meta data
    See the full list at [A.1a: Light Curve File Primary Header] of
    http://archive.stsci.edu/kepler/manuals/archive_manual.pdf

---------------------------------------------------------------------------
usage:

 $ python process.py <source folder> <output file>

---------------------------------------------------------------------------
"""

import glob
import os
import sys
import json
import pyfits

def main():
    """ process fits file """

    if len(sys.argv) == 3:
        src = os.path.abspath(sys.argv[1])   # source folder
        out = os.path.abspath(sys.argv[2])   # output file name
    else:
        sys.exit('Usage: python process.py <source folder> <output filename>')

    cwd = os.getcwd()

    os.chdir(src)
    fits_files = glob.glob('*.fits')
    count = len(fits_files)
    print 'Total:{0} FITS files\n'.format(count)

    lc = {}
    i = 0
    for fn in fits_files:
        i = i + 1
        d = {}
        if i % 100 == 0:
            print 'file No.{0} / {1}'.format(i, count)
        try:
            fits = pyfits.open(fn)
            data = fits[1].data
            header = fits[0].header

            # Barycenter corrected Julian date
            d['TIME'] = data.field('TIME').tolist()
            # raw flux
            d['SAP_FLUX'] = data.field('SAP_FLUX').tolist()
            # flux processed by PDC, systematic error corrected
            d['PDCSAP_FLUX'] = data.field('PDCSAP_FLUX').tolist()

            for key, val in header.iteritems():
                if isinstance(val, pyfits.card.Undefined):
                    d[key] = 'undefine'
                else:
                    d[key] = val
            fits.close()

            lc[fn[:-5]] = d      # get rid of '.fits'
        except IOError as err:
            print 'At file {0}:'.format(fn)
            print 'I/O error({0}): {1}'.format(err.errno, err.strerror)

    os.chdir(cwd)

    with open(out, 'wb') as f:
        json.dump(lc, f)

if __name__ == '__main__':
    main()
