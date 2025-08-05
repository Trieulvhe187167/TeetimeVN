from flask import Blueprint, jsonify
import sqlite3, datetime
from pathlib import Path

fx_bp = Blueprint("fx", __name__, url_prefix="/api/fx")
DB = Path("data/teetimevn_dev.db")

@fx_bp.route("/<ccy>")
def latest_rate(ccy):
    ccy = ccy.upper()
    today = datetime.date.today().isoformat()
    sql = "SELECT rate_to_vnd FROM fx_rate WHERE rate_date=? AND currency=?"
    rate = sqlite3.connect(DB).execute(sql, (today, ccy)).fetchone()
    if not rate:
        return jsonify({"error": "rate not found"}), 404
    return jsonify({"currency": ccy, "rate_to_vnd": rate[0]})