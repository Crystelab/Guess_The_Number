from flask import Flask, jsonify, request
from flask_cors import CORS
from model import GameModel, RoundModel

app = Flask(__name__)
CORS(app)
gameModel = GameModel()
roundModel = RoundModel()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/begin", methods=['POST'])
def begin():
    gameId = gameModel.add_game()
    return jsonify({"message": "Game added", "id": gameId}), 201


@app.route('/api/game', methods=['GET'])
def get_games():
    games = gameModel.get_all_games()
    return jsonify(games), 200

@app.route('/api/game/<int:gameId>', methods=['GET'])
def get_game(gameId):
    game = gameModel.get_game(gameId)
    if game:
        return jsonify(game), 200
    return jsonify({"error": "Game not found"}), 404

@app.route("/api/guess", methods=['POST'])
def guess():
    data = request.get_json()
    gameId = data.get('gameId')
    guess = data.get('guess')
    roundId = roundModel.add_round(gameId, guess)
    return jsonify({"message": "Round added", "id": roundId}), 201

@app.route('/api/rounds/<int:gameId>', methods=['GET'])
def get_rounds(gameId):
    rounds = roundModel.get_rounds(gameId)
    if rounds:
        return jsonify(rounds), 200
    return jsonify({"error": "Game not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)