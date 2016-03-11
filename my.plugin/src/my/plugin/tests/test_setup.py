# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from my.plugin.testing import MY_PLUGIN_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that my.plugin is properly installed."""

    layer = MY_PLUGIN_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if my.plugin is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'my.plugin'))

    def test_browserlayer(self):
        """Test that IMyPluginLayer is registered."""
        from my.plugin.interfaces import (
            IMyPluginLayer)
        from plone.browserlayer import utils
        self.assertIn(IMyPluginLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MY_PLUGIN_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['my.plugin'])

    def test_product_uninstalled(self):
        """Test if my.plugin is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'my.plugin'))
