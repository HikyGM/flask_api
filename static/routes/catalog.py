from flask import jsonify, request
from config import application
from static.database import db_session
import static.database.__all_models as model


@application.route('/catalog/<int:id_product>', methods=['GET'])
def get_one_product(id_product):
    db_sess = db_session.create_session()
    product = db_sess.query(model.Products.Products).get(id_product)
    if not product:
        return jsonify({'error': 'Not found'})
    return jsonify(product.to_dict(only=(
        'id_products', 'title_product', 'article_number',
        'quantity', 'price', 'category', 'manufacturer'
    )))


@application.route('/catalog', methods=['GET'])
def get_products():
    db_sess = db_session.create_session()
    return jsonify(
        [item.to_dict(only=('id_products', 'title_product',
                            'price', 'category'))
         for item in db_sess.query(model.Products.Products).all()]
    )


@application.route('/catalog', methods=['POST'])
def post_product():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['title', 'article',
                  'quantity', 'price',
                  'category', 'manufacturer']):
        return jsonify({'error': 'Bad request'})
    no_value = {key: 'No value' for key, value in request.json.items() if not value}
    if no_value:
        return jsonify(no_value)
    db_sess = db_session.create_session()
    product = model.Products.Products
    article = db_sess.query(product).filter(product.article_number == request.json['article']).first()
    title = db_sess.query(product).filter(product.title_product == request.json['title']).first()
    errors = {}
    if title:
        errors['title'] = 'Title is used'
    if article:
        errors['article'] = 'Article is used'
    if errors:
        return jsonify(errors)
    add_product = product(
        title_product=request.json['title'],
        article_number=request.json['article'],
        quantity=request.json['quantity'],
        price=request.json['price'],
        category=request.json['category'],
        manufacturer=request.json['manufacturer']
    )
    db_sess.add(add_product)
    db_sess.commit()
    return jsonify({'success': 'OK'})
