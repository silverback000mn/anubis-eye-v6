import time
import random

class MetaManager:
    def __init__(self):
        self.meta_dia = 2000
        self.contas_criadas = 0

    def pensar(self):
        print("[MetaManager] 📊 Iniciando controle de metas...")
        while True:
            self.contas_criadas += random.randint(10, 50)
            falta = self.meta_dia - self.contas_criadas
            if falta <= 0:
                print("[MetaManager] ✅ Meta atingida.")
                self.contas_criadas = 0
            else:
                print(f"[MetaManager] ⏳ Faltam {falta} contas para meta diária.")
            time.sleep(30)

if __name__ == "__main__":
    MetaManager().pensar()
