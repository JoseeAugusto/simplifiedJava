grammar simplifiedJavaGrammar;

program
    : functionDeclarationArea* main EOF
    ;

functionDeclarationArea
    : ID '(' (TYPE ID(',' TYPE ID)*)? ')' ':' (TYPE | VOID) (variablesDeclarationArea)? commands* 'end'
    ;

main
    : 'main' ':' (variablesDeclarationArea)? commands* 'end'
    ;

variablesDeclarationArea
    : 'var' ':' (variablesDeclaration | constantsDeclaration)+
    ;

variablesDeclaration
    : ID(',' ID)* ':' TYPE ';'
    ;

constantsDeclaration
    : 'const' ID '=' terminal = (STRING | INT | BOOLEAN | FLOAT)(',' ID '=' terminal = (STRING | INT | BOOLEAN | FLOAT))* ';'
    ;

commands
    : ifCommand
    | whileCommand
    | assigmentCommand
    | callFunctionCommand ';'
    | printCommand
    | scanfCommand
    | returnCommand
    | breakCommand
    ;

callFunctionCommand
    : ID '(' (expression (',' expression)*)? ')'
    ;

ifCommand
    : ifBlock(elseBlock)?'end'
    ;

whileCommand
    : 'while' '(' expression ')' ':' commands* 'end'
    ;

breakCommand
    : 'break;'
    ;

printCommand
    : 'print' '(' expression(','expression)* ')' ';'
    ;

scanfCommand
    : 'scanf' '(' ID (',' ID)* ')' ';'
    ;

returnCommand
    : 'return' expression ';'
    ;

ifBlock
    : 'if' '(' expression ')' ':' commands*
    ;

elseBlock
    : 'else' ':' commands*
    ;

assigmentCommand
    : ID '=' expression ';'
    ;

expression returns [type, inhType]
    : expression op=('>='|'<='|'>'|'<') term #comparativeOperation
    | term #goTerm
    ;

term returns [type]
    : term op=('=='|'!=') term2 #equalDiffOperation
    | term2 #gotTerm2
    ;

term2 returns [type]
    : term2 op=('+'|'-') term3 #plusMinusOperation
    | term3 #goTerm3
    ;

term3 returns [type]
    : term3 op=('*'|'/') term4 #multDivOperation
    | term4 #goTerm4
    ;

term4 returns [type]
    : '-' term4 #unaryMinusOperation
    | term5 #goTerm5
    ;

term5 returns [type]
    : '!' term5 #notOperation
    | factor #goFactor
    ;

factor returns [type]
    : '(' expression ')' #openCloseParantesisTerminal
    | ID #idTerminal
    | INT #intTerminal
    | FLOAT #floatTerminal
    | STRING #stringTerminal
    | BOOLEAN #boolTerminal
    | callFunctionCommand #callFunctionTerminal
    ;

TYPE
    : 'int'
    | 'str'
    | 'float'
    | 'bool'
    ;

VOID
    : 'void'
    ;

INT
    : [0-9]+
    ;

FLOAT
    : [0-9]+[.][0-9]+
    ;

STRING
    : ["]~["]*["]
    ;

BOOLEAN
    : 'True'
    | 'False'
    ;

ID
    : [a-zA-Z][a-zA-Z0-9_]*
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

CommentInOneLine
    : '//' .*? '\n' -> skip
    ;

CommentOnMultipleLines
    : '/*' .*? '*/' -> skip
    ;
