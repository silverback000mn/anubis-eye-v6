import requests
import os
import random
import time

def baixar_fotos(qtd=12, pasta_destino="fotos/"):
    os.makedirs(pasta_destino, exist_ok=True)
    print(f"[FOTOS] Salvando {qtd} imagens em: {pasta_destino}")
    
    for i in range(qtd):
        url = f"https://source.unsplash.com/random/400x400?sig={random.randint(1,9999)}"
        response = requests.get(url)
        if response.status_code == 200:
            caminho = os.path.join(pasta_destino, f"img_{i+1}.jpg")
            with open(caminho, "wb") as f:
                f.write(response.content)
            print(f"[FOTOS] 📷 Imagem salva: {caminho}")
        time.sleep(1.5)

if __name__ == "__main__":
    baixar_fotos()
