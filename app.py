from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = ""
app.config["MONGO_URI"] = ""


mongoDB_cliente = PyMongo(app)
db = mongoDB_cliente.db


planets = [
    {
        "basicDetails": [
            {
                "mass": "5.6834 x 10^26 kg",
                "volume": "8.2713 x 10^14 km^3",
                "period": 10747.0,
                "temperature": 134.0,
                "host_star_mass": 1.0,
                "host_star_temperature": 6000.0
                
            }
        ],
        "description": "Saturn is the sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. It is a gas giant with an average radius of about nine and a half times that of Earth. It has only one-eighth the average density of Earth; however, with its larger volume, Saturn is over 95 times more massive.",
        "id": 6,
        "imgSrc": [
            {
                "img": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Saturn_during_Equinox.jpg",
                "imgDescription": "Pictured in natural color approaching equinox, photographed by Cassini in July 2008; the dot in the bottom left corner is Titan."
            }
        ],
        "key": "45l1h8dab43b",
        "name": "Saturn",
        "planetOrder": "6",
        "source": "Wikipedia",
        "wikiLink": "https://en.wikipedia.org/wiki/Saturn"
    },
    {
        "basicDetails": [
            {
                "mass": "1.8982 x 10^27 kg",
                "volume": "1.4313 x 10^15 km^3",
                "period": 4331.0,
                "temperature": 165.0,
                "host_star_mass": 1.0,
                "host_star_temperature": 6000.0
            }
        ],
        "description": "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass more than two and a half times that of all the other planets in the Solar System combined, but slightly less than one-thousandth the mass of the Sun.",
        "id": 5,
        "imgSrc": [
            {
                "img": "https://upload.wikimedia.org/wikipedia/commons/2/2b/Jupiter_and_its_shrunken_Great_Red_Spot.jpg",
                "imgDescription": "Full disk view in natural colour, taken by the Hubble Space Telescope in April 2014"
            }
        ],
        "key": "75oii1s99r6e",
        "name": "Jupiter",
        "planetOrder": "5",
        "source": "Wikipedia",
        "wikiLink": "https://en.wikipedia.org/wiki/Jupiter"
    },
    {
        "basicDetails": [
            {
                "mass": "(8.6810±0.0013) x 1025 kg",
                "volume": "6.833 x 1013 km^3",
                "period": 30589.0,
                "temperature": 76.0,
                "host_star_mass": 1.0,
                "host_star_temperature": 6000.0
            }
        ],
        "description": "Uranus is the seventh planet from the Sun. Its name is a reference to the Greek god of the sky, Uranus, who, according to Greek mythology, was the great-grandfather of Ares, grandfather of Zeus and father of Cronus. It has the third-largest planetary radius and fourth-largest planetary mass in the Solar System.",
        "id": 7,
        "imgSrc": [
            {
                "img": "https://upload.wikimedia.org/wikipedia/commons/4/48/Uranus_as_seen_by_NASA%27s_Voyager_2_%28remastered%29.png",
                "imgDescription": "Photograph of Uranus in true colour (by Voyager 2 in 1986)"
            }
        ],
        "key": "9jun2xna6ig8",
        "name": "Uranus",
        "planetOrder": "7",
        "source": "Wikipedia",
        "wikiLink": "https://en.wikipedia.org/wiki/Uranus"
    },
]

#consultar todos
@app.route('/planets',methods=['GET'])
def consultAll():
    return jsonify(planets)

#consultar por id
@app.route('/planets/<int:id>',methods=['GET'])
def consultForId(id):
    for planet in planets:
        if planet.get('id') == id:
            return jsonify(planet)
        
#editar 
@app.route('/planets/<int:id>',methods=['PUT'])
def editPlanetForId(id):
    changePlanet = request.get_json()
    for index,planet in enumerate(planets):
        if planet.get('id') == id:
            planets[index].update(changePlanet)
            return jsonify(planets[index])        
        
#criar 
@app.route('/planets',methods=['POST'])
def createPlanet():
    newPlanet = request.get_json()
    planets.append(newPlanet)
    return jsonify(planets)

#excluir
@app.route('/planets/<int:id>',methods=['DELETE'])
def deletePlanet(id):
    for index, planet in enumerate(planets):
        if planet.get('id') == id:
            del planets(index)

            return jsonify(planets)
        


#port=5000,host='localhost'
#verificar a porta para fazer o deploye com o servidor 
#CZ0SdZm85oa9U7aQ mongoDB key
app.run(debug=True)
