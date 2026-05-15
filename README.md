# API Flask SQL

API simples em Flask para gerenciar livros com CRUD completo e banco de dados PostgreSQL.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

## Descrição

Este projeto expõe uma API REST para gerenciar livros com os seguintes recursos:

- `POST /books` — criar um livro
- `GET /books` — listar todos os livros
- `GET /books/<id>` — buscar um livro por ID
- `PUT /books/<id>` — atualizar um livro
- `DELETE /books/<id>` — remover um livro

O modelo `Book` contém os campos:

- `id` (UUID)
- `title`
- `author`
- `description`
- `isFavorite`
- `isReading`
- `isFinished`

## Tecnologias

- Python
- Flask
- Flask SQLAlchemy
- Flask-Migrate
- PostgreSQL
- Docker Compose

## Configuração local

### 1. Subir o banco PostgreSQL

Use o `docker-compose.yml` do projeto para subir o banco:

```bash
docker compose up -d
```

O serviço PostgreSQL estará disponível em `localhost:5432` com as credenciais:

- usuário: `postgres`
- senha: `postgres`
- banco: `book`

### 2. Criar e ativar ambiente virtual

No diretório do projeto:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências

Instale as dependências necessárias:

```bash
pip install flask flask_sqlalchemy flask_migrate psycopg2-binary
```

### 4. Executar migrações

A aplicação já utiliza `Flask-Migrate`. Para criar as tabelas no banco, rode:

```bash
export FLASK_APP=app.py
flask db init         # se ainda não existir migrations/
flask db migrate -m "init"
flask db upgrade
```

> Observação: se a pasta `migrations/` já existir, pule o `flask db init`.

### 5. Rodar a aplicação

```bash
python app.py
```

A aplicação será iniciada em `http://0.0.0.0:8080`.

## Endpoints

### Criar livro

`POST /books`

Body JSON:

```json
{
  "title": "Nome do livro",
  "author": "Autor",
  "description": "Descrição do livro"
}
```

### Listar livros

`GET /books`

### Buscar livro por ID

`GET /books/<id>`

### Atualizar livro

`PUT /books/<id>`

Body JSON (qualquer campo opcional):

```json
{
  "title": "Novo título",
  "author": "Novo autor",
  "description": "Nova descrição",
  "isFavorite": true,
  "isReading": false,
  "isFinished": true
}
```

### Excluir livro

`DELETE /books/<id>`

## Observações

- O `app.py` está configurado para usar `postgresql://postgres:postgres@localhost:5432/book`.
- Se você rodar o PostgreSQL via Docker Compose, essa configuração funciona porque o container expõe a porta `5432` no host.
- Caso altere host/porta/usuário, atualize `app.config['SQLALCHEMY_DATABASE_URI']` no `app.py`.

## Estrutura do projeto

- `app.py` — aplicação Flask e endpoints
- `db.py` — instância do SQLAlchemy
- `models/book.py` — modelo `Book`
- `docker-compose.yml` — serviço PostgreSQL
- `migrations/` — arquivos de migração do banco de dados
