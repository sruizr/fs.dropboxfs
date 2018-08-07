fs.dropboxfs
============

``fs.dropboxfs`` is a Dropbox driver for PyFileSystem2.


Supported Python versions
-------------------------

- Python 2.7
- Python 3.5
- Python 3.6
- Python 3.7
- PyPy

Usage
-----

Use the ``fs.open_fs`` method with the ``webdav://`` protocol:

.. code:: python

    >>> import fs
    >>> handle = fs.open_fs('webdav://admin:admin@zopyx.com:22082/exist/webdav/db')

or use the public constructor of the ``dropboxfs`` class:

.. code:: python

    >>> from dropboxfs.dropboxfs import dropboxfs
    >>> url = 'http://zopyx.com:22082'
    >>> root = '/exist/webdav/db'
    >>> handle = dropboxfs(url, login='admin', password='admin', root)
    >>> handle.makedir('foo')
    >>> print(handle.listdir('.'))
    ....

Repository
----------

- https://github.com/PyFilesystem/fs.dropboxfs

Issue tracker
-------------

- https://github.com/PyFilesystem/fs.dropboxfs/issues

Tests
-----

- https://travis-ci.org/PyFilesystem/fs.dropboxfs/builds

Author and contributors
-----------------------

- Rehan Khwaja
- Andreas Jung


License
-------

This module is published under the MIT license.

This module was partly and financed by Andreas Jung/ZOPYX


Contact
-------

| Andreas Jung/ZOPYX
| Hundskapfklinge 33
| D-72074 Tübingen
| info@zopyx.com
| www.zopyx.com

