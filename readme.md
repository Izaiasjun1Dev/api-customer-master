# Boas praticas de desenvovilmento de apis
## Tecnologias ultilizada para prover a api-customer
* Python
* Django Rest Framework
* Django
* Django Filters
* Validate docbr
* Sqlite3
# Para executar o projeto
corra o seguinte comando no seu cmd/propt de comando
### 1 - ```git clone https://github.com/Izaiasjun1Dev/api-customer-master.git```
### 2 - ```cd api-customer-master```
### 3 - ```python manage.py migrate```
### 4 - ```python manage.py createsuperuser``` 
neste passo serão feitas algumas perguntas atraves do seu prompt de comando para efetivamente criar um super user !
### 3 - ```python manage.py runserver```

e voilà apalicação estara rodando!

# Após a configuração!

se for do seu interesse poderá popular a sua base de dados com o comando python populate.py desde que esteja na pasta raiz do projeto!

-- voçe terá disponivel em seu navegador as seguintes rotas

esta rota dara acesso a toda a parte administrativa do sistema
* http://localhost:8000/admin   

esta rota dara acesso a pagina inicial da api
* http://localhost:8000/    

aqui tera acesso e controle ao endpoint de clientes
* http://127.0.0.1:8000/clientes/
  