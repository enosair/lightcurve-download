# Extract data from light curve fits files and dump to json 
#
# A dictionary will be saved to the output json file, where the name of
# lightcurves (key) will be mapped to a dictionary with the following fields:
#
#   - TIME:        Barycenter corrected Julian date
#   - SAP_FLUX:    raw flux
#   - PDCSAP_FLUX: flux processed by PDC, systematic error corrected
#   - other meta data 
#     See the full list at [A.1a: Light Curve File Primary Header] of
#     http://archive.stsci.edu/kepler/manuals/archive_manual.pdf
#
# ---------------------------------------------------------------------------
# usage:
#  $ python process.py <source folder> <output file>
#
# ---------------------------------------------------------------------------
# Change log
#
# 04/02/2013 - change file name of csv files - get rid of '.fits'
# 04/12/2013 - added I/O Error handling
# 10/13/2014 - read user input, change to csv
# 10/30/2014 - added meta data, save to json


import glob
import pyfits
import os
import sys
import json

def showFITS(fitsobj):
    fitsobj.info()
    lc = fitsobj[1]
    print 'The lightcurve data contains fields:'
    lc.header


def main():

    if len(sys.argv) == 3:
        src = os.path.abspath(sys.argv[1])   # source folder
        out = os.path.abspath(sys.argv[2])   # output file name
    else:                 
        sys.exit('Usage: python process.py <source folder> <output filename>')

    cwd = os.getcwd()

    os.chdir(src)
    fname = glob.glob('*.fits')
    count = len(fname)
    print('Total:{0} FITS files\n'.format(count))


    lc= {}
    i = 0
    for fn in fname:
        i = i + 1
        d = {}
        if ( i % 100 == 0 ):  
                print('file No.{0} / {1}'.format(i,count))
        try:
            FITSfile = pyfits.open(fn)
            data = FITSfile[1].data
            header = FITSfile[0].header

            d['TIME'] = data.field('TIME').tolist()                 # Barycenter corrected Julian date
            d['SAP_FLUX'] = data.field('SAP_FLUX').tolist()         # raw flux
            d['PDCSAP_FLUX'] = data.field('PDCSAP_FLUX').tolist()   # flux processed by PDC, systematic error corrected

            for k, v in header.iteritems():
                if isinstance(v, pyfits.card.Undefined):
                    d[k] = 'undefine'
                else:
                    d[k] = v
            FITSfile.close()

            lc[fn[:-5]] = d      # get rid of '.fits' 
        except IOError as e:
            print 'At file {0}:'.format(fname)
            print 'I/O error({0}): {1}'.format(e.errno, e.strerror)

    os.chdir(cwd)

    f=open(out,'wb')
    json.dump(lc, f)
    f.close()

if __name__ == '__main__':
    main()
