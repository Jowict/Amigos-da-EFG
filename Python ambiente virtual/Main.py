import json
from fastapi import FastAPI
from Pessoa import Pessoa
from pessoa_model import PessoaModelo

p1 = Pessoa(
    '1',
    'JoãoPeba',
    '11/12/1998',
    'Proplayer de Valorant',
    'Gamer',
    'Solteiro',
    'Masculino',
    )

p2 = Pessoa(
    '2',
    'Laricela',
    '20/10/2006',
    'Cientista de Dados Sênior',
    'Superior',
    'Muito que bem',
    'Feminino'
    )

p3 = Pessoa(
    '3',
    'Matheus',
    '12/05/1999',
    'VideoMaker',
    'Superior',
    'Casado',
    'Masculino'
    )

p4 =  Pessoa(
    '4',
    'César',
    '31/12/2003',
    'Motorista de aplicativo',
    'Superior',
    'Casado',
    'Masculino'
    )


lista_pessoas = [
        p1,p2,p3,p4
    ]


app = FastAPI()#Variável classe FastAPI

#@ = Anotation, função que tem como parâmetro a função abaixo dela.
@app.get('/')
def minha_api():
    return 'Bem-vindo a minha API, para Usuários, acesse a rota /api/users'

@app.get('/api/users')
def users_api():
    return

@app.get('/api/v2/users')
def read_api():
    with open('user.json') as arquivos:
        return json.loads(arquivos.read())
    
@app.get('/api/users/{id_pessoa}')
def get_pessoa(id_pessoa):
    for pessoa in lista_pessoas:
        if pessoa.id == id_pessoa:
            return pessoa
        
    return lista_pessoas[1]

@app.get('/api/v2/users/{id_pessoa}')
def get_pessoa(id_pessoa):
    with open('user.json') as arquivos:
        pessoas = json.loads(arquivos.read())
    
    for pessoa in pessoas:
        if pessoa.id == id_pessoa:
            return pessoa
        
    return "Pessoa não encontrada"

@app.get('/api/users/{nome_pessoa}')
def get_pessoa(nome_pessoa: str):
    for pessoa in lista_pessoas:
        if pessoa.nome == nome_pessoa:
            return pessoa
        
    return lista_pessoas[1]

@app.post('/api/v3/users/')
def post_pessoa(pessoa: PessoaModelo):
    with open('user.json', encoding='utf-8') as arquivo:
        pessoas = list(json.loads(arquivo.read()))
    
    pessoa.id = pessoas[-1]['id'] + 1
    pessoas.append(pessoa.model_dump())
    
    with open('user.json', 'w', encoding='utf-8') as arquivo:
        arquivo.write(json.dumps(pessoas, indent=4))

    return f'Pessoa com nome {pessoa.nome} criada com sucesso'

@app.delete('/api/v3/users/{id}')
def delete_pessoa(id: int):
    with open('user.json', encoding='utf-8') as arquivo:
        pessoas = list(json.loads(arquivo.read()))

    for posicao in range(len(pessoas)):
        print(posicao)
        if pessoas[posicao]['id'] == id:
            pessoas.pop(posicao)

            with open('user.json', 'w', encoding='utf-8') as arquivo:
                arquivo.write(json.dumps(pessoas, indent=4))

            return 'pessoa foi de vala'

    return 'pessoa nao existe'

@app.patch ('/api/v3/users/{id}')
def update_pesoas(id: int):
    with open('user.json', encoding='utf-8') as arquivo:
        pessoas = list(json.loads(arquivo.read()))
