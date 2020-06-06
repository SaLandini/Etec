from flask import Flask, render_template
app = Flask(__name__)

@app.route('/tarefas')
def hello_world():
    menssage = "TAREFA CARAI"
    return render_template("tabela.html", menssage=menssage)

if __name__ == "__main__":
    app.run()