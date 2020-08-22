from web.api import api
from web.models import Article
from .authentication import auth
from flask import jsonify, request, url_for, abort
from flask_login import login_required

# 获取文章列表，分页数据
@api.route('/articles/')
@auth.login_required
def get_articles():
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.paginate(
        page, per_page=20,
        error_out=False
    )
    articles = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_articles', page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_articles', page=page+1)

    return jsonify({
        'articles': [article.to_json() for article in articles],
        'prev_url': prev,
        'next_url': next,
        'count': pagination.total
    })

# 根据id获取文章信息，单个数据
@api.route('/articles/<int:id>')
def get_article(id):
    article = Article.query.filter_by(id=id).first()
    # 错误判断
    if article is None:
        abort(404)
    return article.to_json()

# 新增一篇文章
@api.route('/articles/', methods=['POST'])
def new_article():
    article = Article.from_json(request.json)
    db.session.add(article)
    db.session.commit()
    return article.to_json()

# 根据id修改文章内容
@api.route('/articles/<int:id>', methods=['PUT'])
def edit_article(id):
    article = Article.query.filter_by(id=id).first()
    article.title = request.json.get('title')
    article.sec_title = request.json.get('sec_title')
    article.content = request.json.get('content')
    db.session.add(article)
    db.session.commit()
    return article.to_json()

# 根据id删除文章
@api.route('/articles/<int:id>', methods=['DELETE'])
def del_article(id):
    pass

# 不提供批量删除文章功能

# 根据分类id获取该分类下文章列表
@api.route('/articles/author_or_subject/')
def get_articles_by_author_or_subject():
    author_id = request.args.get('author_id', None, type=int)
    subject_id = request.args.get('subject_id', None, type=int)
    query = Article.query
    if author_id is not None:
        query = query.filter_by(author_id=author_id)
    if subject_id is not None:
        query = query.filter_by(subject_id=subject_id)

    page = request.args.get('page', 1, type=int)
    pagination = query.paginate(
        page,
        per_page=20,
        error_out=False
    )

    articles = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_articles_by_author_or_subject', page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_articles_by_author_or_subject', page=page+1)

    return jsonify({
        'articles': [article.to_json() for article in articles],
        'prev_url': prev,
        'next_url': next,
        'count': pagination.total
    })