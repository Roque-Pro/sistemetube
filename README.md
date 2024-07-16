Descrição<br/>
Este projeto é uma aplicação web para download de vídeos do YouTube com opções de qualidade selecionáveis.<br/>

Estrutura do Projeto<br/>
arduino<br/>
Copiar código<br/>



meu_projeto/ <br/>
│<br/>
├── static/<br/>
│   ├── style.css<br/>
│<br/>
├── templates/<br/>
│   ├── index.html<br/>
│   ├── success.html<br/>
│<br/>
├── app.py<br/>



Pré-requisitos<br/>
Python 3.x instalado<br/>
Flask framework instalado (pip install Flask)<br/>
Biblioteca youtube_dl instalada (pip install youtube_dl)<br/>
Como Executar<br/>
Clone o repositório para sua máquina local.<br/>
Navegue até o diretório do projeto.<br/>
Execute o seguinte comando para iniciar o servidor Flask:<br/>
Copiar código<br/>
python app.py<br/>
Abra um navegador web e vá para http://localhost:5000.<br/>
Como Utilizar<br/>
Na página inicial, cole o link do vídeo do YouTube desejado.<br/>
Selecione a qualidade de vídeo desejada utilizando os checkboxes fornecidos.<br/>
Clique no botão "Baixar".<br/>
Após o download, você será redirecionado para a página de sucesso onde poderá ver uma mensagem indicando que o vídeo foi baixado com sucesso.<br/>
Notas Adicionais<br/>
Este projeto utiliza Flask para o backend e HTML/CSS para o frontend básico.<br/>
Certifique-se de ter uma conexão com a internet estável ao baixar vídeos do YouTube.<br/>
Este projeto não deve ser usado para baixar conteúdo protegido por direitos autorais sem permissão.<br/>
