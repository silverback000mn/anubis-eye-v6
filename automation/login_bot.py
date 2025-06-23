from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def login_instagram(username, password):
    print("[LOGIN BOT] Iniciando login...")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.instagram.com/accounts/login/")

    time.sleep(5)

    try:
        user_input = driver.find_element(By.NAME, "username")
        pass_input = driver.find_element(By.NAME, "password")

        user_input.send_keys(username)
        pass_input.send_keys(password)

        time.sleep(2)

        pass_input.submit()
        print("[LOGIN BOT] Login enviado...")

        time.sleep(5)

        if "challenge" in driver.current_url or "login" in driver.current_url:
            print("[LOGIN BOT] ⚠️ Login falhou ou exigiu verificação.")
        else:
            print("[LOGIN BOT] ✅ Login bem-sucedido.")

    except Exception as e:
        print(f"[LOGIN BOT] ❌ Erro: {e}")

    driver.quit()

# Exemplo de uso:
if __name__ == "__main__":
    login_instagram("seu_usuario", "sua_senha")
