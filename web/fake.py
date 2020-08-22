from random import randint
from sqlalchemy.exc import IntegrityError
from web import db
from faker import Faker
from web.models import User, Article, Subject, Comment

def users(count=100):
    fake = Faker(locale='zh_CN')
    i = 0
    while i < count:
        u = User(
            email       =fake.email(),
            username    = fake.user_name(),
            password    = '123456',
            confirmed   = True,
            name        = fake.name(),
            location    = fake.city(),
            about_me    = fake.text(),
            member_since= fake.past_date()
        )
        db.session.add(u)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()

def articles(count=100):
    fake = Faker(locale='zh_CN')
    user_count = User.query.count()
    subject_count = Subject.query.filter_by(is_leaf=True).count()
    for i in range(count):
        u = User.query.offset(randint(0, user_count-1)).first()
        subject = Subject.query.filter_by(is_leaf=True).offset(randint(0, subject_count-1)).first()
        a = Article(
            title           = fake.sentence(),
            sec_title       = fake.sentence(),
            content         = fake.text(),
            created_time    = fake.past_date(),
            author          = u,
            subject         = subject
        )
        db.session.add(a)
    db.session.commit()

def subjects(count=3):
    fake = Faker(locale='zh_CN')
    for i in range(count):
        sub_subjects = []
        for j in range(4):
            st = Subject(
                name        = fake.word(),
                is_root     = False,
                is_leaf     = True,
                sub_subjects= []
            )
            sub_subjects.append(st)
        
        s = Subject(
            name            = fake.word(),
            is_root         = True,
            is_leaf         = False,
            sub_subjects    = sub_subjects
        )
        db.session.add(s)
    db.session.commit()

def comments(count=100):
    fake = Faker('zh_CN')
    user_count = User.query.count()
    article_count = Article.query.count()
    for i in range(count):
        _user = User.query.offset(randint(0, user_count-2)).first()
        _article = Article.query.offset(randint(0, article_count-1)).first()
        comment = Comment(
            content         = fake.text(),
            content_html    = '',
            reviewer        = _user,
            article         = _article
        )
        db.session.add(comment)
        # db.session.commit()
    # user = User.query.offset(randint(0, user_count-1)).first()
    # article = Article.query.offset(randint(0, article_count-1)).first()
    # user = User.query.filter_by(id=20).first()
    # article = Article.query.filter_by(id=30).first()
    # comment = Comment(
    #     content             = fake.text(),
    #     content_html        = '',
    #     reviewer            = user,
    #     article             = article
    # )
    # db.session.add(comment)
    db.session.commit()