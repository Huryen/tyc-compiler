# Generated from c:/Users/ASUS/Desktop/tyc-compiler/src/grammar/TyC.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,56,359,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,4,0,69,8,0,11,0,12,0,70,1,0,1,0,1,1,1,1,1,1,1,1,5,1,79,8,1,10,
        1,12,1,82,9,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,3,3,93,8,3,1,3,
        1,3,1,3,3,3,98,8,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,106,8,4,10,4,12,4,
        109,9,4,1,5,1,5,1,5,1,6,1,6,5,6,116,8,6,10,6,12,6,119,9,6,1,6,1,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,133,8,7,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,145,8,8,1,9,1,9,1,9,5,9,150,8,
        9,10,9,12,9,153,9,9,1,10,1,10,1,10,3,10,158,8,10,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,3,11,167,8,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,13,1,13,1,13,1,13,3,13,179,8,13,1,13,3,13,182,8,13,1,13,3,13,185,
        8,13,1,13,1,13,3,13,189,8,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,3,14,201,8,14,1,14,1,14,1,15,5,15,206,8,15,10,15,
        12,15,209,9,15,1,16,1,16,1,16,1,16,5,16,215,8,16,10,16,12,16,218,
        9,16,1,17,1,17,1,17,5,17,223,8,17,10,17,12,17,226,9,17,1,18,1,18,
        1,18,1,18,1,18,1,18,3,18,234,8,18,1,18,3,18,237,8,18,1,19,1,19,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,249,8,20,1,21,1,21,1,
        21,1,21,1,21,1,21,5,21,257,8,21,10,21,12,21,260,9,21,1,22,1,22,1,
        22,1,22,1,22,1,22,5,22,268,8,22,10,22,12,22,271,9,22,1,23,1,23,1,
        23,1,23,1,23,1,23,5,23,279,8,23,10,23,12,23,282,9,23,1,24,1,24,1,
        24,1,24,1,24,1,24,5,24,290,8,24,10,24,12,24,293,9,24,1,25,1,25,1,
        25,1,25,1,25,1,25,5,25,301,8,25,10,25,12,25,304,9,25,1,26,1,26,1,
        26,1,26,1,26,1,26,5,26,312,8,26,10,26,12,26,315,9,26,1,27,1,27,1,
        27,1,27,1,27,3,27,322,8,27,1,28,1,28,1,28,3,28,327,8,28,1,28,1,28,
        1,28,1,28,1,28,5,28,334,8,28,10,28,12,28,337,9,28,1,29,1,29,1,29,
        5,29,342,8,29,10,29,12,29,345,9,29,1,30,1,30,1,30,1,30,1,30,1,30,
        3,30,353,8,30,1,31,1,31,1,32,1,32,1,32,0,6,42,44,46,48,50,52,33,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,64,0,8,1,0,28,29,1,0,30,33,1,0,23,24,
        1,0,25,27,2,0,23,24,36,36,1,0,37,38,3,0,20,21,52,52,54,55,5,0,10,
        10,13,13,15,15,22,22,53,53,373,0,68,1,0,0,0,2,74,1,0,0,0,4,86,1,
        0,0,0,6,92,1,0,0,0,8,102,1,0,0,0,10,110,1,0,0,0,12,113,1,0,0,0,14,
        132,1,0,0,0,16,144,1,0,0,0,18,146,1,0,0,0,20,154,1,0,0,0,22,159,
        1,0,0,0,24,168,1,0,0,0,26,174,1,0,0,0,28,193,1,0,0,0,30,207,1,0,
        0,0,32,210,1,0,0,0,34,219,1,0,0,0,36,236,1,0,0,0,38,238,1,0,0,0,
        40,248,1,0,0,0,42,250,1,0,0,0,44,261,1,0,0,0,46,272,1,0,0,0,48,283,
        1,0,0,0,50,294,1,0,0,0,52,305,1,0,0,0,54,321,1,0,0,0,56,323,1,0,
        0,0,58,338,1,0,0,0,60,352,1,0,0,0,62,354,1,0,0,0,64,356,1,0,0,0,
        66,69,3,2,1,0,67,69,3,6,3,0,68,66,1,0,0,0,68,67,1,0,0,0,69,70,1,
        0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,73,5,0,0,1,73,
        1,1,0,0,0,74,75,5,16,0,0,75,76,5,53,0,0,76,80,5,43,0,0,77,79,3,4,
        2,0,78,77,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,83,
        1,0,0,0,82,80,1,0,0,0,83,84,5,44,0,0,84,85,5,47,0,0,85,3,1,0,0,0,
        86,87,3,64,32,0,87,88,5,53,0,0,88,89,5,47,0,0,89,5,1,0,0,0,90,93,
        3,64,32,0,91,93,5,18,0,0,92,90,1,0,0,0,92,91,1,0,0,0,92,93,1,0,0,
        0,93,94,1,0,0,0,94,95,5,53,0,0,95,97,5,41,0,0,96,98,3,8,4,0,97,96,
        1,0,0,0,97,98,1,0,0,0,98,99,1,0,0,0,99,100,5,42,0,0,100,101,3,12,
        6,0,101,7,1,0,0,0,102,107,3,10,5,0,103,104,5,48,0,0,104,106,3,10,
        5,0,105,103,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,
        0,0,108,9,1,0,0,0,109,107,1,0,0,0,110,111,3,64,32,0,111,112,5,53,
        0,0,112,11,1,0,0,0,113,117,5,43,0,0,114,116,3,14,7,0,115,114,1,0,
        0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,120,1,0,
        0,0,119,117,1,0,0,0,120,121,5,44,0,0,121,13,1,0,0,0,122,133,3,16,
        8,0,123,124,3,38,19,0,124,125,5,47,0,0,125,133,1,0,0,0,126,133,3,
        12,6,0,127,133,3,22,11,0,128,133,3,24,12,0,129,133,3,26,13,0,130,
        133,3,28,14,0,131,133,3,36,18,0,132,122,1,0,0,0,132,123,1,0,0,0,
        132,126,1,0,0,0,132,127,1,0,0,0,132,128,1,0,0,0,132,129,1,0,0,0,
        132,130,1,0,0,0,132,131,1,0,0,0,133,15,1,0,0,0,134,135,3,64,32,0,
        135,136,3,18,9,0,136,137,5,47,0,0,137,145,1,0,0,0,138,139,5,4,0,
        0,139,140,5,53,0,0,140,141,5,39,0,0,141,142,3,38,19,0,142,143,5,
        47,0,0,143,145,1,0,0,0,144,134,1,0,0,0,144,138,1,0,0,0,145,17,1,
        0,0,0,146,151,3,20,10,0,147,148,5,48,0,0,148,150,3,20,10,0,149,147,
        1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,19,1,
        0,0,0,153,151,1,0,0,0,154,157,5,53,0,0,155,156,5,39,0,0,156,158,
        3,38,19,0,157,155,1,0,0,0,157,158,1,0,0,0,158,21,1,0,0,0,159,160,
        5,12,0,0,160,161,5,41,0,0,161,162,3,38,19,0,162,163,5,42,0,0,163,
        166,3,14,7,0,164,165,5,9,0,0,165,167,3,14,7,0,166,164,1,0,0,0,166,
        167,1,0,0,0,167,23,1,0,0,0,168,169,5,19,0,0,169,170,5,41,0,0,170,
        171,3,38,19,0,171,172,5,42,0,0,172,173,3,14,7,0,173,25,1,0,0,0,174,
        175,5,11,0,0,175,181,5,41,0,0,176,182,3,16,8,0,177,179,3,38,19,0,
        178,177,1,0,0,0,178,179,1,0,0,0,179,180,1,0,0,0,180,182,5,47,0,0,
        181,176,1,0,0,0,181,178,1,0,0,0,182,184,1,0,0,0,183,185,3,38,19,
        0,184,183,1,0,0,0,184,185,1,0,0,0,185,186,1,0,0,0,186,188,5,47,0,
        0,187,189,3,38,19,0,188,187,1,0,0,0,188,189,1,0,0,0,189,190,1,0,
        0,0,190,191,5,42,0,0,191,192,3,14,7,0,192,27,1,0,0,0,193,194,5,17,
        0,0,194,195,5,41,0,0,195,196,3,38,19,0,196,197,5,42,0,0,197,198,
        5,43,0,0,198,200,3,30,15,0,199,201,3,34,17,0,200,199,1,0,0,0,200,
        201,1,0,0,0,201,202,1,0,0,0,202,203,5,44,0,0,203,29,1,0,0,0,204,
        206,3,32,16,0,205,204,1,0,0,0,206,209,1,0,0,0,207,205,1,0,0,0,207,
        208,1,0,0,0,208,31,1,0,0,0,209,207,1,0,0,0,210,211,5,6,0,0,211,212,
        3,38,19,0,212,216,5,49,0,0,213,215,3,14,7,0,214,213,1,0,0,0,215,
        218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,33,1,0,0,0,218,216,
        1,0,0,0,219,220,5,8,0,0,220,224,5,49,0,0,221,223,3,14,7,0,222,221,
        1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,35,1,
        0,0,0,226,224,1,0,0,0,227,228,5,5,0,0,228,237,5,47,0,0,229,230,5,
        7,0,0,230,237,5,47,0,0,231,233,5,14,0,0,232,234,3,38,19,0,233,232,
        1,0,0,0,233,234,1,0,0,0,234,235,1,0,0,0,235,237,5,47,0,0,236,227,
        1,0,0,0,236,229,1,0,0,0,236,231,1,0,0,0,237,37,1,0,0,0,238,239,3,
        40,20,0,239,39,1,0,0,0,240,249,3,42,21,0,241,242,5,53,0,0,242,243,
        5,39,0,0,243,249,3,40,20,0,244,245,3,42,21,0,245,246,5,39,0,0,246,
        247,3,40,20,0,247,249,1,0,0,0,248,240,1,0,0,0,248,241,1,0,0,0,248,
        244,1,0,0,0,249,41,1,0,0,0,250,251,6,21,-1,0,251,252,3,44,22,0,252,
        258,1,0,0,0,253,254,10,2,0,0,254,255,5,34,0,0,255,257,3,44,22,0,
        256,253,1,0,0,0,257,260,1,0,0,0,258,256,1,0,0,0,258,259,1,0,0,0,
        259,43,1,0,0,0,260,258,1,0,0,0,261,262,6,22,-1,0,262,263,3,46,23,
        0,263,269,1,0,0,0,264,265,10,2,0,0,265,266,5,35,0,0,266,268,3,46,
        23,0,267,264,1,0,0,0,268,271,1,0,0,0,269,267,1,0,0,0,269,270,1,0,
        0,0,270,45,1,0,0,0,271,269,1,0,0,0,272,273,6,23,-1,0,273,274,3,48,
        24,0,274,280,1,0,0,0,275,276,10,2,0,0,276,277,7,0,0,0,277,279,3,
        48,24,0,278,275,1,0,0,0,279,282,1,0,0,0,280,278,1,0,0,0,280,281,
        1,0,0,0,281,47,1,0,0,0,282,280,1,0,0,0,283,284,6,24,-1,0,284,285,
        3,50,25,0,285,291,1,0,0,0,286,287,10,2,0,0,287,288,7,1,0,0,288,290,
        3,50,25,0,289,286,1,0,0,0,290,293,1,0,0,0,291,289,1,0,0,0,291,292,
        1,0,0,0,292,49,1,0,0,0,293,291,1,0,0,0,294,295,6,25,-1,0,295,296,
        3,52,26,0,296,302,1,0,0,0,297,298,10,2,0,0,298,299,7,2,0,0,299,301,
        3,52,26,0,300,297,1,0,0,0,301,304,1,0,0,0,302,300,1,0,0,0,302,303,
        1,0,0,0,303,51,1,0,0,0,304,302,1,0,0,0,305,306,6,26,-1,0,306,307,
        3,54,27,0,307,313,1,0,0,0,308,309,10,2,0,0,309,310,7,3,0,0,310,312,
        3,54,27,0,311,308,1,0,0,0,312,315,1,0,0,0,313,311,1,0,0,0,313,314,
        1,0,0,0,314,53,1,0,0,0,315,313,1,0,0,0,316,317,7,4,0,0,317,322,3,
        54,27,0,318,319,7,5,0,0,319,322,3,54,27,0,320,322,3,56,28,0,321,
        316,1,0,0,0,321,318,1,0,0,0,321,320,1,0,0,0,322,55,1,0,0,0,323,335,
        3,60,30,0,324,326,5,41,0,0,325,327,3,58,29,0,326,325,1,0,0,0,326,
        327,1,0,0,0,327,328,1,0,0,0,328,334,5,42,0,0,329,330,5,40,0,0,330,
        334,5,53,0,0,331,334,5,37,0,0,332,334,5,38,0,0,333,324,1,0,0,0,333,
        329,1,0,0,0,333,331,1,0,0,0,333,332,1,0,0,0,334,337,1,0,0,0,335,
        333,1,0,0,0,335,336,1,0,0,0,336,57,1,0,0,0,337,335,1,0,0,0,338,343,
        3,38,19,0,339,340,5,48,0,0,340,342,3,38,19,0,341,339,1,0,0,0,342,
        345,1,0,0,0,343,341,1,0,0,0,343,344,1,0,0,0,344,59,1,0,0,0,345,343,
        1,0,0,0,346,353,3,62,31,0,347,353,5,53,0,0,348,349,5,41,0,0,349,
        350,3,38,19,0,350,351,5,42,0,0,351,353,1,0,0,0,352,346,1,0,0,0,352,
        347,1,0,0,0,352,348,1,0,0,0,353,61,1,0,0,0,354,355,7,6,0,0,355,63,
        1,0,0,0,356,357,7,7,0,0,357,65,1,0,0,0,35,68,70,80,92,97,107,117,
        132,144,151,157,166,178,181,184,188,200,207,216,224,233,236,248,
        258,269,280,291,302,313,321,326,333,335,343,352
    ]

