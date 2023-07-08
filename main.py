import os
from antlr4 import *
from gen.simplifiedJavaGrammarLexer import simplifiedJavaGrammarLexer
from gen.simplifiedJavaGrammarParser import simplifiedJavaGrammarParser
from MysimplifiedJavaGrammarListener import MySimplifiedJavaGrammarListener

if __name__ == '__main__':
    file = FileStream("exemplo.txt")

    # parte lexica
    lexer = simplifiedJavaGrammarLexer(file)
    streams = CommonTokenStream(lexer)

    # parte analise sintatica
    parser = simplifiedJavaGrammarParser(streams)
    tree = parser.program()

    # parte analise semantica
    filename = 'programExample'
    l = MySimplifiedJavaGrammarListener(filename)
    walker = ParseTreeWalker()
    walker.walk(l, tree)
