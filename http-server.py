from flask import Flask, json, request
from flask_cors import CORS
from itertools import count

games = { }
gameIdCounter = count(1)

api = Flask(__name__)
CORS(api)

@api.route("/")
def main():
    return "hello world"

@api.route('/games', methods=['GET'])
def get_games():
    return json.dumps(list(games.values()))

@api.route('/games', methods=['POST'])
def create_game():
    newgame = request.get_json()
    newid = next(gameIdCounter)
    newgame['id'] = newid
    games[newid] = newgame
    return json.dumps(newgame)

@api.route('/games/<int:gameId>', methods=['GET'])
def get_game(gameId):
    return json.dumps(games[gameId])

@api.route('/games/<int:gameId>', methods=['PUT'])
def update_game(gameId):
    game = request.get_json()
    games[game['id']] = game
    return json.dumps(game)

@api.route('/games/<int:gameId>', methods=['DELETE'])
def delete_game(gameId):
    game = games[gameId]
    del games[gameId]
    return json.dumps(game)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=5000, debug=True) 
