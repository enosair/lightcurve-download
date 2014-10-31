lightcurve-download
===================

Download fits data and extract raw flux / pdc process flux / meta data, save to
json file.

Search & Download
-----------------
Find the bundle of Kepler data you want at

http://archive.stsci.edu/kepler/data\_search/search.php

Choose the output format to be FILE: WGET LC/TPF commands, this will create a
customized WGET script.

The scripts included are for long cadence lightcurves in quarter 17. We use
following abbreviations:
  * conf - confirmed to be exoplanet host star
  * cand - planetary candidates
  * eb   - eclipsing binary
  * fp   - false positive

Process
-------
Run

```python
python process.py <folder of fits file> <output json file>
```

It will extract the fields and save it to a json file.

Load and plot lightcurves
-------------------------
Run

```python
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
