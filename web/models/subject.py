from web import db
from flask import jsonify, url_for
from web.exceptions import ValidationError

# 文章分类

class Subject(db.Model):
    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    is_root = db.Column(db.Boolean, default=False)
    is_leaf = db.Column(db.Boolean, default=False)

    articles = db.relationship('Article', backref='subject')

    parent_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    parent = db.relationship(
        'Subject',
        foreign_keys    = [parent_id,],
        remote_side     = [id],
        backref         = 'sub_subjects'
    )

    @staticmethod
    def from_json(json_subject):
        # 
        name = json_subject.get('name')
        if name is None or name == '':
            raise ValidationError('文章分类必须有名称.')
        return Subject(
            name        = json_subject.get('name'),
            is_root     = json_subject.get('is_root'),
            is_leaf     = json_subject.get('is_leaf'),
            parent_id   = json_subject.get('parent_id')
        )