from web import db
from datetime import datetime

class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text())
    content_html = db.Column(db.Text())
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow)

    reviewer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))