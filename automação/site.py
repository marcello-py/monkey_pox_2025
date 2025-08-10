# MANDAR AS PACIAIS DO SITE WINDY PARA O WHATSAPP
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Inicia o navegador
driver = webdriver.Firefox()
driver.maximize_window()

# Acessa o Bing
driver.get("https://www.bing.com")  # devido o Google ser muito sensível a automação, solicita captcha facilmente

# Localiza o campo de busca
campo_busca = driver.find_element(By.NAME, 'q')

sleep(10)

# Digita "windy"
campo_busca.send_keys("windy")

sleep(10)

# Pressiona Enter
campo_busca.send_keys(Keys.ENTER)

sleep(10)

# Localiza o primeiro resultado
primeiro_resultado = driver.find_element(By.XPATH, "(//h2/a)[1]")

# Localiza o caminho alternativo, pelo nome
resultado_nome = driver.find_element(By.XPATH, "//h2/a[text()='Windy: Wind map & weather forecast']")

sleep(10)

# Clica pelo nome
resultado_nome.click()

sleep(20)

campo_busca_windy = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.ID, "q"))
)

campo_busca_windy.send_keys("São Paulo")
campo_busca_windy.send_keys(Keys.ENTER)

sleep(400)
# Encerra o navegador
driver.quit()