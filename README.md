# Web Scraping de Notícias com Selenium

Este projeto é um exemplo de web scraping utilizando o framework Selenium em Python. O objetivo é coletar notícias relacionadas ao personagem "Deadpool" do site https://www.omelete.com.br/, salvar os títulos e datas de publicação em um arquivo de texto.

## Requisitos

- Python 3.7 ou superior
- ChromeDriver (compatível com sua versão do Google Chrome)

## Instalação

1. **Clone o repositório:**

    ```bash
    git clone git@github.com:mayukuni/teste-tecnico-revio.git
    cd teste-tecnico-revio
    ```

2. **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use: venv\Scripts\activate
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Baixe o ChromeDriver:**

    - Faça o download do ChromeDriver https://sites.google.com/a/chromium.org/chromedriver/.

## Uso

1. **Execute o script:**

    ```bash
    python script.py
    ```

2. **O script fará o seguinte:**

    - Abre o site https://www.omelete.com.br/.
    - Clica no ícone de busca e insere o termo "deadpool".
    - Coleta os títulos e datas das notícias relacionadas ao termo.
    - Salva os dados em um arquivo chamado `noticias_deadpool.txt` no formato JSON.

3. **Verifique o arquivo `noticias_deadpool.txt` para ver os dados coletados.**
