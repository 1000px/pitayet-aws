from web import db
from datetime import datetime
from flask import url_for
from web.exceptions import ValidationError


class Article(db.Model):
    __tablename__ = 'articles'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512), index=True)
    sec_title = db.Column(db.String(512))
    content = db.Column(db.Text())
    created_time = db.Column(db.DateTime(), default=datetime.utcnow)
    modified_time = db.Column(db.DateTime(), default=datetime.utcnow)

    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    
    comments = db.relationship('Comment', backref='article')

    def to_json(self):
        json_article = {
            'url': url_for('api.get_article', id=self.id),
            'title': self.title,
            'sec_title': self.sec_title,
            'content': self.content,
            'created_time': self.created_time,
            'modified_time': self.modified_time,
            'author_url': url_for('api.get_user', id=self.author_id)
        }
        return json_article

    @staticmethod
    def from_json(json_article):
        title = json_article.get('title')
        if title is None or title == '':
            raise ValidationError('文章标题不能为空！')
        content = json_article.get('content')
        if content is None or content == '':
            raise ValidationError('文章内容不能为空！')
        # 添加作者验证逻辑
        author_id = json_article.get('author_id')

        return Article(
            title           = title,
            sec_title       = json_article.get('sec_title'),
            content         = json_article.get('content'),
            author_id       = author_id
        )