#!flask/bin/python
from flask import Flask, jsonify
from flask import make_response
from flask import request
from flask_cors import CORS
import pyodbc
con = pyodbc.connect("DRIVER={SQL Server};server=localhost;database=bilvideo")
cursor = con.cursor()
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

def getcomment():
    cursor.execute('select comment from Comment order by commentId desc')
    row = [x for x in cursor]
    return row[0]
    #with open('comments.json', 'w') as fp:
    #    json.dump(comments, fp)
    #with open('comments.csv', 'w') as output_file:
    #    dict_writer = csv.DictWriter(output_file, keys)
    #    dict_writer.writer.writerow(keys)
    #    dict_writer.writerows(comments)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route('/api/getcomments', methods=['GET'])
def get_products():
    newcomment = getcomment()
    #tryclassifier()
    from sentimentAnalysist import duygu_analizi
    sonuc = duygu_analizi().classification(newcomment)
    return jsonify(str(sonuc))


@app.route('/azon/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        return jsonify({'product': 'Not found'}), 404
    return jsonify({'product': product})


@app.route('/api/getcomments', methods=['POST'])
def create_product():
    newProduct = {
        'id': products[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json['description'],
        'price': request.json.get('price', 1),
        'category': request.json['category'],
        'inStock': request.json.get('inStock', False)
    }
    products.append(newProduct)
    return jsonify({'product': newProduct}), 201


@app.route('/azon/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        return jsonify({'product': 'Not found'}), 404
    products.remove(product[0])
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    return make_response(
        jsonify({'HTTP 404 Error': 'The content you looks for does not exist. Please check your request.'}), 404)


if __name__ == '__main__':
    app.run(debug=True)  # !flask/bin/python
yorumlarial()

con.close()