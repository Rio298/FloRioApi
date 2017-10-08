#!flask/bin/python
from flask import Flask, make_response, jsonify, abort
import datetime
from utilities import create_random_game_id

app = Flask(__name__)

@app.route('/')
def index():
    return "Server is Running!"

deviceIds = []
startTime = 0

@app.route('/startgame', methods=['GET'])
def start_game():
    if len(deviceIds) % 2 == 0: #First Device
        new_game_id = create_random_game_id(deviceIds)
        deviceIds.append(new_game_id)

        return make_response(jsonify({'gameId': new_game_id}), 200)
    elif len(deviceIds) % 2 == 1: #Seconde Device
        new_game_id = create_random_game_id(deviceIds)
        deviceIds.append(new_game_id)

        global startTime
        startTime = datetime.datetime.now().second + 5
        if startTime >= 60:
            startTime -= 60

        return make_response(jsonify({'gameId': new_game_id, 'startTime': startTime}), 200)

    abort(404)

@app.route('/gamestatus', methods=['GET'])
def game_status():
    if len(deviceIds) % 2 == 1:
        return make_response(jsonify({"statusText": "Waiting for Player"}), 200)
    if len(deviceIds) % 2 == 0:
        return make_response(jsonify({'startTime': startTime}), 200)

    abort(404)


@app.route('/reset', methods=["GET"])
def reset_game_ids():
    global deviceIds
    deviceIds = []
    return make_response("Success!", 200)

if __name__ == '__main__':
    app.run(debug=True)
