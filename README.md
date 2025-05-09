# Evoluum Tasks

O **Evoluum Tasks** é o sistema responsável pelo cadastro de tarefas de usuários.

### Requisitos 🗒️

- Python 3.10.12. A sugestão é usar o [pyenv](https://github.com/pyenv/pyenv) para instalar o interpretador Python com mais facilidade na versão desejada.
- Instalação de bibliotecas.
- Arquivo .env criado na raiz do diretório com as variáveis de ambiente.

---

### Arquitetura e Stack 🛠️

A arquitetura utilizada é baseada na Clean Architecture, em que a camada de banco de dados e APIs são isolados das regras de negócios. 
Principais frameworks e bibliotecas:

- FastAPI
- Pydantic
- SQLAlchemy

---

### Execução do código ⚙️

Recomenda-se criar um virtualenv para isolar as dependências da aplicação. Com o ambiente virtual criado e ativado, rode o comando a seguir

```jsx
pip install -r requirements.txt
```

---


### Principais comandos 💻

Para rodar localmente a aplicação no localhost:8000:

```jsx
python main.py
```

Em http://localhost:8000/docs é possível verificar a documentação dos endpoints existentes.

Para realizar a criação das tabelas no banco de dados:

```jsx
python create_tables.py
```


---


### Endpoints integrados com FlutterFlow 🔄

**POST /users/signup**

Request Body
```jsx
{
  "email": "user@example.com",
  "name": "string",
  "last_name": "string",
  "password": "string"
}
```

Resposta com Sucesso

```jsx
{
  "id": 0,
  "email": "user@example.com",
  "name": "string",
  "last_name": "string"
}
```

---


**POST /users/login**

Request body em Form-data
```jsx
"username": "user@example.com"
"password": "string"
```

Resposta com Sucesso

```jsx
{
  "id": 0,
  "email": "user@example.com",
  "name": "string",
  "last_name": "string",
  "access_token": "string",
  "token_type": "string"
}
```
