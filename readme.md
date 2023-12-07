# Ponderada Semana 7

Essa API feita em python tem o objetivo de manejar duas entidades: Usuários e Histórias, além de, por meio de uma integração com chatgpt, inserir novos trechos as histórias já criadas.

## Como rodar o projeto?

O projeto foi desenvolvido para rodar por meio do Docker. Sendo assim, com docker e docker-compose instalados em sua máquina, na raíz do projeto, execute o comando:

```
docker-compose up --build -d
```

Dessa forma todas as tecnologias e libs necessárias serão instaladas e configuradas.

Além disso, é necessário criar um arquivo .env na raíz do projeto com a **API_KEY** de sua API do chatgpt, seguindo o padrão:

```
API_KEY_GPT="sua-api-key-aqui!"
```

Vale ressaltar que o processo citado criará um banco de dados MYSQL definido com as credenciais escritas no código. Caso necessário, mude as variáveis no arquivo **mysql_config.py** para contectar-se com outro banco de dados. O script de criação das tabelas está na pasta **mysql-init** na raíz desse repositório.

## Tecnologias utilizadas

A API foi desenvolvida em Python, conectando-se a um banco de dados MYSQL sendo criado por intermédio do docker e docker-compose. Além dessas principais tecnologias, uma série de bibliotecas foram utilizadas, estando listadas no arquivo **requirements.txt**

## Arquitetura Utlizada

Para a criação da API, foi utilizada uma arquitetura de Entidades com DAOs onde as regras de negócio estão nas entidades e a persistência dos dados e comunicação com BD nas DAOs.

## Testes

Para rodar os testes, execute o comando:
```
pytest
```

Foram utilizados duas categorias de testes:

### Testes de integração

Foram feitos dois testes de integração, consumindo a rota de listagem das entidades Usuário e History validando se não houveram problemas com a integração com banco de dados.

### Testes Unitários

Como as lógicas de negócios estão nas entidades com a lógica de persistência imbutida, **não há como realizar testes unitários** na maior parte das funcionalidades da aplicação (pois dependem de sistemas externos). Ainda sim, testes unitários foram criados para funcionalidades essenciais em todas as rotas, como a criação de instâncias das classes User e History e o hasheamento de senhas.


## Referência de API

Para encontrar a referêcia de API desse projeto, rode-o e acesse o endpoint http://localhost:8000/docs

## Autenticação

Para a autenticação, há uma rota de login no projeto que deve receber nickname e senha. As senhas serão guardas no banco de dados hasheadas em **sha256** com um salt, impedindo que senhas iguais produzam hashs iguais e garantindo a segurança das senhas. 

Dessa forma, a comunicação entre o client e API quanto a autenticação deve ser feita utilizando tokens JWT. Um token pode ser obtido pela rota de login de usuário e para testes, a rota de listagem de histórias solicita esse token no header **Authorization** no seguinte padrão: **Bearer {token}**, retornando apenas as histórias relacionadas a aquele usuário.

## ChatGPT

A integração do chatgpt está na rota **histories/{id}/add-part** e deve ser usada passando um body no seguinte formato:
```
{
    {
	    "part": "Texto aqui"
    }
}
```

Essa rota utilizará todas as informações prévias da história e com o auxílio do chatgpt, encaixará o trexo passado no melhor lugar da história já criada, realizando as adaptações necessárias para tal.