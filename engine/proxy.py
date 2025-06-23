import requests
import random

def buscar_proxies_gratuitos():
    print("[PROXY] 🔍 Buscando proxies gratuitos...")
    try:
        resposta = requests.get("https://www.proxy-list.download/api/v1/get?type=https")
        proxies = resposta.text.strip().split("\r\n")
        proxies = [p for p in proxies if ":" in p]
        print(f"[PROXY] ✅ {len(proxies)} proxies obtidos.")
        return proxies
    except Exception as e:
        print(f"[PROXY] ❌ Erro ao buscar proxies: {e}")
        return []

def escolher_proxy():
    proxies = buscar_proxies_gratuitos()
    if not proxies:
        print("[PROXY] ⚠️ Nenhum proxy disponível.")
        return None
    proxy = random.choice(proxies)
    print(f"[PROXY] 🌐 Proxy escolhido: {proxy}")
    return proxy

# Exemplo de uso:
if __name__ == "__main__":
    escolher_proxy()
