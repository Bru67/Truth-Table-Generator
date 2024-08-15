from listas import *
from classes import *

#aqui é onde as classes e funções são chamadas especificamente para desenvolver o ttg

principal = Principal(TabelaVerdade)
principal.processa_expressao()
principal.atribuicao()
principal.value_input()
principal.imprimir()
print('\tLegenda:\n\t 1 = True\n\t 0 = False\n')

# para ver o resultado das listas, descomente

# print(lista_operacoes)
# print(resultados)
# print(expressoes)