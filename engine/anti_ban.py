import random

class AntiBan:
    def __init__(self):
        self.acoes_feitas = 0
        self.alertas = 0
        self.limite_alerta = 3

    def registrar_acao(self):
        self.acoes_feitas += 1
        print(f"[ANTI-BAN] 👣 Ação #{self.acoes_feitas} registrada.")
        if self.acoes_feitas % 10 == 0:
            self.checar_sinais()

    def checar_sinais(self):
        risco = random.choice(["baixo", "médio", "alto"])
        print(f"[ANTI-BAN] 🚨 Verificando sinais de detecção: RISCO {risco.upper()}")

        if risco == "alto":
            self.alertas += 1
            print(f"[ANTI-BAN] ⚠️ Alerta {self.alertas}/{self.limite_alerta}")
            if self.alertas >= self.limite_alerta:
                print("[ANTI-BAN] ❌ Limite de alertas atingido. PAUSANDO atividades.")
                return False
        return True

# Exemplo de uso:
if __name__ == "__main__":
    ab = AntiBan()
    for _ in range(30):
        ab.registrar_acao()
