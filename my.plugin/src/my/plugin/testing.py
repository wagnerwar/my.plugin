# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import my.plugin


class MyPluginLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=my.plugin)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'my.plugin:default')


MY_PLUGIN_FIXTURE = MyPluginLayer()


MY_PLUGIN_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MY_PLUGIN_FIXTURE,),
    name='MyPluginLayer:IntegrationTesting'
)


MY_PLUGIN_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MY_PLUGIN_FIXTURE,),
    name='MyPluginLayer:FunctionalTesting'
)


MY_PLUGIN_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MY_PLUGIN_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='MyPluginLayer:AcceptanceTesting'
)
