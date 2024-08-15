#módulo para listas:

lista_operacoes = [] #armazena operações digitadas pelo teclado
resultados = [] #armazena resultados de combinações de elementos booleandos
expressoes = [] #armazena o resultado das expressões
atri = { 
    'a' : [True, False],
    'b' : [True, False],
    '~a': [not valor for valor in ['a']],
    '~b': [not valor for valor in ['b']]
}
#obs: os valores  para ~a e ~b não estão entrando para a função "atribuicao()" devido á problemas na indexação