from flask import Flask, request, jsonify, json, redirect, url_for, render_template
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():

    return redirect(url_for('requisicao'))
    
@app.route("/hello", methods = ['GET'])
def requisicao():
    name = "pikachu"
    
    proxies = {
    "http": "proxy.spo.ifsp.edu.br:3128",
    "https": "http://proxy.spo.ifsp.edu.br:3128"
}
    
    response = requests.get(
    "https://pokeapi.co/api/v2/pokemon/bulbasaur",
    proxies=proxies,
    verify=False
)
    
    response = json.loads(response.text)['sprites']['front_default']
    
    return render_template('final.html', response = response)
    
    
    

if __name__ == '__main__':
    app.run(debug=True)