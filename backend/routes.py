from flask import Blueprint, request, jsonify
from ai_service import generate_b2b_proposal, generate_product_metadata
from database import save_metadata

api_routes = Blueprint("api_routes", __name__)

@api_routes.route("/generate-tags", methods=["POST"])
def generate_tags():

    data = request.json

    product_name = data.get("product_name")
    description = data.get("description")
    material = data.get("material")

    result = generate_product_metadata(product_name, description, material)

    # save result to database
    save_metadata(product_name, result)

    return jsonify(result)
@api_routes.route("/generate-proposal", methods=["POST"])
def generate_proposal():

    data = request.json

    budget = data.get("budget")
    purpose = data.get("purpose")

    result = generate_b2b_proposal(budget, purpose)

    return jsonify(result)