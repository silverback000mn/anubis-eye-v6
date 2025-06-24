import os
import json

def sincronizar_contas():
    categorias = ["altas", "medias", "baixas"]
    fila = []

    for cat in categorias:
        pasta = f"contas/{cat}"
        if not os.path.exists(pasta):
            continue

        for arquivo in os.listdir(pasta):
            if arquivo.endswith(".json"):
                caminho = os.path.join(pasta, arquivo)
                with open(caminho, "r") as f:
                    dados = json.load(f)
                    fila.append(dados)
                os.remove(caminho)  # Remove da pasta original após pegar

    if fila:
        contas_destino = "dados/contas.json"
        if os.path.exists(contas_destino):
            with open(contas_destino, "r") as f:
                existentes = json.load(f)
        else:
            existentes = []

        todas = existentes + fila

        with open(contas_destino, "w") as f:
            json.dump(todas, f, indent=4, ensure_ascii=False)

        print(f"[sync_contas] {len(fila)} nova(s) conta(s) sincronizadas.")
    else:
        print("[sync_contas] Nenhuma conta nova encontrada.")
