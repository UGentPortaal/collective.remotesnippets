# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.remotesnippets


class CollectiveRemotesnippetsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.remotesnippets)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.remotesnippets:default')


COLLECTIVE_REMOTESNIPPETS_FIXTURE = CollectiveRemotesnippetsLayer()


COLLECTIVE_REMOTESNIPPETS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_REMOTESNIPPETS_FIXTURE,),
    name='CollectiveRemotesnippetsLayer:IntegrationTesting'
)


COLLECTIVE_REMOTESNIPPETS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_REMOTESNIPPETS_FIXTURE,),
    name='CollectiveRemotesnippetsLayer:FunctionalTesting'
)


COLLECTIVE_REMOTESNIPPETS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_REMOTESNIPPETS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveRemotesnippetsLayer:AcceptanceTesting'
)
