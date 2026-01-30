"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer
from src.grammar.lexererr import ErrorToken, LexerError
from tests.utils import Tokenizer


"""ID TESTS"""

def test_id_01():
    source = "abc"
    expected = "ID,abc,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_id_02():
    source = "a1"
    expected = "ID,a1,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_id_03():
    source = "abc123"
    expected = "ID,abc123,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_id_04():
    source = "A"
    expected = "ID,A,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_id_05():
    source = "_abc"
    expected = "ID,_abc,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_id_06():
    source = "abc_1"
    expected = "ID,abc_1,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_id_07():
    source = "aBc"
    expected = "ID,aBc,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_id_08():
    source = "aaBC"
    expected = "ID,aaBC,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_id_09():
    source = "_"
    expected = "ID,_,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_id_10():
    source = "_X_x"
    expected = "ID,_X_x,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_id_11():
    source = "a1b2c3"
    expected = "ID,a1b2c3,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_id_12():
    source = "_123"
    expected = "ID,_123,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_id_13():
    source = "abc_def"
    expected = "ID,abc_def,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_id_14():
    source = "a_1_b_2"
    expected = "ID,a_1_b_2,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_id_15():
    source = "abca123456789012345"
    expected = "ID,abca123456789012345,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_id_16():
    source = "abcdefghijklmnopqrstuvwxyz"
    expected = "ID,abcdefghijklmnopqrstuvwxyz,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_id_17():
    source = "a"
    expected = "ID,a,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_id_18():
    source = "abc123"
    expected = "ID,abc123,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_id_19():
    source = "_a_b_c"
    expected = "ID,_a_b_c,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected  

def test_id_20():
    source = "aAbB1cD2"
    expected = "ID,aAbB1cD2,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected  


"""NUMBER LITERAL TESTS"""

def test_int_01():
    assert Tokenizer("0").get_tokens_as_string() == "INTLIT,0,EOF"

def test_int_02():
    assert Tokenizer("123").get_tokens_as_string() == "INTLIT,123,EOF"

def test_int_03():
    assert Tokenizer("00123").get_tokens_as_string() == "INTLIT,00123,EOF"

def test_int_04():
    assert Tokenizer("1 2").get_tokens_as_string() == "INTLIT,1,INTLIT,2,EOF"

def test_int_05():
    assert Tokenizer("123abc").get_tokens_as_string() == "INTLIT,123,ID,abc,EOF"

def test_int_06():
    assert Tokenizer("1e").get_tokens_as_string() == "INTLIT,1,ID,e,EOF"

def test_int_07():
    assert Tokenizer("1 2 3").get_tokens_as_string() == "INTLIT,1,INTLIT,2,INTLIT,3,EOF"

def test_int_08():
    assert Tokenizer("1A2B3C").get_tokens_as_string() == "INTLIT,1,ID,A2B3C,EOF"

def test_int_09():
    assert Tokenizer("1010101").get_tokens_as_string() == "INTLIT,1010101,EOF"

def test_int_10():
    assert Tokenizer("12_A34_B").get_tokens_as_string() == "INTLIT,12,ID,_A34_B,EOF"



def test_float_01():
    assert Tokenizer("1.0").get_tokens_as_string() == "FLOATLIT,1.0,EOF"

def test_float_02():
    assert Tokenizer("0.0").get_tokens_as_string() == "FLOATLIT,0.0,EOF"

def test_float_03():
    assert Tokenizer("1.").get_tokens_as_string() == "FLOATLIT,1.,EOF"

def test_float_04():
    assert Tokenizer(".5").get_tokens_as_string() == "FLOATLIT,.5,EOF"

def test_float_05():
    assert Tokenizer("1.2abc").get_tokens_as_string() == "FLOATLIT,1.2,ID,abc,EOF"

def test_float_06():
    assert Tokenizer("1e4").get_tokens_as_string() == "FLOATLIT,1e4,EOF"

def test_float_07():
    assert Tokenizer("0.23_abc").get_tokens_as_string() == "FLOATLIT,0.23,ID,_abc,EOF"

def test_float_08():
    assert Tokenizer("0.1_a_b_c").get_tokens_as_string() == "FLOATLIT,0.1,ID,_a_b_c,EOF"

def test_float_09():
    assert Tokenizer("2E-3").get_tokens_as_string() == "FLOATLIT,2E-3,EOF"

