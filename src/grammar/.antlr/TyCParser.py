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
        4,1,47,236,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,5,0,52,8,0,10,0,
        12,0,55,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,68,8,
        1,1,2,1,2,1,3,1,3,1,3,1,3,3,3,76,8,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,
        84,8,4,10,4,12,4,87,9,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,95,8,5,10,5,
        12,5,98,9,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,106,8,6,10,6,12,6,109,9,
        6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,117,8,7,10,7,12,7,120,9,7,1,8,1,8,
        1,8,1,8,1,8,1,8,5,8,128,8,8,10,8,12,8,131,9,8,1,9,1,9,1,9,1,9,1,
        9,1,9,5,9,139,8,9,10,9,12,9,142,9,9,1,10,1,10,1,10,3,10,147,8,10,
        1,11,1,11,1,11,1,11,1,11,1,11,3,11,155,8,11,1,12,1,12,1,13,1,13,
        1,14,1,14,1,14,1,14,1,15,1,15,1,15,5,15,168,8,15,10,15,12,15,171,
        9,15,1,16,1,16,1,16,1,16,3,16,177,8,16,1,17,1,17,5,17,181,8,17,10,
        17,12,17,184,9,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,
        18,195,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,3,21,215,8,21,1,22,1,22,3,
        22,219,8,22,1,23,1,23,3,23,223,8,23,1,24,1,24,1,24,1,24,1,24,1,24,
        3,24,231,8,24,1,24,3,24,234,8,24,1,24,0,6,8,10,12,14,16,18,25,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,0,7,1,0,21,22,2,0,23,24,28,29,1,0,31,32,1,0,33,35,2,0,30,30,32,
        32,3,0,16,17,19,20,46,46,1,0,11,14,237,0,53,1,0,0,0,2,67,1,0,0,0,
        4,69,1,0,0,0,6,75,1,0,0,0,8,77,1,0,0,0,10,88,1,0,0,0,12,99,1,0,0,
        0,14,110,1,0,0,0,16,121,1,0,0,0,18,132,1,0,0,0,20,146,1,0,0,0,22,
        154,1,0,0,0,24,156,1,0,0,0,26,158,1,0,0,0,28,160,1,0,0,0,30,164,
        1,0,0,0,32,176,1,0,0,0,34,178,1,0,0,0,36,187,1,0,0,0,38,196,1,0,
        0,0,40,202,1,0,0,0,42,214,1,0,0,0,44,218,1,0,0,0,46,222,1,0,0,0,
        48,233,1,0,0,0,50,52,3,2,1,0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,
        0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,53,1,0,0,0,56,57,5,0,0,1,57,
        1,1,0,0,0,58,68,3,28,14,0,59,60,3,4,2,0,60,61,5,42,0,0,61,68,1,0,
        0,0,62,68,3,34,17,0,63,68,3,36,18,0,64,68,3,38,19,0,65,68,3,40,20,
        0,66,68,3,48,24,0,67,58,1,0,0,0,67,59,1,0,0,0,67,62,1,0,0,0,67,63,
        1,0,0,0,67,64,1,0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,68,3,1,0,0,0,69,
        70,3,6,3,0,70,5,1,0,0,0,71,76,3,8,4,0,72,73,5,18,0,0,73,74,5,27,
        0,0,74,76,3,6,3,0,75,71,1,0,0,0,75,72,1,0,0,0,76,7,1,0,0,0,77,78,
        6,4,-1,0,78,79,3,10,5,0,79,85,1,0,0,0,80,81,10,2,0,0,81,82,5,26,
        0,0,82,84,3,10,5,0,83,80,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,
        86,1,0,0,0,86,9,1,0,0,0,87,85,1,0,0,0,88,89,6,5,-1,0,89,90,3,12,
        6,0,90,96,1,0,0,0,91,92,10,2,0,0,92,93,5,25,0,0,93,95,3,12,6,0,94,
        91,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,11,1,0,0,
        0,98,96,1,0,0,0,99,100,6,6,-1,0,100,101,3,14,7,0,101,107,1,0,0,0,
        102,103,10,2,0,0,103,104,7,0,0,0,104,106,3,14,7,0,105,102,1,0,0,
        0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,13,1,0,0,0,
        109,107,1,0,0,0,110,111,6,7,-1,0,111,112,3,16,8,0,112,118,1,0,0,
        0,113,114,10,2,0,0,114,115,7,1,0,0,115,117,3,16,8,0,116,113,1,0,
        0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,15,1,0,0,
        0,120,118,1,0,0,0,121,122,6,8,-1,0,122,123,3,18,9,0,123,129,1,0,
        0,0,124,125,10,2,0,0,125,126,7,2,0,0,126,128,3,18,9,0,127,124,1,
        0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,17,1,0,
        0,0,131,129,1,0,0,0,132,133,6,9,-1,0,133,134,3,20,10,0,134,140,1,
        0,0,0,135,136,10,2,0,0,136,137,7,3,0,0,137,139,3,20,10,0,138,135,
        1,0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,19,1,
        0,0,0,142,140,1,0,0,0,143,144,7,4,0,0,144,147,3,20,10,0,145,147,
        3,22,11,0,146,143,1,0,0,0,146,145,1,0,0,0,147,21,1,0,0,0,148,155,
        3,24,12,0,149,155,5,18,0,0,150,151,5,36,0,0,151,152,3,4,2,0,152,
        153,5,37,0,0,153,155,1,0,0,0,154,148,1,0,0,0,154,149,1,0,0,0,154,
        150,1,0,0,0,155,23,1,0,0,0,156,157,7,5,0,0,157,25,1,0,0,0,158,159,
        7,6,0,0,159,27,1,0,0,0,160,161,3,26,13,0,161,162,3,30,15,0,162,163,
        5,42,0,0,163,29,1,0,0,0,164,169,3,32,16,0,165,166,5,43,0,0,166,168,
        3,32,16,0,167,165,1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,169,170,
        1,0,0,0,170,31,1,0,0,0,171,169,1,0,0,0,172,177,5,18,0,0,173,174,
        5,18,0,0,174,175,5,27,0,0,175,177,3,4,2,0,176,172,1,0,0,0,176,173,
        1,0,0,0,177,33,1,0,0,0,178,182,5,38,0,0,179,181,3,2,1,0,180,179,
        1,0,0,0,181,184,1,0,0,0,182,180,1,0,0,0,182,183,1,0,0,0,183,185,
        1,0,0,0,184,182,1,0,0,0,185,186,5,39,0,0,186,35,1,0,0,0,187,188,
        5,4,0,0,188,189,5,36,0,0,189,190,3,4,2,0,190,191,5,37,0,0,191,194,
        3,2,1,0,192,193,5,5,0,0,193,195,3,2,1,0,194,192,1,0,0,0,194,195,
        1,0,0,0,195,37,1,0,0,0,196,197,5,6,0,0,197,198,5,36,0,0,198,199,
        3,4,2,0,199,200,5,37,0,0,200,201,3,2,1,0,201,39,1,0,0,0,202,203,
        5,7,0,0,203,204,5,36,0,0,204,205,3,42,21,0,205,206,5,42,0,0,206,
        207,3,44,22,0,207,208,5,42,0,0,208,209,3,46,23,0,209,210,5,37,0,
        0,210,211,3,2,1,0,211,41,1,0,0,0,212,215,3,4,2,0,213,215,1,0,0,0,
        214,212,1,0,0,0,214,213,1,0,0,0,215,43,1,0,0,0,216,219,3,4,2,0,217,
        219,1,0,0,0,218,216,1,0,0,0,218,217,1,0,0,0,219,45,1,0,0,0,220,223,
        3,4,2,0,221,223,1,0,0,0,222,220,1,0,0,0,222,221,1,0,0,0,223,47,1,
        0,0,0,224,225,5,8,0,0,225,234,5,42,0,0,226,227,5,9,0,0,227,234,5,
        42,0,0,228,230,5,10,0,0,229,231,3,4,2,0,230,229,1,0,0,0,230,231,
        1,0,0,0,231,232,1,0,0,0,232,234,5,42,0,0,233,224,1,0,0,0,233,226,
        1,0,0,0,233,228,1,0,0,0,234,49,1,0,0,0,20,53,67,75,85,96,107,118,
        129,140,146,154,169,176,182,194,214,218,222,230,233
    ]

