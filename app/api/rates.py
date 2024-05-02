from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint

from app.service import RatesService

blp = Blueprint("api", __name__, description="Rates Task API")

@blp.route("/rates")
class Rates(MethodView):
    
    def get(self):
        date_from = request.args.get("date_from")
        date_to = request.args.get("date_to")
        origin = request.args.get("origin")
        destination = request.args.get("destination")
        prices = RatesService.get_prices(date_from, date_to, origin, destination)
        # return [date_from, date_to, origin, destination]
        return "Rates"