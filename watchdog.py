import os
import subprocess
import time

def verificar_processos():
    processos = {
        "ia/ra/ra.py": False,
        "ia/isis/isis.py": False,
        "ia/sauron/sauron.py": False,
        "ia/tempo/tempo.py": False
    }

    while True:
        for path in processos:
            if not processos[path] or not processo_ativo(path):
                print(f"[WATCHDOG] Reiniciando {path}")
                processos[path] = subprocess.Popen(["python", path])
        time.sleep(30)

def processo_ativo(path):
    # Simula sempre falha para testar reinício
    return False

if __name__ == "__main__":
    print("[WATCHDOG] Ativo e monitorando IAs.")
    verificar_processos()
