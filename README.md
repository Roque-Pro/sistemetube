Descrição
Este projeto é uma aplicação web para download de vídeos do YouTube com opções de qualidade selecionáveis.

Estrutura do Projeto
arduino
Copiar código



meu_projeto/
│
├── static/
│   ├── style.css
│
├── templates/
│   ├── index.html
│   ├── success.html
│
├── app.py



Pré-requisitos
Python 3.x instalado
Flask framework instalado (pip install Flask)
Biblioteca youtube_dl instalada (pip install youtube_dl)
Como Executar
Clone o repositório para sua máquina local.
Navegue até o diretório do projeto.
Execute o seguinte comando para iniciar o servidor Flask:
Copiar código
python app.py
Abra um navegador web e vá para http://localhost:5000.
Como Utilizar
Na página inicial, cole o link do vídeo do YouTube desejado.
Selecione a qualidade de vídeo desejada utilizando os checkboxes fornecidos.
Clique no botão "Baixar".
Após o download, você será redirecionado para a página de sucesso onde poderá ver uma mensagem indicando que o vídeo foi baixado com sucesso.
Notas Adicionais
Este projeto utiliza Flask para o backend e HTML/CSS para o frontend básico.
Certifique-se de ter uma conexão com a internet estável ao baixar vídeos do YouTube.
Este projeto não deve ser usado para baixar conteúdo protegido por direitos autorais sem permissão.
