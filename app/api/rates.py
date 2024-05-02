from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from app.service import RatesService
from app.schemas import RateSchema, PriceSchema

blp = Blueprint("Rates API", __name__, description="Rates Task API")

@blp.route("/rates")
class Rates(MethodView):
    
    @blp.arguments(RateSchema, location="query")
    @blp.response(200, PriceSchema(many=True))
    def get(self, args):
        date_from = args.get("date_from")
        date_to = args.get("date_to")
        origin = args.get("origin")
        destination = args.get("destination")
        try:
            prices = RatesService.get_prices(date_from, date_to, origin, destination)
        except ValueError as err:
            abort(400, message=str(err))
        except Exception as err:
            abort(500, message=str(err))
        
        return prices