import unittest

import stactools.can_flood


class TestModule(unittest.TestCase):

    def test_version(self):
        self.assertIsNotNone(stactools.can_flood.__version__)
