#!/usr/bin/python3
"""
Task 3: Displaying Data from JSON or CSV Files in Flask
"""

import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(filepath):
    """Read and parse product data from a JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def read_csv(filepath):
    """Read and parse product data from a CSV file."""
    products = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Read items from items.json and render them using items.html."""
    try:
        with open('items.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    """Display products from JSON or CSV based on query parameters."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id is not None:
        try:
            target_id = int(product_id)
            data = [p for p in data if int(p['id']) == target_id]
        except ValueError:
            data = []

        if not data:
            return render_template(
                'product_display.html', error='Product not found'
            )

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
