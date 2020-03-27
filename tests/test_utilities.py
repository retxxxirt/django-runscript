from collections import Callable

from django.test import TestCase

from django_runscript import utilities


class UtilitiesTestCase(TestCase):
    def test_import_script(self):
        self.assertIsInstance(utilities.import_script('test_app.script_a'), Callable)
        self.assertIsInstance(utilities.import_script('tests.test_app.script_a'), Callable)

        self.assertRaises(ImportError, utilities.import_script, 'test_app.script_c')
        self.assertRaises(ImportError, utilities.import_script, 'tests.test_app.scripts.script_a')

    def test_import_script_lookup(self):
        self.assertIsInstance(utilities.import_script_lookup('script_a'), Callable)
        self.assertIsInstance(utilities.import_script_lookup('test_app.script_a'), Callable)
        self.assertIsInstance(utilities.import_script_lookup('tests.test_app.script_a'), Callable)
        self.assertIsInstance(utilities.import_script_lookup('test_app.scripts.script_a'), Callable)
        self.assertIsInstance(utilities.import_script_lookup('tests.test_app.scripts.script_a'), Callable)

        self.assertRaises(ImportError, utilities.import_script_lookup, 'scripts.script_a')
        self.assertRaises(ImportError, utilities.import_script_lookup, 'test_app.script_c')
