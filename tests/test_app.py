from flask import url_for
from flask_testing import TestCase

from app import app, db, Players, Games

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False)
        return app

def setUp(self):
    db.create_all()

    sample1 = Players(name = "MissWoman", alliance = "Ally", current_rating = 1500)

    db.session.add(sample1)
    db.session.commit()

def tearDown(self):

    db.session.remove()
    db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'MissWoman', response.data)

# Test adding 
class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('home'),
            data = dict(name="MrMan"),
            follow_redirects=True
        )
        self.assertIn(b'MrMan',response.data)