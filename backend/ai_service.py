import random

def generate_product_metadata(product_name, description, material):

    name = (product_name or "").lower()
    desc = (description or "").lower()
    mat = (material or "").lower()

    # category rules
    if "toothbrush" in name:
        primary = "Personal Care"
        sub = "Toothbrush"
    elif "bottle" in name:
        primary = "Kitchenware"
        sub = "Bottle"
    elif "bag" in name:
        primary = "Accessories"
        sub = "Reusable Bag"
    else:
        primary = "Eco Products"
        sub = "General"

    # SEO tags
    tags = [
        f"{material} {product_name}".lower(),
        f"eco friendly {product_name}".lower(),
        f"sustainable {product_name}".lower(),
        f"{product_name} reusable".lower(),
        f"plastic free {product_name}".lower()
    ]

    # sustainability filters
    filters = []

    if mat in ["bamboo", "wood", "coconut"]:
        filters.append("biodegradable")

    if "plastic" not in mat:
        filters.append("plastic-free")

    filters.append("eco-friendly")

    return {
        "primary_category": primary,
        "sub_category": sub,
        "seo_tags": tags,
        "sustainability_filters": filters
    }


def generate_b2b_proposal(budget, purpose):

    budget = int(budget)

    notebook_budget = int(budget * 0.4)
    bottle_budget = int(budget * 0.4)
    card_budget = int(budget * 0.2)

    proposal = {
        "product_mix": [
            {"product": "Bamboo Notebook", "quantity": notebook_budget // 200},
            {"product": "Reusable Steel Bottle", "quantity": bottle_budget // 300},
            {"product": "Seed Paper Cards", "quantity": card_budget // 50}
        ],
        "budget_allocation": {
            "notebooks": notebook_budget,
            "bottles": bottle_budget,
            "cards": card_budget
        },
        "estimated_total_cost": budget,
        "impact_summary": "Using reusable and biodegradable products reduces plastic waste and promotes sustainable gifting."
    }

    return proposal