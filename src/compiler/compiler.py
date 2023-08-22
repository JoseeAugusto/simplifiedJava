import os
from antlr4 import *
from gen.simplifiedJavaGrammarLexer import simplifiedJavaGrammarLexer
from gen.simplifiedJavaGrammarParser import simplifiedJavaGrammarParser
from MysimplifiedJavaGrammarListener import MySimplifiedJavaGrammarListener

def compiler(file):
    # parte lexica
    lexer = simplifiedJavaGrammarLexer(file)
    streams = CommonTokenStream(lexer)

    # parte analise sintatica
    parser = simplifiedJavaGrammarParser(streams)
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        exit(1)

    # parte analise semantica
    filename = 'code'
    l = MySimplifiedJavaGrammarListener(filename)
    walker = ParseTreeWalker()
    walker.walk(l, tree)
    print("program " + filename + ".jsp generated")