import os
from antlr4 import *
from gen.simplifiedJavaGrammarLexer import simplifiedJavaGrammarLexer
from gen.simplifiedJavaGrammarParser import simplifiedJavaGrammarParser
from MysimplifiedJavaGrammarListener import MySimplifiedJavaGrammarListener

if __name__ == '__main__':
    file = FileStream("exemplo12.txt")

    # parte lexica
    lexer = simplifiedJavaGrammarLexer(file)
    streams = CommonTokenStream(lexer)

    # parte analise sintatica
    parser = simplifiedJavaGrammarParser(streams)
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        exit(1)

    # parte analise semantica
    filename = 'ex'
    l = MySimplifiedJavaGrammarListener(filename)
    walker = ParseTreeWalker()
    walker.walk(l, tree)
    print("program " + filename + ".jsp generated")