def test_float_10():
    assert Tokenizer("5.67E-2").get_tokens_as_string() == "FLOATLIT,5.67E-2,EOF"


"""STRING TESTS"""

def test_string_01():
    assert Tokenizer('"abc"').get_tokens_as_string() == "STRINGLIT,abc,EOF"

def test_string_02():
    assert Tokenizer('"aBcD"').get_tokens_as_string() == "STRINGLIT,aBcD,EOF"

def test_string_03():
    assert Tokenizer('"abc123"').get_tokens_as_string() == "STRINGLIT,abc123,EOF"

def test_string_04():
    assert Tokenizer('"a b c"').get_tokens_as_string() == "STRINGLIT,a b c,EOF"

def test_string_05():
    assert Tokenizer('"a\\n"').get_tokens_as_string() == "STRINGLIT,a\\n,EOF"

def test_string_06():
    assert Tokenizer('"abc\\t"').get_tokens_as_string() == "STRINGLIT,abc\\t,EOF"

def test_string_07():
    assert Tokenizer('"aB\\b"').get_tokens_as_string() == "STRINGLIT,aB\\b,EOF"

def test_string_08():
    assert Tokenizer('"aB\\\"c"').get_tokens_as_string() == "STRINGLIT,aB\\\"c,EOF"

def test_string_09():
    assert Tokenizer('"123_a45"').get_tokens_as_string() == "STRINGLIT,123_a45,EOF"

def test_string_10():
    assert Tokenizer('"a\\\\b"').get_tokens_as_string() == "STRINGLIT,a\\\\b,EOF"

def test_unclose_01():
    with pytest.raises(Exception):
        Tokenizer('"abc').get_tokens_as_string()

def test_unclose_02():
    with pytest.raises(Exception):
        Tokenizer('"ab\\n').get_tokens_as_string()

def test_unclose_03():
    with pytest.raises(Exception):
        Tokenizer('"abc\n').get_tokens_as_string()

def test_unclose_04():
    with pytest.raises(Exception):
        Tokenizer('"ab\\t\n').get_tokens_as_string()

def test_unclose_05():
    with pytest.raises(Exception):
        Tokenizer('"ab123\\t\n').get_tokens_as_string()

def test_illegal_01():
    with pytest.raises(Exception):
        Tokenizer('"abc\\q"').get_tokens_as_string()

def test_illegal_02():
    with pytest.raises(Exception):
        Tokenizer('"ab\\tcd\\z"').get_tokens_as_string()

def test_illegal_03():
    with pytest.raises(Exception):
        Tokenizer('"abc\\x').get_tokens_as_string()

def test_illegal_04():
    with pytest.raises(Exception):
        Tokenizer('"a1b2c3\\x').get_tokens_as_string()

def test_illegal_05():
    with pytest.raises(Exception):
        Tokenizer('"a_Bb_c\\x').get_tokens_as_string()


"""OPERATOR,SEPERATOR,COMMENT,ERROR_TOKEN TESTS"""

def test_op_01():
    assert Tokenizer("+").get_tokens_as_string() == "ADD,+,EOF"

def test_op_02():
    assert Tokenizer("==").get_tokens_as_string() == "EQ,==,EOF"

def test_op_03():
    assert Tokenizer("=").get_tokens_as_string() == "ASSIGN,=,EOF"

def test_op_04():
    assert Tokenizer("!=").get_tokens_as_string() == "NEQ,!=,EOF"

def test_op_05():
    assert Tokenizer("a<=b").get_tokens_as_string() == \
        "ID,a,LE,<=,ID,b,EOF"

def test_op_06():
    assert Tokenizer("+").get_tokens_as_string() == "ADD,+,EOF"

def test_op_07():
    assert Tokenizer("-").get_tokens_as_string() == "SUB,-,EOF"

def test_op_08():
    assert Tokenizer("*").get_tokens_as_string() == "MUL,*,EOF"

def test_op_09():
    assert Tokenizer("/").get_tokens_as_string() == "DIV,/,EOF"

def test_op_10():
    assert Tokenizer("a+b").get_tokens_as_string() == "ID,a,ADD,+,ID,b,EOF"
    
def test_sep_01():
    assert Tokenizer("(a)").get_tokens_as_string() == \
        "LPAREN,(,ID,a,RPAREN,),EOF"

def test_sep_02():
    assert Tokenizer("(a,b)").get_tokens_as_string() == \
        "LPAREN,(,ID,a,COMMA,,,ID,b,RPAREN,),EOF"

