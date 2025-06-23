import random

def gerar_bio():
    emojis = ["🌍", "💡", "📸", "🎯", "🧠", "🚀", "💼", "🏞️", "🕊️", "🎧", "📝", "🔮"]
    profissoes = ["Designer", "Engenheiro", "Psicólogo", "Artista", "Fotógrafo", "Empreendedor", "Estudante", "Cientista", "Professor", "Dev"]
    frases = [
        "Explorando o mundo um clique por vez",
        "Apaixonado por ideias que mudam tudo",
        "Vivendo no agora com olhos no futuro",
        "Transformando café em código",
        "Criando com propósito e amor",
        "Respirando arte e inovação",
        "Entre mapas mentais e projetos reais",
        "Fazendo da vida uma obra em progresso",
        "Apenas sendo... eu mesmo",
        "Comunicando com silêncios e cores"
    ]

    bio = f"{random.choice(emojis)} {random.choice(profissoes)} | {random.choice(frases)}"
    return bio

# Exemplo:
if __name__ == "__main__":
    for _ in range(5):
        print(gerar_bio())
