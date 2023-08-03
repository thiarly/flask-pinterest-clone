# Flask Pinterest Clone

Você pode acessar o projeto pelo link: [Flask Pinterest Clone](https://flask-pinterest-clone-production.up.railway.app/?next=%2Fperfil%2F2).

## Descrição

Este é um clone do Pinterest, construído usando Flask, que permite aos usuários compartilhar imagens e interagir com o conteúdo de outros usuários. O projeto está hospedado no [Railway](https://railway.app/).

O projeto implementa as seguintes funcionalidades:

- Criação de conta e autenticação de usuário.
- Funcionalidades de perfil do usuário.
- Upload de fotos.
- Exibição de feed com as fotos postadas.

As rotas implementadas são as seguintes:

- Homepage (`/`): exibe a página inicial e lida com a autenticação do usuário.
- Criar conta (`/criar-conta`): permite que novos usuários criem uma conta.
- Perfil (`/perfil/<id_usuario>`): exibe o perfil de um usuário e permite o upload de fotos se o perfil pertencer ao usuário autenticado.
- Logout (`/logout`): termina a sessão do usuário atual.
- Feed (`/feed`): exibe todas as fotos postadas, na ordem da mais recente para a mais antiga.

## Instalação

As seguintes bibliotecas são necessárias para executar o projeto:

```bash
bcrypt==4.0.1
blinker==1.6.2
click==8.1.6
dnspython==2.4.1
email-validator==2.0.0.post2
Flask==2.3.2
Flask-Bcrypt==1.0.1
Flask-Login==0.6.2
Flask-SQLAlchemy==3.0.5
Flask-WTF==1.1.1
greenlet==2.0.2
gunicorn==21.2.0
idna==3.4
importlib-metadata==6.8.0
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
packaging==23.1
psycopg2==2.9.6
SQLAlchemy==2.0.19
typing_extensions==4.7.1
Werkzeug==2.3.6
WTForms==3.0.1
zipp==3.16.2


Você pode instalar essas bibliotecas com o seguinte comando:

bash
Copy code
pip install -r requirements.txt
Uso

Após a instalação das dependências, você pode iniciar o aplicativo localmente com o seguinte comando:

bash
Copy code
flask run
Em seguida, você pode acessar o aplicativo em seu navegador no endereço http://localhost:5000.

Contribuição

Se você deseja contribuir para este projeto, fique à vontade para fazer um fork e enviar um pull request.

Licença

Este projeto está licenciado sob a licença MIT.
