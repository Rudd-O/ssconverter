ssconverter
============================

This is a very small program, maintained and ported to Python 3, that
converts specific sheets of OpenOffice / LibreOffice spreadsheets
to CSV.

Its name is ssconverter.  Its original  and current  purpose is to batch-convert any number of spreadsheets from OpenOffice or LibreOffice into CSV files, with a twist: unlike unoconv, it lets you specify which sheet of the many possible sheets in the spreadsheet file you want to convert.  It's invaluable to speed up batch conversion of CSV files.

Another feature not present in the original is the ability to enable macros and recalculate the spreadsheet right before exporting it to CSV.  This is useful for people who have macro-based formulas in their spreadsheets, which would otherwise export with #VALUE! in every cell position where a macro-based formula was entered.

Installation
------------

Clone the source into a directory on your computer.

Open a terminal and navigate to that directory.

Make an RPM package which you can install by running

```
python3 setup.py bdist_rpm
```

in a terminal window.

Tnstall the created `noarch` RPM inside the `dist/` folder.

Alternatively, you can install it using `python setup.py install`.

Usage
-----

Run the program `ssconverter` without options to get help.

Credits
-------

This program [originated on Linux Journal](https://www.linuxjournal.com/content/convert-spreadsheets-csv-files-python-and-pyuno-part-1v2).
