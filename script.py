import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# inicia uma instância do Chrome WebDriver
service = Service()

# define a preferência para o navegador Chrome
options = webdriver.ChromeOptions()

# inicia o navegador Chrome
driver = webdriver.Chrome(service=service, options=options)

# abre a página de busca
driver.get("https://www.omelete.com.br/")

# clica no ícone de busca
search = WebDriverWait(driver, 10).until(
  EC.element_to_be_clickable((By.TAG_NAME, 'i'))
)
search.click()

# insere "deadpool" no campo de busca e envia
search_box = WebDriverWait(driver, 10).until(
  EC.visibility_of_element_located((By.NAME, 'q'))
)
search_box.send_keys('deadpool')
search_box.submit()

# função para coletar os títulos e datas das notícias
def get_news_info(driver):
  news_list = []
  try:
    news = WebDriverWait(driver, 10).until(
      EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.mark'))
    )
    for new in news:
      try:
        title_element = new.find_element(By.CSS_SELECTOR, '.mark__title h2')
        date_element = new.find_element(By.CSS_SELECTOR, '.mark__time')
        title = title_element.text.strip()
        date = date_element.text.strip()
        # adiciona o título e a data à lista de notícias
        news_list.append({
          'titulo': title,
          'data': date
        })
      except Exception as e:
        print(f"Erro ao coletar título ou data: {e}")
  except Exception as e:
    print(f"Erro ao coletar informações: {e}")
  return news_list

all_news = []

# rola até o final da página
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# coleta informações ao rolar até o final
all_news.extend(get_news_info(driver))

scroll_height = 300 
current_position = driver.execute_script("return window.pageYOffset;")
previous_height = driver.execute_script("return document.body.scrollHeight")
max_scroll_attempts = 5
scroll_attempts = 0

# rola gradualmente para cima até o limite de tentativas
while scroll_attempts < max_scroll_attempts:
  new_position = current_position - scroll_height
  driver.execute_script(f"window.scrollTo(0, {new_position});")
  time.sleep(2)

  # coleta informações enquanto rola para cima
  all_news.extend(get_news_info(driver))

  # verifica se existe um botão
  try:
    load_more_button = driver.find_element(By.CSS_SELECTOR, '#loadMore')
    if load_more_button.is_displayed():
      print("botão encontrado.")
      # clica no botão
      load_more_button.click()
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(3) 
      current_position = driver.execute_script("return window.pageYOffset;")
      previous_height = driver.execute_script("return document.body.scrollHeight")
      scroll_attempts = 0
      # reinicia o loop após clicar no botão
      continue  
  except Exception as e:
    pass

  # verifica se o height aumentou
  new_height = driver.execute_script("return document.body.scrollHeight")
  if new_height > previous_height:
    print("altura aumentou")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    current_position = driver.execute_script("return window.pageYOffset;")
    previous_height = new_height
    # reinicia o loop se a altura da página aumentou
    continue

  # atualiza a posição atual
  current_position = new_position  
  scroll_attempts += 1

driver.quit()

# salva os dados em um arquivo .txt
with open('noticias_deadpool.txt', 'w', encoding='utf-8') as file:
  for news_item in all_news:
    file.write(json.dumps(news_item, ensure_ascii=False) + '\n')

print("raspagem concluída")

# média de tempo de execução: 50 minutos