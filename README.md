# musestore

## prerequisitos pra rodar:
- Python (3.7 ou +)
- postgres

## Observações
É interessante utilizar o virtualenv para separar dependencias de desenvolvimento, também é interessante criar um super usuário para acessar o painel admin e começar a bricadeira :D

rode os comandos na raiz do projeto para iniciar o virtualenv:
```bash
$ pip install virtualenv
$ python -m virtualenv venv
```
#### caso esteja no linux:
```bash
$ source venv/bin/activate
```
#### caso esteja no windows:
```bash
$ venv\Scripts\activate
```
comandos pra rodar:
```bash
$ cp musestore/.env.example musestore/.env
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```
#### para criar o superuser:
```bash
$ python manage.py createsuperuser
```
_Obs: acesse localhost:8000/admin/ para acessar o painel admin e localhost:8000/swagger/ para acessar a documentação_
