
import unittest
from pyspotify import spotify
import _mockspotify

spotify._spotify = _mockspotify

class MockClient:

    cache_location = "/foo"
    settings_location = "/foo"
    application_key = "appkey_good"
    user_agent = "user_agent_foo"
    username = "username_good"
    password = "password_good"

    def logged_in(self, session, error):
        print "MockClient: logged_in"
        username = session.username()
        self.found_username = username
        session.logout()

class TestSession(unittest.TestCase):

    def test_initialisation(self):
        client = MockClient()
        spotify.run(client)
        self.assertEqual(client.username, client.found_username)



