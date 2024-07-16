Flask Video Downloader
Este é um aplicativo web simples desenvolvido com Flask para baixar vídeos do YouTube.

Funcionalidades
Download de Vídeos: Permite ao usuário inserir um URL do YouTube e escolher a qualidade para baixar o vídeo.
Formatos de Download: Suporta download de vídeo em várias qualidades e também permite baixar apenas o áudio em formato MP3.
Interface Simples: Utiliza HTML, CSS e JavaScript para criar uma interface amigável.
Pré-requisitos
Python 3.7 ou superior
Flask
youtube-dl
Instalação
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/flask-video-downloader.git
cd flask-video-downloader
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Uso
Inicie o servidor Flask:

bash
Copiar código
python app.py
Abra seu navegador e acesse http://localhost:5000.

Cole o URL do vídeo do YouTube na caixa de entrada e escolha a qualidade desejada.

Clique em "Baixar" para iniciar o download.

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
├── requirements.txt
└── README.md






static/: Contém arquivos estáticos como CSS.
templates/: Contém templates HTML para renderizar as páginas.
app.py: O arquivo principal que define a aplicação Flask e suas rotas.
requirements.txt: Lista de dependências Python.
Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests para melhorias ou correções de bugs.

Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
