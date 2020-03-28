from collections import Callable

from django.conf import settings
from django.test import TestCase

from django_runscript import utilities


class UtilitiesTestCase(TestCase):
    def test_apps_lookup(self):
        self.assertEqual(utilities.apps_lookup('%s'), settings.INSTALLED_APPS)

    def test_import_script(self):
        self.assertIsInstance(utilities.import_script('script_a'), Callable)
        self.assertIsInstance(utilities.import_script('test_app_a.script_a'), Callable)
        self.assertIsInstance(utilities.import_script('tests.test_app_a.script_a'), Callable)
        self.assertIsInstance(utilities.import_script('test_app_a.scripts.script_a'), Callable)
        self.assertIsInstance(utilities.import_script('tests.test_app_a.scripts.script_a'), Callable)

        self.assertIsInstance(utilities.import_script('run_script_a'), Callable)
        self.assertIsInstance(utilities.import_script('test_app_b.run_script_a'), Callable)
        self.assertIsInstance(utilities.import_script('tests.test_app_b.run_script_a'), Callable)
        self.assertIsInstance(utilities.import_script('test_app_b.scripts.run_script_a'), Callable)
        self.assertIsInstance(utilities.import_script('tests.test_app_b.scripts.run_script_a'), Callable)

        self.assertRaises(ImportError, utilities.import_script, 'scripts.script_a')
        self.assertRaises(ImportError, utilities.import_script, 'test_app_a.script_c')
        self.assertRaises(ImportError, utilities.import_script, 'test_app_b.script_a')

        self.assertRaises(ImportError, utilities.import_script, 'scripts.run_script_a')
        self.assertRaises(ImportError, utilities.import_script, 'test_app_b.run_script_c')
