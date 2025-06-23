import random

class VotanteBase:
    def __init__(self, nome):
        self.nome = nome

    def votar(self, modulo_afetado):
        opcoes = ["ajustar", "guardar", "enviar_admin"]
        voto = random.choice(opcoes)
        print(f"[{self.nome}] Votou por: {voto.upper()} para {modulo_afetado}")
        return voto

def convocar_conselho(modulo):
    print(f"\n[CONSELHO] 🧠 Iniciando votação sobre: {modulo}")
    votos = []
    for i in range(1, 21):
        membro = VotanteBase(f"IA_Conselheira_{i}")
        voto = membro.votar(modulo)
        votos.append(voto)

    return votos

# Exemplo:
if __name__ == "__main__":
    resultado = convocar_conselho("IA_RA")
    print("\n[RESUMO] Votos:", resultado)
