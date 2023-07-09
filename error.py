class ErrorVariableNotDeclared(Exception):
    def __init__(self, line, id):
        message = 'Line {}: ID not declared: {}'.format(line, id)
        super().__init__(message)

class ErrorDeclarationAlreadyMade(Exception):
    def __init__(self, line, id):
        message = 'Line {}: ID already declared: {}'.format(line, id)
        super().__init__(message)

class ErrorTypeNotReported(Exception):
    def __init__(self, line, id):
        message = 'Line {}: Type not reported: {}'.format(line, id)
        super().__init__(message)

class ErrorUnexpectedType(Exception):
    def __init__(self, line, expectedType, receivedType):
        message = 'Line {}: Expected type {} but {} was received'.format(line, expectedType, receivedType)
        super().__init__(message)

class ErroTipoIncompativelDecl(Exception):
    def __init__(self, line, type):
        mensagem = 'Linha {}: Esperado o tipo {} na declaração da constante'.format(line, type)
        super().__init__(mensagem)

class ErroBreak(Exception):
    def __init__(self, line):
        mensagem = 'Linha {}: Break fora do loop'.format(line)
        super().__init__(mensagem)

class ErrorTypeExpression(Exception):
    def __init__(self, line, operation, type1, type2=None):
        message = 'line {}: Operation {} not supported for the types: {} e {}'.format(line, operation, type1, type2) if type2 else 'Line {}: Operation {} not supported for the types: {}'.format(line, operation, type1)
        super().__init__(message)

class ErroTipoExpressaoDiferenteDeIncremento(Exception):
    def __init__(self, line):
        mensagem = 'Linha {}: Variaveis diferentes na declaracao do for e no incremento'.format(line)
        super().__init__(mensagem)

class ErroRetorno(Exception):
    def __init__(self, line):
        mensagem = 'Linha {}: Retorno fora do escopo da função'.format(line)
        super().__init__(mensagem)

class ErroTipoInesperado(Exception):
    def __init__(self, line, expected_type, received_type):
        mensagem = 'Linha {}: Esperado tipo {}, mas foi recebido {}'.format(line, expected_type, received_type)
        super().__init__(mensagem)

class ErroDuplaExpressao(Exception):
    def __init__(self, line):
        mensagem = 'Linha {}: Expressão possui mais comparadores do que atributos'.format(line)
        super().__init__(mensagem)

class ErroArgumentoEsperado(Exception):
    def __init__(self, line, expectedArgs, recivedArgs):
        mensagem = 'Linha {}: Esperado {} argumentos, mas somente foram recebidos {}'.format(line, expectedArgs, recivedArgs)
        super().__init__(mensagem)

class ErrorVariableNotFoundAtSymbolTable(Exception):
    def __init__(self, varName, scope):
        message = 'Variable {} not found in scope {}'.format(varName, 'LOCAL' if scope else 'GLOBAL')
        super().__init__(message)

class ErroDeclaracaoDepoisDoBloco(Exception):
    def __init__(self):
        mensagem = 'Variaveis declaradas depois do inicio da funcao'
        super().__init__(mensagem)