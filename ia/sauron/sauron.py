import time
import random

class IA_Sauron:
    def __init__(self):
        self.erros_consecutivos = 0
        self.max_erro = 3

    def pensar(self):
        print("[IA_Sauron] Pensando com inteligência adaptativa")
        while True:
            if self.simular_acao() == "erro":
                self.erros_consecutivos += 1
                print(f"[IA_Sauron] ❌ Erro #{self.erros_consecutivos}")
                if self.erros_consecutivos >= self.max_erro:
                    if not self.resolver():
                        self.solicitar_guardia()
            else:
                self.erros_consecutivos = 0
                print("[IA_Sauron] ✅ Ação bem sucedida")
            time.sleep(5)

    def simular_acao(self):
        return "erro" if random.random() < 0.3 else "sucesso"

    def resolver(self):
        print("[IA_Sauron] Tentando estratégias alternativas...")
        for i in range(5):
            time.sleep(1)
            if random.random() > 0.5:
                print(f"[IA_Sauron] Estratégia #{i+1} funcionou!")
                self.erros_consecutivos = 0
                return True
        print("[IA_Sauron] Nenhuma estratégia resolveu.")
        return False

    def solicitar_guardia(self):
        print("[IA_Sauron] Chamando Guardiã...")
