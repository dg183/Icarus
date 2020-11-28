from flask import Flask, jsonify
import json
from json import JSONEncoder

class SpaceshipEncoder(JSONEncoder):
    def default(self, o):
            return o.__dict__


# key = id, value = Spaceship (object)
ships = {}

class Spaceship:
    spaceshipCount = 0

    def __init__(self, name, model, location, status):
        self.id = Spaceship.spaceshipCount
        Spaceship.spaceshipCount += 1
        self.name = name
        self.model = model
        self.location = location
        self.status = status


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

app = Flask(__name__)

# ========================
# =
# =     Default route
# =
# ========================
@app.route('/')
def hello():
    return 'Welcome to Icarus'

# ========================
# =
# =     Add spaceship
# =
# ========================
@app.route('/addShip')
def addSpaceship():
    s = Spaceship('Name','MyModel','Thislocation','Maintenance')
    print(s.toJSON())

    ships[s.id] = s

    return s.toJSON()

# ========================
# =
# =      List spaceships (NOT REQUIRED)
# =
# ========================
@app.route('/listShips')
def listShips():
    jsonStr = json.dumps(ships, indent=4, cls=SpaceshipEncoder)
    print(jsonStr)
    return jsonStr

# ========================
# =
# =      TODO: Update spaceship
# =
# ========================
# TODO: make PUT request
# TODO: add queries
@app.route('/updateShip')
def updateShip():
    return "/updateShip"

# ========================
# =
# =      TODO: Add location
# =
# ========================
# TODO: make POST request
# TODO: add queries
@app.route('/addLocation')
def addLocation():
    return "/addLocation"

# ========================
# =
# =      TODO: Remove spaceship
# =
# ========================
# TODO: make DEL request
# TODO: add queries
@app.route('/removeShip')
def removeShip():
    return "/removeShip"

# ========================
# =
# =      TODO: Remove location
# =
# ========================
# TODO: make DEL request
# TODO: add queries
@app.route('/removeLocation')
def removeLocation():
    return "/removeLocation"

# ========================
# =
# =      TODO: Travel
# =
# ========================
# TODO: make POST request
# TODO: add queries
@app.route('/travel')
def travel():
    return "/travel"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
    