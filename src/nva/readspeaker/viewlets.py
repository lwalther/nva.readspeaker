from datetime import datetime
from zope.interface import Interface
from uvc.api import api
from plone import api as ploneapi
from plone.app.layout.viewlets.interfaces import IAboveContentTitle
from plone.app.layout.viewlets.interfaces import IAboveContent
from plone.app.layout.viewlets.interfaces import IPortalHeader

api.templatedir('templates')

cid = '10429'
readid = 'content'

class ReadSpeakerScript(api.Viewlet):
    api.context(Interface)
    api.viewletmanager(IPortalHeader)
    

class ReadSpeakerViewlet(api.Viewlet):
    api.context(Interface)
    api.viewletmanager(IAboveContentTitle)

    def available(self):
        #if hasattr(self.context, 'layout'):
        #    if self.context.layout == 'folder_full_view':
        #        return False
        return True
        allowedTypes = ['Document', 'News Item', 'Event', 'Folder',]
        if self.context.portal_type in allowedTypes:
            return True
        return False

    def update(self):
        pageurl = self.context.absolute_url()
        self.buttonid = 'readspeaker_button_%s' % datetime.now().strftime('%f')
        self.readurl = '//app-eu.readspeaker.com/cgi-bin/rsent?customerid=%s&amp;lang=de_de&amp;readid=%s&amp;url=%s' % (cid, readid, pageurl) 
