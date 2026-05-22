<<<<<<< HEAD
from extensions import db
=======
from app import db
>>>>>>> upstream/master

# MODELS
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
<<<<<<< HEAD
    username = db.Column(db.String(100), nullable=False)

    posts = db.relationship("Post", backref="user")

=======
    email = db.Column(db.String(100), nullable=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(500), nullable=True)

    posts = db.relationship("Post", backref='user')
>>>>>>> upstream/master

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
<<<<<<< HEAD

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    comments = db.relationship("Comment", backref="post")

=======
    user_id = db.Column(db.Integer, db.ForeignKey("user.id") )

    comments = db.relationship("Comment", backref='post')
>>>>>>> upstream/master

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)

<<<<<<< HEAD
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
=======
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))



class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False)
>>>>>>> upstream/master
