import json
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

def main():
    """ example to load and plot data from json """

    if len(sys.argv) == 2:
        jf = os.path.abspath(sys.argv[1])  # source json file
    else:
        sys.exit('Usage: python example.py <source json file>')

    # load data
    lc = json.load(open(jf, 'r'))

    # plot flux for the first two lightcurves
    i = 0
    for k, v in lc.iteritems():
        i += 1
        if i > 2:
            break
        else:
            time = np.array(v['TIME'])
            raw = np.array(v['SAP_FLUX'])              # raw flux
            pdc = np.array(v['PDCSAP_FLUX'])           # PDC pipeline processed flux
            radius = v['RADIUS']                          # stella radius

            plt.subplot(2, 2, 1)
            plt.plot(time[~np.isnan(raw)], raw[~np.isnan(raw)], 'k.') # remove nan
            plt.title("{0}  Radius {1}".format(k[0:13], radius))    # name and radius
            plt.xlabel('time')
            plt.ylabel('raw flux')

            plt.subplot(2, 2, 3)
            plt.plot(time[~np.isnan(raw)], pdc[~np.isnan(raw)], 'r.') # remove nan
            plt.xlabel('time')
            plt.ylabel('PDC corrected flux')

    plt.show()

if __name__ == '__main__':
    main()
