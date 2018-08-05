from __future__ import print_function
from fs.test import FSTestCases
from dropboxfs.dropboxfs import DropboxFS
import unittest
import os
from dropbox import create_session


def join(a, b):
    return a + b


class TestDropboxFS(FSTestCases, unittest.TestCase):
    def make_fs(self):
        # Return an instance of your FS object here
        self.access_token = (
            "Ozdb24UtqKAAAAAAAAAAC5-zHhrmCXEmdFWu9Dmj0PJrvWn-FCG23zLpt5k6OiGu"
        )

        if "DEV" in os.environ:
            proxies = {
                "http": "http://127.0.0.1:1087",
                "https": "http://127.0.0.1:1087",
            }

            sess = create_session(8, proxies=proxies)
        else:
            sess = None
        fs = DropboxFS(self.access_token, session=sess)

        for f in fs.listdir("/"):
            f = fs.fix_path(f)
            fs.dropbox.files_delete_v2(f)

        return fs

    def test_case_sensitive(self):
        # dropbox  insesitive
        pass
