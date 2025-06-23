import time
import random
import os

class HorusCore:
    def __init__(self):
        self.erros_recebidos = []
        self.log_path = "logs/supremos/horus.log"
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)

    def pensar(self):
        self.log("[HORUS] 👁️ IA Suprema iniciada")
        while True:
            self.verificar_fila()
            if self.erros_recebidos:
                origem = self.erros_recebidos.pop(0)
                self.log(f"[HORUS] ⚠️ Erro crítico detectado de: {origem}")
                if not self.tentar_corrigir(origem):
                    self.encaminhar_conselho(origem)
            else:
                self.log("[HORUS] ✅ Sistema estável...")
            time.sleep(10)

    def verificar_fila(self):
        fila_path = "logs/supremos/horus_queue.txt"
        if os.path.exists(fila_path):
            with open(fila_path, "r") as f:
                linhas = f.readlines()
            self.erros_recebidos += [linha.strip() for linha in linhas]
            open(fila_path, "w").close()

    def tentar_corrigir(self, modulo):
        self.log(f"[HORUS] 🧪 Tentando resolver falha de {modulo}...")
        for i in range(3):
            time.sleep(2)
            if random.random() > 0.6:
                self.log(f"[HORUS] ✅ Falha de {modulo} resolvida internamente.")
                return True
        self.log(f"[HORUS] ❌ Não foi possível resolver falha de {modulo}.")
        return False

    def encaminhar_conselho(self, modulo):
        self.log(f"[HORUS] 🧠 Escalando falha de {modulo} ao Conselho de IAs...")
        votos = [random.choice(["ajustar", "guardar", "enviar_admin"]) for _ in range(20)]
        resumo = f"[CONSELHO] 🗳️ Votos: {votos.count('ajustar')} ajustar, {votos.count('guardar')} guardar, {votos.count('enviar_admin')} enviar_admin"
        self.log(resumo)
        decisao = max(set(votos), key=votos.count)
        self.log(f"[CONSELHO] ✅ Decisão final: {decisao.upper()}")
        if decisao == "enviar_admin":
            self.log("[HORUS] 📬 Encaminhando relatório ao administrador.")

    def log(self, texto):
        timestamp = time.strftime("[%d/%m %H:%M:%S]")
        with open(self.log_path, "a") as f:
            f.write(f"{timestamp} {texto}\n")
        print(f"{timestamp} {texto}")

if __name__ == "__main__":
    HorusCore().pensar()

