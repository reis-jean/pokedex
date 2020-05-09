from flask import Flask, render_template, request, redirect

app = Flask(__name__)

pokemons = [
        ['bulbasaur','https://i.imgur.com/ntcCJr4.png'],
        ['charmander','https://i.imgur.com/5HmVqlW.png'],
        ['squirtle', 'https://i.imgur.com/h2aCkl3.png'],
        ['pikachu', 'https://i.imgur.com/soCJ6J5.png']
    ]

@app.route('/')
def index():
    return render_template(
        'index.html',
        titulo='pokedex',
        pokemons = pokemons
    )

@app.route('/poke/<int:id>')
def pokemon(id):
    poke = pokemons[id]
    return render_template('pokemon.html',
        pokemon = poke 
    )

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/store', methods=['POST'])
def store():
    nome = request.form['nome']
    img = request.form['img']
    
    pokemons.append([nome, img])
    
    return redirect('/')


if __name__ == '__main__':
    app.run()