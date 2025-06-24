import threading
import subprocess
import time
import os
from utils.sync_contas import sincronizar_contas

def iniciar_ia(nome, path):
    def run():
        print(f"🚀 Iniciando {nome}")
        while True:
            try:
                subprocess.run(["python", path])
            except Exception as e:
                print(f"⚠️ {nome} caiu: {e}")
            time.sleep(5)
    return run

if __name__ == "__main__":
    # 🔁 Sincronizar contas criadas manualmente para fila real
    sincronizar_contas()

    threads = [
        threading.Thread(target=iniciar_ia("IA_RA", "ia/ra/ra.py")),
        threading.Thread(target=iniciar_ia("IA_Isis", "ia/isis/isis.py")),
        threading.Thread(target=iniciar_ia("IA_Sauron", "ia/sauron/sauron.py")),
        threading.Thread(target=iniciar_ia("IA_Tempo", "ia/tempo/tempo.py")),
        threading.Thread(target=iniciar_ia("HORUS", "horus_core.py")),
        threading.Thread(target=iniciar_ia("Watchdog", "watchdog.py")),
        threading.Thread(target=iniciar_ia("Painel", "painel_web/app.py")),
    ]

    for t in threads:
        t.daemon = True
        t.start()

    print("✅ Sistema Anubis Eye iniciado. Pressione Ctrl+C para parar.")
    while True:
        time.sleep(60)
