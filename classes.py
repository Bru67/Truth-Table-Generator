from listas import *

class TabelaVerdade:
    def __init__(self, a, b, operador): #Definição inicial da classe
        self.a = a
        self.b = b
        self.operador = operador

    def atribuicao(self):
        for i in range(len(atri['a'])): #Criará uma Tupla armazenando os resultados na lista 'resultados'
            self.a = atri['a'][i]
            for c in range(len(atri['b'])):
                self.b = atri['b'][c]
                resultados.append((self.a, self.b))
        return resultados

    #Funções relacionadas aos operadores lógicos:
    def and_func(self):
        return self.a and self.b    

    def or_func(self):
        return self.a or self.b

    def seEntao(self):
        return not self.a or self.b  #implicação lógica para Se Então

    def seEsomenteSe(self):
        return True if self.a == self.b else False
    #ele retorna True se e somente se P for igual ao valor de Q e vise-versa

    def not_func(self):
        return not self.a, not self.b
    # ele transforma ambos valores de A e B em negativos, apresentando os dois resultados

class Principal(TabelaVerdade):
    def __init__ (self, expressaoDigitada):
        self.expressaoDigitada= expressaoDigitada
        super().__init__(None, None, None)
        self.a = None
        self.operador = None
        self.b = None 

    def processa_expressao(self):
        self.expressaoDigitada = input('\n\tInsira uma operação lógica para ser calculado a tabela verdade: \n'
                                       '\t(Obs: Utilize espaços para separar as variáveis)\n\t')
        sem_espacos = self.expressaoDigitada.strip() 
        #strip() retira os espaços do início e do fim da string (por motivos estéticos da tabela final), n interefere na construção da operação
        expressao_minuscula = sem_espacos.lower()
        #lower() torna tudo o que o usuário digitar minúculo para ñ comprometer os comandos da classe pai
        partes_expressao = expressao_minuscula.split()
        #split() separa em partes a string a partir dos espaços digitados pelo usuário
        lista_operacoes.append([expressao_minuscula])

        self.a = partes_expressao[0]  #substring correspondente a 'a'
        self.operador = partes_expressao[1]  #substring correspondente ao 'operador'
        self.b = partes_expressao[2]  #substring correspondente a 'b'
        lista_operacoes.insert(0, [self.a]) 
        lista_operacoes.insert(1, [self.b])

        return self.a, self.operador, self.b

    def value_input(self): #Realizando a operação lógica do input
        for resultado in resultados:
            self.a = resultado[0]
            self.b = resultado[1]
            if self.operador == '^':
                expressoes.append(self.and_func())
            elif self.operador == 'v':
                expressoes.append(self.or_func())
            elif self.operador == '->':
                expressoes.append(self.seEntao())
            elif self.operador == '<->':
                expressoes.append(self.seEsomenteSe())
            elif self.operador == '~':
                expressoes.append(self.not_func())
               
            else:
                expressoes.append("Erro")
        return expressoes
    
    def imprimir(self):
        
        print('\t ____________________________')
        print(f'\t| {lista_operacoes[0]} | {lista_operacoes[1]} | {lista_operacoes[2]}  ')
        print('\t|-------|-------|------------|')
        for resultado, expressao in zip(resultados, expressoes):
            print(f'\t| {resultado[0]:^5} | {resultado[1]:^5} | {expressao:^10} |')
        print('\t|_______|_______|____________|')