from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    blogs = db.relationship('Blog',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You do not have permissions to view password')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'


class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    description = db.Column(db.String)
    comments = db.relationship('Comment',backref = 'blog',lazy = "dynamic")
    category = db.Column(db.String)
    def __repr__(self):
        return f'Blog {self.name}'


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))
    def __repr__(self):
        return f'Comment {self.username}'


pass_secure  = db.Column(db.String(255))

@property
def password(self):
    raise AttributeError('You cannot read the password attribute')

@password.setter
def password(self, password):
    self.pass_secure = generate_password_hash(password)


def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)
