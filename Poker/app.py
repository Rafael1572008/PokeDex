from flask import Flask, request, jsonify, json, redirect, url_for, render_template
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():

    return redirect(url_for('requisicao'))
    
@app.route("/hello")
def requisicao():
    name_get = "mewtwo"

    # Caos rode em lugar que tenha prox (IFSP)
    """proxies = {
        "http": "proxy.spo.ifsp.edu.br:3128",
        "https": "http://proxy.spo.ifsp.edu.br:3128"
    } 
        
        response = requests.get(
        "https://pokeapi.co/api/v2/pokemon/bulbasaur",
        proxies=proxies,
        verify=False
    ) """

    response = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{name_get}").text)

    img_poker = response['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
    name_poker = response['forms'][0]['name']
    id_poker = response['id']


    info_poker = {"name_poker": name_poker,
                  "id_poker": id_poker,
                  "img_poker": img_poker,
                  }
    
    return render_template('final.html', info_poker = info_poker)

    

if __name__ == '__main__':
    app.run(debug=True)