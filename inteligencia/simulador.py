import random
import time
from conselho.conselho import convocar_conselho

class SimuladorSistema:
    def __init__(self):
        self.modulos = ["IA_RA", "IA_Isis", "IA_Sauron", "IA_Tempo"]
        self.erros_detectados = 0

    def rodar_simulacoes(self, ciclos=10):
        print(f"[SIMULADOR] 🔁 Rodando {ciclos} ciclos de simulação...\n")
        for i in range(1, ciclos + 1):
            print(f"[CICLO {i}] Verificando módulos...\n")
            time.sleep(1)
            modulo_afetado = random.choice(self.modulos)
            erro = random.random() < 0.3  # 30% de chance de erro
            if erro:
                self.erros_detectados += 1
                print(f"[ERRO] ❌ Erro crítico detectado em {modulo_afetado}")
                votos = convocar_conselho(modulo_afetado)
                self.decidir(votos)
            else:
                print("[STATUS] ✅ Nenhum erro detectado.\n")
            time.sleep(1.5)

    def decidir(self, votos):
        decisao = max(set(votos), key=votos.count)
        print(f"\n[DECISÃO FINAL] 🧠 Conselho decidiu: {decisao.upper()}\n")
        print("─" * 50)

# Executar diretamente
if __name__ == "__main__":
    sim = SimuladorSistema()
    sim.rodar_simulacoes(ciclos=12)
