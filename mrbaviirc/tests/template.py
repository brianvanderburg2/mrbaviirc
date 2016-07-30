""" Unit tests for the template engine. """

__author__      = "Brian Allen Vanderburg II"
__copyright__   = "Copyright 2016"
__license__     = "MIT"


import os
import json
import glob

import unittest


from .. import template


DATADIR = os.path.join(os.path.dirname(__file__), "template_data")

class TemplateTest(unittest.TestCase):

    def setUp(self):
        self._env = template.Environment()

    def tearDown(self):
        self._env = None

    def test_compare(self):
        """ Run tests by applying template to input and comparing output. """

        with open(os.path.join(DATADIR, "data.json"), "rU") as handle:
            data = json.load(handle)

        for path in sorted(glob.glob(os.path.join(DATADIR, "*.tmpl"))):
            source = path
            target = source[:-5] + ".txt"

            tmpl = self._env.load_file(filename=source)
            rndr = template.StringRenderer()
            tmpl.render(rndr, data)

            contents = rndr.get()

            with open(target, "rU") as handle:
                target_contents = handle.read()

            self.assertEqual(
                contents,
                target_contents,
                "render compare failed: {0}".format(os.path.basename(path))
            )


def suite():
    return unittest.makeSuite(TemplateTest)

