grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// TODO: Define grammar rules here
program
    : stmt* EOF
    ;

stmt
    : decl
    | expr SEMI
    | block
    | if_stmt
    | whileStmt
    | forStmt
    | jumpStmt
    ;

expr
    : assignExpr
    ;

assignExpr
    : logicOrExpr
    | ID ASSIGN assignExpr
    ;

logicOrExpr
    : logicOrExpr OR andExpr
    | andExpr
    ;

andExpr
    : andExpr AND eqExpr
    | eqExpr
    ;

eqExpr
    : eqExpr (EQ | NEQ) relExpr
    | relExpr
    ;

relExpr
    : relExpr (LT | LE | GT | GE) addExpr
    | addExpr
    ;

addExpr
    : addExpr (ADD | SUB) mulExpr
    | mulExpr
    ;

mulExpr
    : mulExpr (MUL | DIV | MOD) unaryExpr
    | unaryExpr
    ;

unaryExpr
    : (NOT | SUB) unaryExpr
    | primary
    ;

primary
    : literal
    | ID
    | LPAREN expr RPAREN
    ;

literal
    : INTLIT
    | FLOATLIT
    | STRINGLIT
    | TRUE
    | FALSE
    ;

type
    : INT
    | FLOAT
    | BOOL
    | STRING
    ;

decl
    : type idList SEMI
    ;

idList
    : idItem (COMMA idItem)*
    ;

idItem
    : ID
    | ID ASSIGN expr
    ;

block
    : LBRACE stmt* RBRACE
    ;

if_stmt
    : IF LPAREN expr RPAREN stmt (ELSE stmt)?
    ;

whileStmt
    : WHILE LPAREN expr RPAREN stmt
    ;

forStmt
    : FOR LPAREN forInit SEMI forCond SEMI forUpdate RPAREN stmt
    ;

forInit
    : expr
    | 
    ;

forCond
    : expr
    | 
    ;


forUpdate
    : expr
    | 
    ;

jumpStmt
    : BREAK SEMI
    | CONTINUE SEMI
    | RETURN expr? SEMI
    ;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;

IF        : 'if';
ELSE      : 'else';
WHILE     : 'while';
FOR       : 'for';
BREAK     : 'break';
CONTINUE  : 'continue';
RETURN    : 'return';

INT       : 'int';
FLOAT     : 'float';
BOOL      : 'bool';
STRING    : 'string';
VOID      : 'void';

TRUE      : 'true';
FALSE     : 'false';

ID : [a-zA-Z_][a-zA-Z_0-9]*;

fragment DIGIT : [0-9];

FLOATLIT
    : DIGIT+ '.' DIGIT* ([eE] [+-]? DIGIT+)?   
    | '.' DIGIT+ ([eE] [+-]? DIGIT+)?          
    | DIGIT+ [eE] [+-]? DIGIT+                  
    ;

INTLIT
    : DIGIT+
    ;

EQ        : '==';
NEQ       : '!=';
LE        : '<=';
GE        : '>=';
AND       : '&&';
OR        : '||';

ASSIGN    : '=';
LT        : '<';
GT        : '>';
NOT       : '!';

ADD       : '+';
SUB       : '-';
MUL       : '*';
DIV       : '/';
MOD       : '%';

LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
LBRACK  : '[';
RBRACK  : ']';
SEMI    : ';';
COMMA   : ',';

fragment ESC_SEQ
    : '\\' [btnfr"\\]
    ;

ILLEGAL_ESCAPE
    : '"' ( ~["\\\r\n] | ESC_SEQ )* '\\' ~[btnfr"\\]
      { raise IllegalEscape(self.text[1:]) }
    ;

UNCLOSE_STRING
    : '"' ( ~["\\\r\n] | ESC_SEQ )* ( EOF | '\r' | '\n' )
      { raise UncloseString(self.text[1:]) }
    ;

STRINGLIT
    : '"' ( ~["\\\r\n] | ESC_SEQ )* '"'
      { self.text = self.text[1:-1] }
    ;

ERROR_CHAR: .;

