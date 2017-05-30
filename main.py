from google.appengine.ext import ndb
import webapp2
import json


class Message(ndb.Model):
    """Message model"""
    sender = ndb.StringProperty()
    recipient = ndb.StringProperty()
    msg = ndb.TextProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)


class MainPage(webapp2.RequestHandler):
    """
    This class takes care of the main page on a web interface. 
    """
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Brains webapp2 testing server')


class GetListPage(webapp2.RequestHandler):
    """
    This class defines the call to get a fixed list
    """
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(dict([ { "id" : 1,
                                                "avatar_link" : "images/avatars/1.jpg",
                                                "dob" : "1998-12-03",
                                                "email" : "ross@teamengine.org",
                                                "name" : "ross",
                                                "username" : "jiadar" } ]
        )))


class SendMsgPage(webapp2.RequestHandler):
    """
    This class provides a GET call used to store message information in Datastore.
    Uses NDB.
    """
    def get(self):
        sender = self.request.get('sender')
        recipient = self.request.get('recipient')
        msg = self.request.get('message')

        # NDB interaction
        msg_entry = Message(sender=sender, recipient = recipient, msg=msg)
        msg_entry.put()

        self.response.write("ok")



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/get_list', GetListPage),
    ('/send_msg', SendMsgPage),
], debug=True)
