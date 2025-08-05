from flask import Blueprint
total_merit_bp = Blueprint("total_merit", __name__, url_prefix="/total-merit")

@total_merit_bp.route("/")
def merit_index():
    return "Total Merit placeholder"