class TyCParser ( Parser ):

    grammarFileName = "TyC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'auto'", "'break'", "'case'", "'continue'", "'default'", 
                     "'else'", "'float'", "'for'", "'if'", "'int'", "'return'", 
                     "'string'", "'struct'", "'switch'", "'void'", "'while'", 
                     "'true'", "'false'", "'bool'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'||'", "'&&'", "'!'", "'++'", "'--'", "'='", 
                     "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
                     "','", "':'" ]

    symbolicNames = [ "<INVALID>", "WS", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "AUTO", "BREAK", "CASE", "CONTINUE", "DEFAULT", "ELSE", 
                      "FLOAT", "FOR", "IF", "INT", "RETURN", "STRING", "STRUCT", 
                      "SWITCH", "VOID", "WHILE", "TRUE", "FALSE", "BOOL", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", "NEQ", "LT", 
                      "GT", "LE", "GE", "OR", "AND", "NOT", "INC", "DEC", 
                      "ASSIGN", "DOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACK", "RBRACK", "SEMI", "COMMA", "COLON", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "STRINGLIT", "ID", "FLOATLIT", "INTLIT", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_structDecl = 1
    RULE_memberDecl = 2
    RULE_funcDecl = 3
    RULE_paramList = 4
    RULE_param = 5
    RULE_block = 6
    RULE_stmt = 7
    RULE_varDecl = 8
    RULE_idList = 9
    RULE_idItem = 10
    RULE_ifStmt = 11
    RULE_whileStmt = 12
    RULE_forStmt = 13
    RULE_switchStmt = 14
    RULE_caseList = 15
    RULE_caseStmt = 16
    RULE_defaultStmt = 17
    RULE_jumpStmt = 18
    RULE_expr = 19
    RULE_assignExpr = 20
    RULE_logicOrExpr = 21
    RULE_andExpr = 22
    RULE_eqExpr = 23
    RULE_relExpr = 24
    RULE_addExpr = 25
    RULE_mulExpr = 26
    RULE_unaryExpr = 27
    RULE_postfixExpr = 28
    RULE_listExpr = 29
    RULE_primary = 30
    RULE_literal = 31
    RULE_type = 32

    ruleNames =  [ "program", "structDecl", "memberDecl", "funcDecl", "paramList", 
                   "param", "block", "stmt", "varDecl", "idList", "idItem", 
                   "ifStmt", "whileStmt", "forStmt", "switchStmt", "caseList", 
                   "caseStmt", "defaultStmt", "jumpStmt", "expr", "assignExpr", 
                   "logicOrExpr", "andExpr", "eqExpr", "relExpr", "addExpr", 
                   "mulExpr", "unaryExpr", "postfixExpr", "listExpr", "primary", 
                   "literal", "type" ]

    EOF = Token.EOF
    WS=1
    LINE_COMMENT=2
    BLOCK_COMMENT=3
    AUTO=4
    BREAK=5
    CASE=6
    CONTINUE=7
    DEFAULT=8
    ELSE=9
    FLOAT=10
    FOR=11
    IF=12
    INT=13
    RETURN=14
    STRING=15
    STRUCT=16
    SWITCH=17
    VOID=18
    WHILE=19
    TRUE=20
    FALSE=21
    BOOL=22
    ADD=23
    SUB=24
    MUL=25
    DIV=26
    MOD=27
    EQ=28
    NEQ=29
    LT=30
    GT=31
    LE=32
    GE=33
    OR=34
    AND=35
    NOT=36
    INC=37
    DEC=38
    ASSIGN=39
    DOT=40
    LPAREN=41
    RPAREN=42
    LBRACE=43
    RBRACE=44
    LBRACK=45
    RBRACK=46
    SEMI=47
    COMMA=48
    COLON=49
    ILLEGAL_ESCAPE=50
    UNCLOSE_STRING=51
    STRINGLIT=52
    ID=53
    FLOATLIT=54
    INTLIT=55
    ERROR_CHAR=56

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TyCParser.EOF, 0)

        def structDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StructDeclContext)
            else:
                return self.getTypedRuleContext(TyCParser.StructDeclContext,i)


        def funcDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.FuncDeclContext)
            else:
                return self.getTypedRuleContext(TyCParser.FuncDeclContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_program




    def program(self):

        localctx = TyCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [16]:
                    self.state = 66
                    self.structDecl()
                    pass
                elif token in [10, 13, 15, 18, 22, 53]:
                    self.state = 67
                    self.funcDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 70 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 9007199259304960) != 0)):
                    break

            self.state = 72
            self.match(TyCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(TyCParser.STRUCT, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def memberDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.MemberDeclContext)
            else:
                return self.getTypedRuleContext(TyCParser.MemberDeclContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_structDecl




    def structDecl(self):

        localctx = TyCParser.StructDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_structDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(TyCParser.STRUCT)
            self.state = 75
            self.match(TyCParser.ID)
            self.state = 76
            self.match(TyCParser.LBRACE)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 9007199258977280) != 0):
                self.state = 77
                self.memberDecl()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 83
            self.match(TyCParser.RBRACE)
            self.state = 84
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_memberDecl




    def memberDecl(self):

        localctx = TyCParser.MemberDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_memberDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.type_()
            self.state = 87
            self.match(TyCParser.ID)
            self.state = 88
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(TyCParser.BlockContext,0)


        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def VOID(self):
            return self.getToken(TyCParser.VOID, 0)

        def paramList(self):
            return self.getTypedRuleContext(TyCParser.ParamListContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_funcDecl




    def funcDecl(self):

        localctx = TyCParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 90
                self.type_()

            elif la_ == 2:
                self.state = 91
                self.match(TyCParser.VOID)


            self.state = 94
            self.match(TyCParser.ID)
            self.state = 95
            self.match(TyCParser.LPAREN)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9007199258977280) != 0):
                self.state = 96
                self.paramList()


            self.state = 99
            self.match(TyCParser.RPAREN)
            self.state = 100
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ParamContext)
            else:
                return self.getTypedRuleContext(TyCParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.COMMA)
            else:
                return self.getToken(TyCParser.COMMA, i)

        def getRuleIndex(self):
            return TyCParser.RULE_paramList




    def paramList(self):

        localctx = TyCParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.param()
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 103
                self.match(TyCParser.COMMA)
                self.state = 104
                self.param()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_param




    def param(self):

        localctx = TyCParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.type_()
            self.state = 111
            self.match(TyCParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.StmtContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_block




    def block(self):

        localctx = TyCParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(TyCParser.LBRACE)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67565470596398256) != 0):
                self.state = 114
                self.stmt()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self.match(TyCParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(TyCParser.VarDeclContext,0)


        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def block(self):
            return self.getTypedRuleContext(TyCParser.BlockContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(TyCParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(TyCParser.WhileStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(TyCParser.ForStmtContext,0)


        def switchStmt(self):
            return self.getTypedRuleContext(TyCParser.SwitchStmtContext,0)


        def jumpStmt(self):
            return self.getTypedRuleContext(TyCParser.JumpStmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_stmt




    def stmt(self):

        localctx = TyCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stmt)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.expr()
                self.state = 124
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.block()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.ifStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                self.whileStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 129
                self.forStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 130
                self.switchStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 131
                self.jumpStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def idList(self):
            return self.getTypedRuleContext(TyCParser.IdListContext,0)


        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def AUTO(self):
            return self.getToken(TyCParser.AUTO, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_varDecl




    def varDecl(self):

        localctx = TyCParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_varDecl)
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 13, 15, 22, 53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.type_()
                self.state = 135
                self.idList()
                self.state = 136
                self.match(TyCParser.SEMI)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(TyCParser.AUTO)
                self.state = 139
                self.match(TyCParser.ID)
                self.state = 140
                self.match(TyCParser.ASSIGN)
                self.state = 141
                self.expr()
                self.state = 142
                self.match(TyCParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.IdItemContext)
            else:
                return self.getTypedRuleContext(TyCParser.IdItemContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.COMMA)
            else:
                return self.getToken(TyCParser.COMMA, i)

        def getRuleIndex(self):
            return TyCParser.RULE_idList




    def idList(self):

        localctx = TyCParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.idItem()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 147
                self.match(TyCParser.COMMA)
                self.state = 148
                self.idItem()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_idItem




    def idItem(self):

        localctx = TyCParser.IdItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_idItem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(TyCParser.ID)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 155
                self.match(TyCParser.ASSIGN)
                self.state = 156
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(TyCParser.IF, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(TyCParser.ELSE, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_ifStmt




    def ifStmt(self):

        localctx = TyCParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(TyCParser.IF)
            self.state = 160
            self.match(TyCParser.LPAREN)
            self.state = 161
            self.expr()
            self.state = 162
            self.match(TyCParser.RPAREN)
            self.state = 163
            self.stmt()
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 164
                self.match(TyCParser.ELSE)
                self.state = 165
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(TyCParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def stmt(self):
            return self.getTypedRuleContext(TyCParser.StmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_whileStmt




    def whileStmt(self):

        localctx = TyCParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(TyCParser.WHILE)
            self.state = 169
            self.match(TyCParser.LPAREN)
            self.state = 170
            self.expr()
            self.state = 171
            self.match(TyCParser.RPAREN)
            self.state = 172
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(TyCParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.SEMI)
            else:
                return self.getToken(TyCParser.SEMI, i)

        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def stmt(self):
            return self.getTypedRuleContext(TyCParser.StmtContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(TyCParser.VarDeclContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_forStmt




    def forStmt(self):

        localctx = TyCParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(TyCParser.FOR)
            self.state = 175
            self.match(TyCParser.LPAREN)
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 176
                self.varDecl()
                pass

            elif la_ == 2:
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 67556674498461696) != 0):
                    self.state = 177
                    self.expr()


                self.state = 180
                self.match(TyCParser.SEMI)
                pass


            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 67556674498461696) != 0):
                self.state = 183
                self.expr()


            self.state = 186
            self.match(TyCParser.SEMI)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 67556674498461696) != 0):
                self.state = 187
                self.expr()


            self.state = 190
            self.match(TyCParser.RPAREN)
            self.state = 191
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(TyCParser.SWITCH, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)

        def caseList(self):
            return self.getTypedRuleContext(TyCParser.CaseListContext,0)


        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)

        def defaultStmt(self):
            return self.getTypedRuleContext(TyCParser.DefaultStmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_switchStmt




    def switchStmt(self):

        localctx = TyCParser.SwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_switchStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(TyCParser.SWITCH)
            self.state = 194
            self.match(TyCParser.LPAREN)
            self.state = 195
            self.expr()
            self.state = 196
            self.match(TyCParser.RPAREN)
            self.state = 197
            self.match(TyCParser.LBRACE)
            self.state = 198
            self.caseList()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 199
                self.defaultStmt()


            self.state = 202
            self.match(TyCParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def caseStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.CaseStmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.CaseStmtContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_caseList




    def caseList(self):

        localctx = TyCParser.CaseListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_caseList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 204
                self.caseStmt()
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(TyCParser.CASE, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def COLON(self):
            return self.getToken(TyCParser.COLON, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.StmtContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_caseStmt




    def caseStmt(self):

        localctx = TyCParser.CaseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_caseStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(TyCParser.CASE)
            self.state = 211
            self.expr()
            self.state = 212
            self.match(TyCParser.COLON)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67565470596398256) != 0):
                self.state = 213
                self.stmt()
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(TyCParser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(TyCParser.COLON, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.StmtContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_defaultStmt




    def defaultStmt(self):

        localctx = TyCParser.DefaultStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_defaultStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(TyCParser.DEFAULT)
            self.state = 220
            self.match(TyCParser.COLON)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67565470596398256) != 0):
                self.state = 221
                self.stmt()
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JumpStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(TyCParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def CONTINUE(self):
            return self.getToken(TyCParser.CONTINUE, 0)

        def RETURN(self):
            return self.getToken(TyCParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_jumpStmt




    def jumpStmt(self):

        localctx = TyCParser.JumpStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_jumpStmt)
        self._la = 0 # Token type
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.match(TyCParser.BREAK)
                self.state = 228
                self.match(TyCParser.SEMI)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.match(TyCParser.CONTINUE)
                self.state = 230
                self.match(TyCParser.SEMI)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 231
                self.match(TyCParser.RETURN)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 67556674498461696) != 0):
                    self.state = 232
                    self.expr()


                self.state = 235
                self.match(TyCParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignExpr(self):
            return self.getTypedRuleContext(TyCParser.AssignExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_expr




    def expr(self):

        localctx = TyCParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.assignExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicOrExpr(self):
            return self.getTypedRuleContext(TyCParser.LogicOrExprContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def assignExpr(self):
            return self.getTypedRuleContext(TyCParser.AssignExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_assignExpr




    def assignExpr(self):

        localctx = TyCParser.AssignExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignExpr)
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.logicOrExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.match(TyCParser.ID)
                self.state = 242
                self.match(TyCParser.ASSIGN)
                self.state = 243
                self.assignExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 244
                self.logicOrExpr(0)
                self.state = 245
                self.match(TyCParser.ASSIGN)
                self.state = 246
                self.assignExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicOrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpr(self):
            return self.getTypedRuleContext(TyCParser.AndExprContext,0)


        def logicOrExpr(self):
            return self.getTypedRuleContext(TyCParser.LogicOrExprContext,0)


        def OR(self):
            return self.getToken(TyCParser.OR, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_logicOrExpr



    def logicOrExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.LogicOrExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_logicOrExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.andExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.LogicOrExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicOrExpr)
                    self.state = 253
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 254
                    self.match(TyCParser.OR)
                    self.state = 255
                    self.andExpr(0) 
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eqExpr(self):
            return self.getTypedRuleContext(TyCParser.EqExprContext,0)


        def andExpr(self):
            return self.getTypedRuleContext(TyCParser.AndExprContext,0)


        def AND(self):
            return self.getToken(TyCParser.AND, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_andExpr



    def andExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.AndExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_andExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.eqExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.AndExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_andExpr)
                    self.state = 264
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 265
                    self.match(TyCParser.AND)
                    self.state = 266
                    self.eqExpr(0) 
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class EqExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relExpr(self):
            return self.getTypedRuleContext(TyCParser.RelExprContext,0)


        def eqExpr(self):
            return self.getTypedRuleContext(TyCParser.EqExprContext,0)


        def EQ(self):
            return self.getToken(TyCParser.EQ, 0)

        def NEQ(self):
            return self.getToken(TyCParser.NEQ, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_eqExpr



    def eqExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.EqExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_eqExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.relExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 280
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.EqExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_eqExpr)
                    self.state = 275
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 276
                    _la = self._input.LA(1)
                    if not(_la==28 or _la==29):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 277
                    self.relExpr(0) 
                self.state = 282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addExpr(self):
            return self.getTypedRuleContext(TyCParser.AddExprContext,0)


        def relExpr(self):
            return self.getTypedRuleContext(TyCParser.RelExprContext,0)


        def LT(self):
            return self.getToken(TyCParser.LT, 0)

        def LE(self):
            return self.getToken(TyCParser.LE, 0)

        def GT(self):
            return self.getToken(TyCParser.GT, 0)

        def GE(self):
            return self.getToken(TyCParser.GE, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_relExpr



    def relExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.RelExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_relExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.addExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.RelExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relExpr)
                    self.state = 286
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 287
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16106127360) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 288
                    self.addExpr(0) 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AddExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mulExpr(self):
            return self.getTypedRuleContext(TyCParser.MulExprContext,0)


        def addExpr(self):
            return self.getTypedRuleContext(TyCParser.AddExprContext,0)


        def ADD(self):
            return self.getToken(TyCParser.ADD, 0)

        def SUB(self):
            return self.getToken(TyCParser.SUB, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_addExpr



    def addExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.AddExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_addExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.mulExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.AddExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_addExpr)
                    self.state = 297
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 298
                    _la = self._input.LA(1)
                    if not(_la==23 or _la==24):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 299
                    self.mulExpr(0) 
                self.state = 304
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MulExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self):
            return self.getTypedRuleContext(TyCParser.UnaryExprContext,0)


        def mulExpr(self):
            return self.getTypedRuleContext(TyCParser.MulExprContext,0)


        def MUL(self):
            return self.getToken(TyCParser.MUL, 0)

        def DIV(self):
            return self.getToken(TyCParser.DIV, 0)

        def MOD(self):
            return self.getToken(TyCParser.MOD, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_mulExpr



    def mulExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.MulExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_mulExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.unaryExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.MulExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                    self.state = 308
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 309
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 310
                    self.unaryExpr() 
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self):
            return self.getTypedRuleContext(TyCParser.UnaryExprContext,0)


        def NOT(self):
            return self.getToken(TyCParser.NOT, 0)

        def SUB(self):
            return self.getToken(TyCParser.SUB, 0)

        def ADD(self):
            return self.getToken(TyCParser.ADD, 0)

        def INC(self):
            return self.getToken(TyCParser.INC, 0)

        def DEC(self):
            return self.getToken(TyCParser.DEC, 0)

        def postfixExpr(self):
            return self.getTypedRuleContext(TyCParser.PostfixExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_unaryExpr




    def unaryExpr(self):

        localctx = TyCParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 68744642560) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 317
                self.unaryExpr()
                pass
            elif token in [37, 38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                _la = self._input.LA(1)
                if not(_la==37 or _la==38):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 319
                self.unaryExpr()
                pass
            elif token in [20, 21, 41, 52, 53, 54, 55]:
                self.enterOuterAlt(localctx, 3)
                self.state = 320
                self.postfixExpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(TyCParser.PrimaryContext,0)


        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.LPAREN)
            else:
                return self.getToken(TyCParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.RPAREN)
            else:
                return self.getToken(TyCParser.RPAREN, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.DOT)
            else:
                return self.getToken(TyCParser.DOT, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.ID)
            else:
                return self.getToken(TyCParser.ID, i)

        def INC(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.INC)
            else:
                return self.getToken(TyCParser.INC, i)

        def DEC(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.DEC)
            else:
                return self.getToken(TyCParser.DEC, i)

        def listExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ListExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ListExprContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_postfixExpr




    def postfixExpr(self):

        localctx = TyCParser.PostfixExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_postfixExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.primary()
            self.state = 335
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 333
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [41]:
                        self.state = 324
                        self.match(TyCParser.LPAREN)
                        self.state = 326
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 67556674498461696) != 0):
                            self.state = 325
                            self.listExpr()


                        self.state = 328
                        self.match(TyCParser.RPAREN)
                        pass
                    elif token in [40]:
                        self.state = 329
                        self.match(TyCParser.DOT)
                        self.state = 330
                        self.match(TyCParser.ID)
                        pass
                    elif token in [37]:
                        self.state = 331
                        self.match(TyCParser.INC)
                        pass
                    elif token in [38]:
                        self.state = 332
                        self.match(TyCParser.DEC)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 337
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.COMMA)
            else:
                return self.getToken(TyCParser.COMMA, i)

        def getRuleIndex(self):
            return TyCParser.RULE_listExpr




    def listExpr(self):

        localctx = TyCParser.ListExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_listExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.expr()
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 339
                self.match(TyCParser.COMMA)
                self.state = 340
                self.expr()
                self.state = 345
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(TyCParser.LiteralContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_primary




    def primary(self):

        localctx = TyCParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_primary)
        try:
            self.state = 352
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 52, 54, 55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.literal()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.match(TyCParser.ID)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 3)
                self.state = 348
                self.match(TyCParser.LPAREN)
                self.state = 349
                self.expr()
                self.state = 350
                self.match(TyCParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(TyCParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(TyCParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(TyCParser.STRINGLIT, 0)

        def TRUE(self):
            return self.getToken(TyCParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(TyCParser.FALSE, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_literal




    def literal(self):

        localctx = TyCParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58546795158962176) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TyCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(TyCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(TyCParser.STRING, 0)

        def BOOL(self):
            return self.getToken(TyCParser.BOOL, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_type




    def type_(self):

        localctx = TyCParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 9007199258977280) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[21] = self.logicOrExpr_sempred
        self._predicates[22] = self.andExpr_sempred
        self._predicates[23] = self.eqExpr_sempred
        self._predicates[24] = self.relExpr_sempred
        self._predicates[25] = self.addExpr_sempred
        self._predicates[26] = self.mulExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logicOrExpr_sempred(self, localctx:LogicOrExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def andExpr_sempred(self, localctx:AndExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def eqExpr_sempred(self, localctx:EqExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def relExpr_sempred(self, localctx:RelExprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def addExpr_sempred(self, localctx:AddExprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def mulExpr_sempred(self, localctx:MulExprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




