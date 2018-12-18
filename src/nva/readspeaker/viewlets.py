from zope.interface import Interface
from uvc.api import api
from plone import api as ploneapi
from plone.app.layout.viewlets.interfaces import IAboveContentTitle
from plone.app.layout.viewlets.interfaces import IAboveContent

api.templatedir('templates')

cid = '10429'
readid = 'content'

class ReadSpeakerViewlet(api.Viewlet):
    api.context(Interface)
    api.viewletmanager(IAboveContentTitle)

    def available(self):
        allowedTypes = ['Document', 'News Item', 'Event', 'Folder',]
        if self.context.portal_type in allowedTypes:
            return True
        return False

    def update(self):
        pageurl = self.context.absolute_url()
        self.readurl = '//app-eu.readspeaker.com/cgi-bin/rsent?customerid=%s&amp;lang=de_de&amp;readid=%s&amp;url=%s' % (cid, readid, pageurl) 
