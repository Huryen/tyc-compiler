grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        raise UncloseString(self.text[1:] if len(self.text) > 1 else self.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(self.text[1:] if len(self.text) > 1 else self.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(self.text)
    else:
        return super().emit()
}

options {
    language = Python3;
}


program
    : (structDecl | funcDecl)+ EOF
    ;

structDecl : STRUCT ID LBRACE memberDecl* RBRACE SEMI ;
memberDecl : type ID SEMI ;
funcDecl   : (type | VOID)? ID LPAREN paramList? RPAREN block ;
paramList  : param (COMMA param)* ;
param      : type ID ;

block      : LBRACE stmt* RBRACE ;

stmt
    : varDecl       
    | expr SEMI     
    | block         
    | ifStmt
    | whileStmt
    | forStmt
    | switchStmt
    | jumpStmt
    ;

varDecl    : type idList SEMI | AUTO ID ASSIGN expr SEMI ;
idList     : idItem (COMMA idItem)* ;
idItem     : ID (ASSIGN expr)? ;

ifStmt     : IF LPAREN expr RPAREN stmt (ELSE stmt)? ;
whileStmt  : WHILE LPAREN expr RPAREN stmt ;
forStmt    : FOR LPAREN (varDecl | expr? SEMI) expr? SEMI expr? RPAREN stmt ;

switchStmt : SWITCH LPAREN expr RPAREN LBRACE caseList defaultStmt? RBRACE ;
caseList   : caseStmt* ;
caseStmt   : CASE expr COLON stmt* ;
defaultStmt: DEFAULT COLON stmt* ;

jumpStmt   : BREAK SEMI | CONTINUE SEMI | RETURN expr? SEMI ;


expr : assignExpr ;
assignExpr : logicOrExpr | ID ASSIGN assignExpr | logicOrExpr ASSIGN assignExpr ;
logicOrExpr: logicOrExpr OR andExpr | andExpr ;
andExpr    : andExpr AND eqExpr | eqExpr ;
eqExpr     : eqExpr (EQ | NEQ) relExpr | relExpr ;
relExpr    : relExpr (LT | LE | GT | GE) addExpr | addExpr ;
addExpr    : addExpr (ADD | SUB) mulExpr | mulExpr ;


mulExpr    : mulExpr (MUL | DIV | MOD) unaryExpr | unaryExpr ;


unaryExpr  : (NOT | SUB | ADD) unaryExpr | (INC | DEC) unaryExpr | postfixExpr ;

postfixExpr
    : primary (
        LPAREN listExpr? RPAREN   
        | DOT ID                  
        | INC | DEC               
      )* ;

listExpr
    : expr (COMMA expr)*
    ;

primary    : literal | ID | LPAREN expr RPAREN ;

literal    : INTLIT | FLOATLIT | STRINGLIT | TRUE | FALSE ;
type       : INT | FLOAT | STRING | BOOL | ID ;


WS : [ \t\r\n\f]+ -> skip ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;

AUTO: 'auto'; BREAK: 'break'; CASE: 'case'; CONTINUE: 'continue';
DEFAULT: 'default'; ELSE: 'else'; FLOAT: 'float'; FOR: 'for';
IF: 'if'; INT: 'int'; RETURN: 'return'; STRING: 'string';
STRUCT: 'struct'; SWITCH: 'switch'; VOID: 'void'; WHILE: 'while';
TRUE: 'true'; FALSE: 'false'; BOOL: 'bool'; 

ADD: '+'; SUB: '-'; MUL: '*'; DIV: '/'; MOD: '%';
EQ: '=='; NEQ: '!='; LT: '<'; GT: '>'; LE: '<='; GE: '>=';
OR: '||'; AND: '&&'; NOT: '!'; INC: '++'; DEC: '--';
ASSIGN: '='; DOT: '.';

LPAREN: '('; RPAREN: ')'; LBRACE: '{'; RBRACE: '}';
LBRACK: '['; RBRACK: ']'; SEMI: ';'; COMMA: ','; COLON: ':';

ILLEGAL_ESCAPE : '"' ( '\\' [bfrnt"'\\] | ~["\\\r\n] )* '\\' ~[bfrnt"'\\] ;
UNCLOSE_STRING : '"' ( '\\' [bfrnt"'\\] | ~["\\\r\n] )* [\r\n] | '"' ( '\\' [bfrnt"'\\] | ~["\\\r\n] )* EOF ;
STRINGLIT      : '"' ( '\\' [bfrnt"'\\] | ~["\\\r\n] )* '"' { self.text = self.text[1:-1] } ;

ID : [a-zA-Z_] [a-zA-Z0-9_]* ;
FLOATLIT : [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)? | '.' [0-9]+ ([eE] [+-]? [0-9]+)? | [0-9]+ [eE] [+-]? [0-9]+ ;
INTLIT   : [0-9]+ ;
ERROR_CHAR : . ;