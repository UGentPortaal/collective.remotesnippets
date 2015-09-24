# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.remotesnippets.testing import COLLECTIVE_REMOTESNIPPETS_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that collective.remotesnippets is properly installed."""

    layer = COLLECTIVE_REMOTESNIPPETS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.remotesnippets is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.remotesnippets'))

    def test_browserlayer(self):
        """Test that ICollectiveRemotesnippetsLayer is registered."""
        from collective.remotesnippets.interfaces import ICollectiveRemotesnippetsLayer
        from plone.browserlayer import utils
        self.assertIn(ICollectiveRemotesnippetsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_REMOTESNIPPETS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.remotesnippets'])

    def test_product_uninstalled(self):
        """Test if collective.remotesnippets is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('collective.remotesnippets'))
