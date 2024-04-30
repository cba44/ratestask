from flask.views import MethodView
from flask_smorest import Blueprint

blp = Blueprint("api", __name__, description="Rates Task API")

@blp.route("/rates")
class Rates(MethodView):
    
    def get(self):
        return "Rates"