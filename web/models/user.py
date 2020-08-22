from web import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import url_for
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(128), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    avatar_hash = db.Column(db.String(64))
    confirmed = db.Column(db.Boolean, default=False)

    articles = db.relationship('Article', backref='author')
    comments = db.relationship('Comment', backref='reviewer')

    @property
    def password(self):
        raise AttributeError('password是非可读属性.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_json(self):
        json_user = {
            'url': url_for('api.get_user', id=self.id),
            'username': self.username,
            'email': self.email,
            'name': self.name,
            'location': self.location,
            'about_me': self.about_me,
            'avatar_hash': self.avatar_hash,
            'confirmed': self.confirmed  
        }
        return json_user