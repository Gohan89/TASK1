from flask import Flask, jsonify
import random

app = Flask(__name__)

animes = [
    "Naruto",
    "One Piece",
    "Attack on Titan",
    "My Hero Academia",
    "Demon Slayer",
    "Fullmetal Alchemist",
    "Sword Art Online",
    "Death Note",
    "Fairy Tail",
    "Tokyo Ghoul"
]

@app.route('/suggest', methods=['GET'])
def suggest_anime():
    anime = random.choice(animes)
    return jsonify({'suggestion': anime})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
