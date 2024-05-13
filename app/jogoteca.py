from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console) -> None:
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route("/")

def home():

    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('God of war', 'Rack n slash', 'PS2')

    lista = [jogo1, jogo2]
    
    return render_template("lista.html", titulo="jogos", jogos=lista)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)