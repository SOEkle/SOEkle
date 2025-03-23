from flask import Flask
import random

app = Flask(__name__)

# List of space facts
space_facts = [
    "The Sun is over 4.5 billion years old.",
    "A day on Venus is longer than a year on Venus.",
    "There are more stars in the universe than grains of sand on Earth.",
    "The largest volcano in the solar system is on Mars.",
    "Light from the Sun takes about 8 minutes to reach Earth."
]

@app.route('/')
def home():
    return random.choice(space_facts)

if __name__ == "__main__":
    app.run()
