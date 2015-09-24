# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from collective.remotesnippets.testing import COLLECTIVE_REMOTESNIPPETS_INTEGRATION_TESTING  # noqa
from collective.remotesnippets.interfaces import ISnippetDocument

import unittest2 as unittest


class SnippetDocumentIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_REMOTESNIPPETS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='SnippetDocument')
        schema = fti.lookupSchema()
        self.assertEqual(ISnippetDocument, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='SnippetDocument')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='SnippetDocument')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(ISnippetDocument.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('SnippetDocument', 'SnippetDocument')
        self.assertTrue(
            ISnippetDocument.providedBy(self.portal['SnippetDocument'])
        )
