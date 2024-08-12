from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Product

@app.route('/')
def index():
    products = Product.query.all()  # Get all products
    return render_template('product_list.html', products=products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        quantity = int(request.form['quantity'])  # Convert quantity to integer
        price = float(request.form['price'])  # Convert price to float
        new_product = Product(name=name, quantity=quantity, price=price)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('product_form.html')

@app.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get(product_id)  # Get product by ID
    if request.method == 'POST':
        product.name = request.form['name']
        product.quantity = int(request.form['quantity'])
        product.price = float(request.form['price'])
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('product_form.html', product=product)

@app.route('/delete_product/<int:product_id>')
def delete_product(product_id):
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('index'))
