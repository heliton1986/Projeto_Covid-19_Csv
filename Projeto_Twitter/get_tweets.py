 # Importar biblioteca json para processar esse tipo de dado
import json

# Para fazer requisições do twitter
from tweepy import OAuthHandler, Stream, StreamListener

from datetime import datetime

# Cadastrar as chaves de acesso
consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

# Definir um arquivo de saída para armazenar os tweets coletados

# Data de hoje(atual)
date_today = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

# Write está abrindo o arquivo para escrita
out = open(f"collected_tweets_{date_today}.txt", "w")

# Implementar uma classe para conexão com o Twitter
class MyListener(StreamListener):

    # Modificar duas açoes do parâmetro StreamListener
    # Encontrando o dado
    def on_data(self, data): # self é a própria classe
        print(data) # Mostrar os dados
        itemString = json.dumps(data) # é para entender que os dados sao json
        out.write(itemString + "\n") # Pega arquivo de saída e escreve nele os dados json
        return True # Ficar retornando os dados
    
    # Encontrando erros
    def on_error(self, status):
        print(status)

# Implementar função MAIN
if __name__ == "__main__":
    l = MyListener() # Instancia a classe MyListener
    auth = OAuthHandler(consumer_key, consumer_secret) # Para autenticar as chaves do Twitter
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l) # Instancia para fazer o stream
    stream.filter(track=["Covid"]) # Filtrando a palavra Covid