class TyCParser ( Parser ):

    grammarFileName = "TyC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'if'", "'else'", "'while'", "'for'", "'break'", "'continue'", 
                     "'return'", "'int'", "'float'", "'bool'", "'string'", 
                     "'void'", "'true'", "'false'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'=='", "'!='", "'<='", "'>='", "'&&'", 
                     "'||'", "'='", "'<'", "'>'", "'!'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "','" ]

    symbolicNames = [ "<INVALID>", "WS", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "IF", "ELSE", "WHILE", "FOR", "BREAK", "CONTINUE", 
                      "RETURN", "INT", "FLOAT", "BOOL", "STRING", "VOID", 
                      "TRUE", "FALSE", "ID", "FLOATLIT", "INTLIT", "EQ", 
                      "NEQ", "LE", "GE", "AND", "OR", "ASSIGN", "LT", "GT", 
                      "NOT", "ADD", "SUB", "MUL", "DIV", "MOD", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                      "SEMI", "COMMA", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "STRINGLIT", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_stmt = 1
    RULE_expr = 2
    RULE_assignExpr = 3
    RULE_logicOrExpr = 4
    RULE_andExpr = 5
    RULE_eqExpr = 6
    RULE_relExpr = 7
    RULE_addExpr = 8
    RULE_mulExpr = 9
    RULE_unaryExpr = 10
    RULE_primary = 11
    RULE_literal = 12
    RULE_type = 13
    RULE_decl = 14
    RULE_idList = 15
    RULE_idItem = 16
    RULE_block = 17
    RULE_if_stmt = 18
    RULE_whileStmt = 19
    RULE_forStmt = 20
    RULE_forInit = 21
    RULE_forCond = 22
    RULE_forUpdate = 23
    RULE_jumpStmt = 24

    ruleNames =  [ "program", "stmt", "expr", "assignExpr", "logicOrExpr", 
                   "andExpr", "eqExpr", "relExpr", "addExpr", "mulExpr", 
                   "unaryExpr", "primary", "literal", "type", "decl", "idList", 
                   "idItem", "block", "if_stmt", "whileStmt", "forStmt", 
                   "forInit", "forCond", "forUpdate", "jumpStmt" ]

    EOF = Token.EOF
    WS=1
    LINE_COMMENT=2
    BLOCK_COMMENT=3
    IF=4
    ELSE=5
    WHILE=6
    FOR=7
    BREAK=8
    CONTINUE=9
    RETURN=10
    INT=11
    FLOAT=12
    BOOL=13
    STRING=14
    VOID=15
    TRUE=16
    FALSE=17
    ID=18
    FLOATLIT=19
    INTLIT=20
    EQ=21
    NEQ=22
    LE=23
    GE=24
    AND=25
    OR=26
    ASSIGN=27
    LT=28
    GT=29
    NOT=30
    ADD=31
    SUB=32
    MUL=33
    DIV=34
    MOD=35
    LPAREN=36
    RPAREN=37
    LBRACE=38
    RBRACE=39
    LBRACK=40
    RBRACK=41
    SEMI=42
    COMMA=43
    ILLEGAL_ESCAPE=44
    UNCLOSE_STRING=45
    STRINGLIT=46
    ERROR_CHAR=47

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

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.StmtContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_program




    def program(self):

        localctx = TyCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70717712334800) != 0):
                self.state = 50
                self.stmt()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.match(TyCParser.EOF)
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

        def decl(self):
            return self.getTypedRuleContext(TyCParser.DeclContext,0)


        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def block(self):
            return self.getTypedRuleContext(TyCParser.BlockContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(TyCParser.If_stmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(TyCParser.WhileStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(TyCParser.ForStmtContext,0)


        def jumpStmt(self):
            return self.getTypedRuleContext(TyCParser.JumpStmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_stmt




    def stmt(self):

        localctx = TyCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.decl()
                pass
            elif token in [16, 17, 18, 19, 20, 30, 32, 36, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.expr()
                self.state = 60
                self.match(TyCParser.SEMI)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.block()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.if_stmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                self.whileStmt()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 6)
                self.state = 65
                self.forStmt()
                pass
            elif token in [8, 9, 10]:
                self.enterOuterAlt(localctx, 7)
                self.state = 66
                self.jumpStmt()
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
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
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
        self.enterRule(localctx, 6, self.RULE_assignExpr)
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.logicOrExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(TyCParser.ID)
                self.state = 73
                self.match(TyCParser.ASSIGN)
                self.state = 74
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
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_logicOrExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.andExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.LogicOrExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicOrExpr)
                    self.state = 80
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 81
                    self.match(TyCParser.OR)
                    self.state = 82
                    self.andExpr(0) 
                self.state = 87
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_andExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.eqExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.AndExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_andExpr)
                    self.state = 91
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 92
                    self.match(TyCParser.AND)
                    self.state = 93
                    self.eqExpr(0) 
                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_eqExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.relExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.EqExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_eqExpr)
                    self.state = 102
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 103
                    _la = self._input.LA(1)
                    if not(_la==21 or _la==22):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 104
                    self.relExpr(0) 
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_relExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.addExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.RelExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relExpr)
                    self.state = 113
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 114
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 830472192) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 115
                    self.addExpr(0) 
                self.state = 120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_addExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.mulExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 129
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.AddExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_addExpr)
                    self.state = 124
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 125
                    _la = self._input.LA(1)
                    if not(_la==31 or _la==32):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 126
                    self.mulExpr(0) 
                self.state = 131
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_mulExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.unaryExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 140
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.MulExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                    self.state = 135
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 136
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60129542144) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 137
                    self.unaryExpr() 
                self.state = 142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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

        def primary(self):
            return self.getTypedRuleContext(TyCParser.PrimaryContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_unaryExpr




    def unaryExpr(self):

        localctx = TyCParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                _la = self._input.LA(1)
                if not(_la==30 or _la==32):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 144
                self.unaryExpr()
                pass
            elif token in [16, 17, 18, 19, 20, 36, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.primary()
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
        self.enterRule(localctx, 22, self.RULE_primary)
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17, 19, 20, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.literal()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(TyCParser.ID)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.match(TyCParser.LPAREN)
                self.state = 151
                self.expr()
                self.state = 152
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
        self.enterRule(localctx, 24, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 70368745947136) != 0)):
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

        def BOOL(self):
            return self.getToken(TyCParser.BOOL, 0)

        def STRING(self):
            return self.getToken(TyCParser.STRING, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_type




    def type_(self):

        localctx = TyCParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0)):
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


    class DeclContext(ParserRuleContext):
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

        def getRuleIndex(self):
            return TyCParser.RULE_decl




    def decl(self):

        localctx = TyCParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.type_()
            self.state = 161
            self.idList()
            self.state = 162
            self.match(TyCParser.SEMI)
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
        self.enterRule(localctx, 30, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.idItem()
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 165
                self.match(TyCParser.COMMA)
                self.state = 166
                self.idItem()
                self.state = 171
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
        self.enterRule(localctx, 32, self.RULE_idItem)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(TyCParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(TyCParser.ID)
                self.state = 174
                self.match(TyCParser.ASSIGN)
                self.state = 175
                self.expr()
                pass


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
        self.enterRule(localctx, 34, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(TyCParser.LBRACE)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70717712334800) != 0):
                self.state = 179
                self.stmt()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 185
            self.match(TyCParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
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
            return TyCParser.RULE_if_stmt




    def if_stmt(self):

        localctx = TyCParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(TyCParser.IF)
            self.state = 188
            self.match(TyCParser.LPAREN)
            self.state = 189
            self.expr()
            self.state = 190
            self.match(TyCParser.RPAREN)
            self.state = 191
            self.stmt()
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 192
                self.match(TyCParser.ELSE)
                self.state = 193
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
        self.enterRule(localctx, 38, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(TyCParser.WHILE)
            self.state = 197
            self.match(TyCParser.LPAREN)
            self.state = 198
            self.expr()
            self.state = 199
            self.match(TyCParser.RPAREN)
            self.state = 200
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

        def forInit(self):
            return self.getTypedRuleContext(TyCParser.ForInitContext,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.SEMI)
            else:
                return self.getToken(TyCParser.SEMI, i)

        def forCond(self):
            return self.getTypedRuleContext(TyCParser.ForCondContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(TyCParser.ForUpdateContext,0)


        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def stmt(self):
            return self.getTypedRuleContext(TyCParser.StmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_forStmt




    def forStmt(self):

        localctx = TyCParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(TyCParser.FOR)
            self.state = 203
            self.match(TyCParser.LPAREN)
            self.state = 204
            self.forInit()
            self.state = 205
            self.match(TyCParser.SEMI)
            self.state = 206
            self.forCond()
            self.state = 207
            self.match(TyCParser.SEMI)
            self.state = 208
            self.forUpdate()
            self.state = 209
            self.match(TyCParser.RPAREN)
            self.state = 210
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_forInit




    def forInit(self):

        localctx = TyCParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_forInit)
        try:
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17, 18, 19, 20, 30, 32, 36, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.expr()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)

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


    class ForCondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_forCond




    def forCond(self):

        localctx = TyCParser.ForCondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_forCond)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17, 18, 19, 20, 30, 32, 36, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.expr()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)

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


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_forUpdate




    def forUpdate(self):

        localctx = TyCParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_forUpdate)
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17, 18, 19, 20, 30, 32, 36, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.expr()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)

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
        self.enterRule(localctx, 48, self.RULE_jumpStmt)
        self._la = 0 # Token type
        try:
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(TyCParser.BREAK)
                self.state = 225
                self.match(TyCParser.SEMI)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(TyCParser.CONTINUE)
                self.state = 227
                self.match(TyCParser.SEMI)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
                self.match(TyCParser.RETURN)
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 70442834395136) != 0):
                    self.state = 229
                    self.expr()


                self.state = 232
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.logicOrExpr_sempred
        self._predicates[5] = self.andExpr_sempred
        self._predicates[6] = self.eqExpr_sempred
        self._predicates[7] = self.relExpr_sempred
        self._predicates[8] = self.addExpr_sempred
        self._predicates[9] = self.mulExpr_sempred
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
         




