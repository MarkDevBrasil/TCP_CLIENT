TCP Client

Um cliente TCP simples desenvolvido em Python para praticar programação de sockets, comunicação em rede e alguns conceitos que fazem parte do dia a dia de quem estuda pentest e segurança da informação.

A ideia do projeto foi colocar em prática conceitos de Python em vez de apenas estudá-los na teoria.

Sobre

O cliente permite informar um IP e uma porta, estabelecer uma conexão TCP com um servidor e trocar dados através do socket.

Atualmente, o fluxo é bem simples:

Cliente
   │
   │  TCP Connection
   ▼
Servidor
   │
   │  Dados
   ▼
Cliente

Funcionalidades
Conexão TCP utilizando socket
Entrada de IP e porta pelo terminal
Envio de dados para o servidor
Recebimento de dados
Timeout na conexão
Tratamento básico de erros
Requisitos
Python 3.x

Nenhuma biblioteca externa é necessária.

Uso

Execute o arquivo:

python client.py


Depois informe o endereço e a porta do servidor:

Digite o IP: 127.0.0.1
Digite a porta para se conectar: 8080


O servidor precisa estar previamente configurado para aceitar conexões nessa porta.

O que estou praticando

Com esse projeto estou trabalhando principalmente:

Python
socket
TCP/IP
Comunicação cliente-servidor
IPs e portas
Tratamento de exceções
Timeouts
Conceitos básicos de redes

Esses conhecimentos também servem como base para projetos maiores voltados a segurança ofensiva e pentest.
Este projeto foi feito para testar e aperfeiçoar meus conhecimentos em Python e redes, utilizando ambientes próprios ou autorizados para os testes.

Python + Networking + Pentest 🔌🐍
