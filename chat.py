from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def chat():
    mensagens = [("Cauê","Como você está?"),("Gustavo","Estou bem e você?"),("Cauê","Também estou")]
    if len(request.args) > 0:
        mensagem_nova = (request.args['nome'], request.args['mensagem'])
        mensagens.append(mensagem_nova)
    print(mensagens)
    return render_template("chat.html", mensagens=mensagens)



app.run(debug=True, port=5001)
