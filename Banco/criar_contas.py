# Importando a classe conta_bancaria
from classes import conta_bancaria

# Dicionário para armazenar as contas, usando o nome como chave
contas = {
    "Ana": conta_bancaria("Ana", 10), 
    "Kaue": conta_bancaria("Kaue", 20)
}

def criar_conta(nome, saldo_inicial=0):
    if nome in contas:
        return "Essa conta já existe, tente novamente."
    
    # Criando e armazenando a conta no dicionário
    contas[nome] = conta_bancaria(nome, saldo_inicial)
    return "Conta criada com sucesso!"
