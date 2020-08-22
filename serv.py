import os
from web import create_app, db
from web.models import Article, User, Subject, Comment
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(
        db          = db,
        Article     = Article,
        User        = User,
        Subject     = Subject,
        Comment     = Comment
    )

@app.cli.command()
def test():
    """Run the unit tests."""
    pass