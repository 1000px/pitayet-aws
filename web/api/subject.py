from web.api import api
from web.models import Subject
from web import db
from flask import jsonify, url_for, request

# 获取所有文章类目
@api.route('/subjects/')
def get_subjects():
    subjects = Subject.query.filter_by(is_root=True).all()
    return jsonify(recurse(subjects, 0))

# 根据id获取某个文章类目（及其子类目）
@api.route('/subjects/<int:id>')
def get_subject(id):
    subject = Subject.query.filter_by(id=id).first()
    return jsonify(recurse([subject], 0))

# 根据id修改某个类目信息（不能修改子类目列表）
@api.route('/subjects/<int:id>', methods=['PUT'])
def edit_subject(id):
    subject = Subject.query.filter_by(id=id).first()

    json_req = request.json
    subject.name = json_req.get('name')
    subject.parent_id = json_req.get('parent_id')
    subject.is_root = json_req.get('is_root')
    subject.is_leaf = json_req.get('is_leaf')

    db.session.add(subject)
    db.session.commit()
    return jsonify(recurse([subject], 0))

# 新增一个类目
@api.route('/subjects/', methods=['POST'])
def new_subject():
    subject = Subject.from_json(request.json)
    db.session.add(subject)
    db.session.commit()
    return jsonify(recurse([subject], 0))

def recurse(subjects, level):
    subs = []
    level += 1
    for sub in subjects:
        sub_subjects = None
        subObj = {
            'url': url_for('api.get_subject', id=sub.id),
            'id': sub.id,
            'level': level,
            'name': sub.name,
            'parent_id': sub.parent_id,
            'is_root': sub.is_root,
            'is_leaf': sub.is_leaf,
        }
        if sub.is_leaf == False:
            sub_subjects = recurse(sub.sub_subjects, level)
            subObj['children'] = sub_subjects
        subs.append(subObj)
    return subs