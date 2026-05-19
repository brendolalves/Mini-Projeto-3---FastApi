import requests

URL = "http://127.0.0.1:8000/produtos"

resposta = requests.get(URL)

if resposta.status_code == 200:
    dados_produtos = resposta.json()
    for produto in dados_produtos:
        print(f"Produto: {produto['nome']} - R$ {['preco']}")
else:
    print("Erro ao consumir o API. ")
