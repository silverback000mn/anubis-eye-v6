import os
import json
import time
import psutil
from datetime import datetime

IA_NOMES = ["IA_RA", "IA_Isis", "IA_Sauron", "IA_Tempo", "HORUS", "Watchdog"]
STATUS_DIR = "status"
os.makedirs(STATUS_DIR, exist_ok=True)

def ia_esta_rodando(nome):
    for proc in psutil.process_iter(attrs=['cmdline']):
        try:
            if nome.lower() in " ".join(proc.info['cmdline']).lower():
                return True
        except:
            continue
    return False

def atualizar_status(nome, ativa):
    status = {
        "nome": nome,
        "status": "🟢 Ativa" if ativa else "🔴 Inativa",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S") if ativa else "-"
    }
    with open(os.path.join(STATUS_DIR, f"{nome}.status"), "w") as f:
        json.dump(status, f, indent=4)

if __name__ == "__main__":
    while True:
        for nome in IA_NOMES:
            ativa = ia_esta_rodando(nome)
            atualizar_status(nome, ativa)
        time.sleep(5)
