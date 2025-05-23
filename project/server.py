from flask import Flask, jsonify, request, abort, render_template
from flask_cors import CORS, cross_origin
from linguistDAO import dao

app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)  # Enable CORS for all domains on all routes
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def home():
    return render_template('linguistfinder.html')

@app.route("/linguists", methods=['GET'])
def getAll():
    linguists = dao.getAll()
    return jsonify(linguists)

@app.route('/linguists/<int:LinguistID>', methods=['GET'])
def findById(LinguistID):
    linguist = dao.findByID(LinguistID)
    if linguist:
        return jsonify(linguist)
    else:
        abort(404)

@app.route('/rates/<int:LinguistID>', methods=['GET'])
def getRate(LinguistID):
    rate = dao.getRateByLinguistID(LinguistID)
    if rate:
        return jsonify(rate)
    else:
        abort(404)

@app.route('/linguists', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    linguist_data = request.json
    added_linguist = dao.create(linguist_data)
    return jsonify(added_linguist), 201

@app.route('/linguists/<int:LinguistID>', methods=['PUT'])
def update(LinguistID):
    if not request.json:
        abort(400)
    linguist_data = request.json
    found = dao.findByID(LinguistID)
    if not found:
        abort(404)
    updated = dao.update(LinguistID, linguist_data)
    return jsonify(updated)

@app.route('/linguists/<int:LinguistID>', methods=['DELETE'])
def delete(LinguistID):
    dao.delete(LinguistID)
    return jsonify({"done": True})


if __name__ == '__main__':
    app.run(debug=True)
