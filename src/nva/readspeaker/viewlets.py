from zope.interface import Interface
from uvc.api import api
from plone import api as ploneapi
from plone.app.layout.viewlets.interfaces import IAboveContentTitle

api.templatedir('templates')

cid = '37'

class ReadSpeakerViewlet(api.Viewlet):
    api.context(Interface)
    api.viewletmanager(IAboveContentTitle)

    def update(self):
        pageurl = self.context.absolute_url()
        self.readurl = "href="//app-na.readspeaker.com/cgi-bin/rsent?customerid=%s&lang=de_de&voice=Max&readid=content&url=%s" % (cid, pageurl)
