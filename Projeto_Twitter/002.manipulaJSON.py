# Processamento de dados provenientes de um JSON

import urllib.request
import json

def manipulaJSON():
    endereco = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webURL = urllib.request.urlopen(endereco)
    if webURL.getcode() == 200:
        dados = webURL.read()
        oJSON = json.loads(dados)

        # Chave metadata e chave count
        contagem = oJSON["metadata"]["count"]
        print(f"Contagem: {str(contagem)}")

        # Loop pegar chaves 

        for local in oJSON["features"]:
            if local["properties"]["place"] == "3 km SSE of Pāhala, Hawaii":
                print("****Encontrado registro especial****")
            else:
                print(local["properties"]["place"])

manipulaJSON()
            