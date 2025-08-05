from flask import Blueprint
news_bp = Blueprint("news", __name__, url_prefix="/<lang>/news")

@news_bp.route("/")
def news_home(lang):
    return "News list (coming soon)"