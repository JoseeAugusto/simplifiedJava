class ErrorVariableNotDeclared(Exception):
    def __init__(self, line, id):
        message = 'Line {}: ID not declared: {}'.format(line, id)
        super().__init__(message)

class ErrorVariableNotInitialized(Exception):
    def __init__(self, line, id):
        message = 'Line {}: ID not initialized: {}'.format(line, id)
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

class ErrorBreakScope(Exception):
    def __init__(self, line):
        message = 'Line {}: break out of a while scope'.format(line)
        super().__init__(message)

class ErrorReturnInNonTypedFunction(Exception):
    def __init__(self, line):
        message = 'Line {}: return in a non-typed function'.format(line)
        super().__init__(message)

class ErrorExpectedReturnCommand(Exception):
    def __init__(self, line):
        message = 'Line {}: expected return command'.format(line)
        super().__init__(message)

class ErrorTypeExpression(Exception):
    def __init__(self, line, operation, type1, type2=None):
        message = 'line {}: Operation {} not supported for the types: {} e {}'.format(line, operation, type1, type2) if type2 else 'Line {}: Operation {} not supported for the types: {}'.format(line, operation, type1)
        super().__init__(message)

class ErrorExpectedArgument(Exception):
    def __init__(self, line, expectedArgs, receivedArgs):
        message = 'Line {}: Expected {} arguments, but {} received'.format(line, expectedArgs, receivedArgs)
        super().__init__(message)

class ErrorVariableNotFoundAtSymbolTable(Exception):
    def __init__(self, varName, scope):
        message = 'Variable {} not found in scope {}'.format(varName, 'LOCAL' if scope else 'GLOBAL')
        super().__init__(message)

class ErrorConstantChangeValue(Exception):
    def __init__(self, line):
        message = 'Line {}: Constants cannot be changed'.format(line)
        super().__init__(message)