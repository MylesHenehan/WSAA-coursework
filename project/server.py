from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
from linguistDAO import linguistDAO

app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)  # Enable CORS for all domains on all routes
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/linguists')
@cross_origin()
def getAll():
    results = linguistDAO.getAll()
    return jsonify(results)


@app.route('/linguists/<int:LinguistID>')
@cross_origin()
def findById(LinguistID):
    foundlinguist = linguistDAO.findByID(LinguistID)
    return jsonify(foundlinguist) if foundlinguist else abort(404)


@app.route('/linguists', methods=['POST'])
@cross_origin()
def create():
    if not request.json:
        abort(400)

    linguist = {
        "LinguistName": request.json['LinguistName'],
        "LinguistEmail": request.json['LinguistEmail'],
        "TargetLocale": request.json['TargetLocale'],
    }
    addedlinguist = linguistDAO.create(linguist)
    return jsonify(addedlinguist), 201


@app.route('/linguists/<int:LinguistID>', methods=['PUT'])
@cross_origin()
def update(LinguistID):
    foundlinguist = linguistDAO.findByID(LinguistID)
    if not foundlinguist:
        abort(404)

    if not request.json:
        abort(400)
    reqJson = request.json

    if 'LinguistName' in reqJson:
        foundlinguist['LinguistName'] = reqJson['LinguistName']
    if 'LinguistEmail' in reqJson:
        foundlinguist['LinguistEmail'] = reqJson['LinguistEmail']
    if 'TargetLocale' in reqJson:
        foundlinguist['TargetLocale'] = reqJson['TargetLocale']

    linguistDAO.update(LinguistID, foundlinguist)
    return jsonify(foundlinguist)


@app.route('/linguists/<int:LinguistID>', methods=['DELETE'])
@cross_origin()
def delete(LinguistID):
    linguistDAO.delete(LinguistID)
    return jsonify({"done": True})


if __name__ == '__main__':
    app.run(debug=True)