def test_sep_03():
    assert Tokenizer("{a}").get_tokens_as_string() == \
        "LBRACE,{,ID,a,RBRACE,},EOF"

def test_sep_04():
    assert Tokenizer("a;").get_tokens_as_string() == \
        "ID,a,SEMI,;,EOF"

def test_sep_05():
    assert Tokenizer("a,b,c").get_tokens_as_string() == \
        "ID,a,COMMA,,,ID,b,COMMA,,,ID,c,EOF"

def test_sep_06():
    assert Tokenizer("()").get_tokens_as_string() == \
        "LPAREN,(,RPAREN,),EOF"

def test_sep_07():
    assert Tokenizer("{}").get_tokens_as_string() == \
        "LBRACE,{,RBRACE,},EOF"

def test_sep_08():
    assert Tokenizer("(a,{b})").get_tokens_as_string() == \
        "LPAREN,(,ID,a,COMMA,,,LBRACE,{,ID,b,RBRACE,},RPAREN,),EOF"

def test_sep_09():
    assert Tokenizer("(a,(b,c))").get_tokens_as_string() == \
        "LPAREN,(,ID,a,COMMA,,,LPAREN,(,ID,b,COMMA,,,ID,c,RPAREN,),RPAREN,),EOF"

def test_sep_10():
    assert Tokenizer("(a,b)").get_tokens_as_string() == \
        "LPAREN,(,ID,a,COMMA,,,ID,b,RPAREN,),EOF"
    
def test_comment_01():
    assert Tokenizer("// comment").get_tokens_as_string() == "EOF"

def test_comment_02():
    assert Tokenizer("a // comment").get_tokens_as_string() == "ID,a,EOF"

def test_comment_03():
    assert Tokenizer("// comment\n").get_tokens_as_string() == "EOF"

def test_comment_04():
    assert Tokenizer("/* comment */").get_tokens_as_string() == "EOF"

def test_comment_05():
    assert Tokenizer("a/*cmt*/b").get_tokens_as_string() == "ID,a,ID,b,EOF"

def test_comment_06():
    assert Tokenizer("/* comment */a").get_tokens_as_string() == "ID,a,EOF"

def test_comment_07():
    assert Tokenizer("a // hello").get_tokens_as_string() == "ID,a,EOF"

def test_error_token_01():
    with pytest.raises(Exception):
        Tokenizer("@").get_tokens_as_string()

def test_error_token_02():
    with pytest.raises(Exception):
        Tokenizer("#").get_tokens_as_string()

def test_error_token_03():
    with pytest.raises(Exception):
        Tokenizer("$").get_tokens_as_string()

def test_error_token_04():
    with pytest.raises(Exception):
        Tokenizer("a@b").get_tokens_as_string()

def test_error_token_05():
    with pytest.raises(Exception):
        Tokenizer("%$").get_tokens_as_string()

def test_error_token_06():
    with pytest.raises(Exception):
        Tokenizer("@").get_tokens_as_string()

def test_mix_01():
    assert Tokenizer("a+1").get_tokens_as_string() == "ID,a,ADD,+,INTLIT,1,EOF"

def test_mix_02():
    assert Tokenizer("x=1.2").get_tokens_as_string() == "ID,x,ASSIGN,=,FLOATLIT,1.2,EOF"

def test_mix_03():
    assert Tokenizer("foo(bar,3)").get_tokens_as_string() == \
        "ID,foo,LPAREN,(,ID,bar,COMMA,,,INTLIT,3,RPAREN,),EOF"

def test_mix_04():
    assert Tokenizer("(a+b)*c").get_tokens_as_string() == \
        "LPAREN,(,ID,a,ADD,+,ID,b,RPAREN,),MUL,*,ID,c,EOF"

def test_mix_05():
    assert Tokenizer("(a,b+c,d)").get_tokens_as_string() == \
        "LPAREN,(,ID,a,COMMA,,,ID,b,ADD,+,ID,c,COMMA,,,ID,d,RPAREN,),EOF"

def test_mix_06():
    assert Tokenizer("a+b // comment").get_tokens_as_string() == \
        "ID,a,ADD,+,ID,b,EOF"

def test_mix_07():
    assert Tokenizer("(\"abc\",a+1)").get_tokens_as_string() == \
        "LPAREN,(,STRINGLIT,abc,COMMA,,,ID,a,ADD,+,INTLIT,1,RPAREN,),EOF"
