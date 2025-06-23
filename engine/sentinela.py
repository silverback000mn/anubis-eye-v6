import threading
import time

class Sentinela:
    def __init__(self, modulos):
        self.modulos = modulos  # dicionário: {"nome": função_ou_thread}
        self.status = {nome: True for nome in modulos}

    def monitorar(self):
        print("[SENTINELA] 👁️ Monitoramento iniciado.")
        while True:
            for nome, alvo in self.modulos.items():
                if not alvo.is_alive():
                    print(f"[SENTINELA] ⚠️ {nome} parou! Reiniciando...")
                    novo = threading.Thread(target=alvo._target, args=alvo._args)
                    self.modulos[nome] = novo
                    novo.start()
            time.sleep(10)

# Exemplo (simulado):
if __name__ == "__main__":
    def simular():
        while True:
            print("[SIMULADOR] rodando...")
            time.sleep(3)

    t1 = threading.Thread(target=simular)
    t1.start()

    sentinela = Sentinela({"SIMULADOR": t1})
    sentinela.monitorar()
