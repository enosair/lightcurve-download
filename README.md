lightcurve-download
===================

Download fits data and extract raw flux / pdc process flux / meta data, save to
json file.

Search & Download
-----------------
Find the bundle of Kepler data you want at

http://archive.stsci.edu/kepler/data_search/search.php

Choose the output format to be FILE: WGET LC/TPF commands, this will create a
customized WGET script.

Process
-------
Run

```python
python process.py <folder of fits file> <output json file>
```

It will extract the fields and save it to a json file.
