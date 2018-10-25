# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import nva.readspeaker


class NvaReadspeakerLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        self.loadZCML(package=nva.readspeaker)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'nva.readspeaker:default')


NVA_READSPEAKER_FIXTURE = NvaReadspeakerLayer()


NVA_READSPEAKER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(NVA_READSPEAKER_FIXTURE,),
    name='NvaReadspeakerLayer:IntegrationTesting',
)


NVA_READSPEAKER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(NVA_READSPEAKER_FIXTURE,),
    name='NvaReadspeakerLayer:FunctionalTesting',
)


NVA_READSPEAKER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        NVA_READSPEAKER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='NvaReadspeakerLayer:AcceptanceTesting',
)
