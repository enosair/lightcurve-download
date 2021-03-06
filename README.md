lightcurve-download
===================

Download fits data and extract raw flux / pdc process flux / meta data into json file.

Search & Download
-----------------
Find the bundle of Kepler data you want at
http://archive.stsci.edu/kepler/data_search/search.php

Choose the output format to be FILE: WGET LC/TPF commands, this will create a
customized WGET script.

The scripts included are for stars observed in quarter 17 in long cadence. We use the
following abbreviations:
  * conf - confirmed to be exoplanet host star
  * cand - planetary candidates
  * eb   - eclipsing binary
  * fp   - false positive

Process
-------
You will need **PyFITS** module. See

http://www.stsci.edu/institute/software_hardware/pyfits

Run

```bash
python process.py <folder of fits file> <output json file>
```

It will extract the fields for each star and save data to a json file.

Load and plot lightcurves
-------------------------
Run

```bash
python example.py <json file>
```

You will see the first two lightcurves stored in the json file, both raw and
processed flux are plotted.

Examples for long cadence quarter 17 stars:

* confirmed hosts
![confirmed hosts](/example_conf.png)

* candidates
![candidates](/example_cand.png)

* eclipsing binaries
![eclipsing binaries](/example_eb.png)

* false positive
![false positive](/example_fp.png)


Full list of meta data
----------------------
Check **A.1a: Light Curve File Primary Header** in
http://archive.stsci.edu/kepler/manuals/archive_manual.pdf


Remarks
-----------------
The data length depends on quarter.
