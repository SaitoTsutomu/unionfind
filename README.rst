`unionfind` is a package for unionfind.

::

   from unionfind import unionfind
   u = unionfind(3) # There are 3 items.
   u.unite(0, 2) # Set 0 and 2 to same group.
   u.issame(1, 2) # Ask "Are 1 and 2 same?"
   u.groups() # Return groups.

See also https://pypi.org/project/ortoolpy/

Requirements
------------
* Python 3

Features
--------
* nothing

Setup
-----
::

   $ pip install unionfind

History
-------
0.0.1 (2015-4-3)
~~~~~~~~~~~~~~~~~~
* first release
