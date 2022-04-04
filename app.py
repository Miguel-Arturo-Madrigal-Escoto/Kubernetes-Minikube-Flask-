from flask import Flask, jsonify
from random import randint

import requests, json

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify({'message': 'PokeAPI is running'})

@app.route("/all")
def all():
    fetch = requests.get('https://pokeapi.co/api/v2/pokemon/')
    resp = json.loads(fetch.text)['results']
    return jsonify(resp)

@app.route("/random")
def random():
    n = randint(1, 1126)
    fetch = requests.get(f'https://pokeapi.co/api/v2/pokemon/{ n }')
    
    resp = json.loads(fetch.text)['forms']
    return jsonify(resp)

@app.route("/<int:id>")
def id(id):
    try:
        if id is not None:
            fetch = requests.get(f'https://pokeapi.co/api/v2/pokemon/{ id }')
            resp = json.loads(fetch.text)
            if resp.get('forms'):
                return jsonify(resp['forms'])
            else:
                return jsonify({'message': 'Pokemon not found'})
        else:
            return jsonify({'message': 'Please specify an id'})
    except:
        return jsonify({'message': 'Pokemon not found'})

@app.route("/<string:name>")
def name(name):
    try:
        if name is not None:
            fetch = requests.get(f'https://pokeapi.co/api/v2/pokemon/{ name }')
            resp = json.loads(fetch.text)
            if resp.get('forms'):
                return jsonify(resp['forms'])
            else:
                return jsonify({'message': 'Pokemon not found'})
        else:
            return jsonify({'message': 'Please specify a name'})
    except:
        return jsonify({'message': 'Pokemon not found'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)