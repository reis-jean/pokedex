from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    pokemons = [
        ['bulbasaur','https://i.imgur.com/ntcCJr4.png'],
        ['charmander','https://i.imgur.com/5HmVqlW.png'],
        ['squirtle', 'https://i.imgur.com/h2aCkl3.png'],
        ['pikachu', 'https://i.imgur.com/soCJ6J5.png']
    ]
    return render_template(
        'index.html',
        titulo='pokedex',
        pokemons = pokemons
    )

if __name__ == '__main__':
    app.run()