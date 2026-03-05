# Rayeva AI Systems Assignment

Applied AI modules for sustainable commerce.

## Implemented Modules

### 1. AI Auto Category & Tag Generator
Automatically analyzes product details and generates:

- Primary category
- Sub-category
- SEO tags
- Sustainability filters

Example Output

{
 "primary_category": "Personal Care",
 "sub_category": "Toothbrush",
 "seo_tags": ["eco friendly toothbrush","bamboo toothbrush"],
 "sustainability_filters": ["plastic-free","biodegradable"]
}

---

### 2. AI B2B Proposal Generator

Generates sustainable product proposals based on budget.

Example Input

budget: 50000  
purpose: corporate gifting

Example Output

{
 "product_mix":[
  {"product":"Bamboo Notebook","quantity":100},
  {"product":"Reusable Steel Bottle","quantity":80}
 ],
 "estimated_total_cost":50000,
 "impact_summary":"Using reusable products reduces plastic waste."
}

---

## Architecture

Frontend (HTML test page)  
↓  
Flask API (routes.py)  
↓  
AI Logic Layer (ai_service.py)  
↓  
Database Layer (SQLite)

---

## Tech Stack

Python  
Flask  
SQLite  
HTML / JavaScript

---

## API Endpoints

POST /generate-tags  
POST /generate-proposal

---

## Project Structure

backend/  
 ├── app.py  
 ├── routes.py  
 ├── ai_service.py  
 └── database.py  

logs/  
test.html  
products.db  
requirements.txt

---

## Future Modules (Architecture Only)

Impact Reporting Generator  
- Calculate plastic saved  
- Estimate carbon reduction  
- Generate sustainability report  

WhatsApp Support Bot  
- Answer order status queries  
- Provide return policy info  
- Escalate refund issues

---

## Demo

Run backend

python backend/app.py

Open

test.html

Generate product metadata and view structured output.

## Demo Video

Project demonstration:
## Demo Video

Project demonstration:
https://drive.google.com/file/d/1htlQVKmXm6RxcR19eBrkNfAfC8Iojn4c/view?usp=drivesdk