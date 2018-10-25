# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from nva.readspeaker.testing import NVA_READSPEAKER_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that nva.readspeaker is properly installed."""

    layer = NVA_READSPEAKER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if nva.readspeaker is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'nva.readspeaker'))

    def test_browserlayer(self):
        """Test that INvaReadspeakerLayer is registered."""
        from nva.readspeaker.interfaces import (
            INvaReadspeakerLayer)
        from plone.browserlayer import utils
        self.assertIn(
            INvaReadspeakerLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = NVA_READSPEAKER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['nva.readspeaker'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if nva.readspeaker is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'nva.readspeaker'))

    def test_browserlayer_removed(self):
        """Test that INvaReadspeakerLayer is removed."""
        from nva.readspeaker.interfaces import \
            INvaReadspeakerLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            INvaReadspeakerLayer,
            utils.registered_layers())
