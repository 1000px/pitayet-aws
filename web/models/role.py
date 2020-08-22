from web import db
from .permission import Permission

# role 用户角色模型
# 用户角色明细：
## 用户角色     权限                                说明
## 匿名         无                                  对应只读权限，这是未登录的未知用户
## 用户         FOLLOW COMMENT WRITE                具有发布文章、发表评论和关注其他用户的权限；这是新用户的默认角色
## 协管员       FOLLOW COMMENT WRITE MODERATE       增加管理其他用户所发表评论的权限
## 管理员       FOLLOW COMMENT WRITE MODERATE ADMIN 具有所有权限，包括修改其他用户所属角色的权限

class Role(db.Model):
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)

    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm
    
    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm