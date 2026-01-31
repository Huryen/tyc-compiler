"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

"""
Lexer test cases for TyC compiler
Implemented ~100 test cases covering all token types and error scenarios.
"""

import pytest
from tests.utils import Tokenizer

def test_kw_auto():
    assert Tokenizer("auto").get_tokens_as_string() == "auto,<EOF>"

def test_kw_break():
    assert Tokenizer("break").get_tokens_as_string() == "break,<EOF>"

def test_kw_case():
    assert Tokenizer("case").get_tokens_as_string() == "case,<EOF>"

def test_kw_continue():
    assert Tokenizer("continue").get_tokens_as_string() == "continue,<EOF>"

def test_kw_default():
    assert Tokenizer("default").get_tokens_as_string() == "default,<EOF>"

def test_kw_else():
    assert Tokenizer("else").get_tokens_as_string() == "else,<EOF>"

def test_kw_float():
    assert Tokenizer("float").get_tokens_as_string() == "float,<EOF>"

def test_kw_for():
    assert Tokenizer("for").get_tokens_as_string() == "for,<EOF>"

def test_kw_if():
    assert Tokenizer("if").get_tokens_as_string() == "if,<EOF>"

def test_kw_int():
    assert Tokenizer("int").get_tokens_as_string() == "int,<EOF>"

def test_kw_return():
    assert Tokenizer("return").get_tokens_as_string() == "return,<EOF>"

def test_kw_string():
    assert Tokenizer("string").get_tokens_as_string() == "string,<EOF>"

def test_kw_struct():
    assert Tokenizer("struct").get_tokens_as_string() == "struct,<EOF>"

def test_kw_switch():
    assert Tokenizer("switch").get_tokens_as_string() == "switch,<EOF>"

def test_kw_void():
    assert Tokenizer("void").get_tokens_as_string() == "void,<EOF>"

def test_kw_while():
    assert Tokenizer("while").get_tokens_as_string() == "while,<EOF>"

def test_kw_true():
    assert Tokenizer("true").get_tokens_as_string() == "true,<EOF>"

def test_kw_false():
    assert Tokenizer("false").get_tokens_as_string() == "false,<EOF>"

def test_kw_bool():
    assert Tokenizer("bool").get_tokens_as_string() == "bool,<EOF>"

def test_kw_mixed():
    assert Tokenizer("int auto void").get_tokens_as_string() == "int,auto,void,<EOF>"



def test_op_add():
    assert Tokenizer("+").get_tokens_as_string() == "+,<EOF>"

def test_op_sub():
    assert Tokenizer("-").get_tokens_as_string() == "-,<EOF>"

def test_op_mul():
    assert Tokenizer("*").get_tokens_as_string() == "*,<EOF>"

def test_op_div():
    assert Tokenizer("/").get_tokens_as_string() == "/,<EOF>"

def test_op_mod():
    assert Tokenizer("%").get_tokens_as_string() == "%,<EOF>"

def test_op_eq():
    assert Tokenizer("==").get_tokens_as_string() == "==,<EOF>"

def test_op_neq():
    assert Tokenizer("!=").get_tokens_as_string() == "!=,<EOF>"

def test_op_lt():
    assert Tokenizer("<").get_tokens_as_string() == "<,<EOF>"

def test_op_gt():
    assert Tokenizer(">").get_tokens_as_string() == ">,<EOF>"

def test_op_le():
    assert Tokenizer("<=").get_tokens_as_string() == "<=,<EOF>"

def test_op_ge():
    assert Tokenizer(">=").get_tokens_as_string() == ">=,<EOF>"

def test_op_assign():
    assert Tokenizer("=").get_tokens_as_string() == "=,<EOF>"

def test_op_not():
    assert Tokenizer("!").get_tokens_as_string() == "!,<EOF>"

def test_op_and():
    assert Tokenizer("&&").get_tokens_as_string() == "&&,<EOF>"

def test_op_or():
    assert Tokenizer("||").get_tokens_as_string() == "||,<EOF>"

def test_op_inc():
    assert Tokenizer("++").get_tokens_as_string() == "++,<EOF>"

def test_op_dec():
    assert Tokenizer("--").get_tokens_as_string() == "--,<EOF>"

def test_op_dot():
    assert Tokenizer(".").get_tokens_as_string() == ".,<EOF>"

def test_op_complex_1():
    assert Tokenizer("<= >= == !=").get_tokens_as_string() == "<=,>=,==,!=,<EOF>"

def test_op_complex_2():
    assert Tokenizer("+++").get_tokens_as_string() == "++,+,<EOF>"



def test_sep_lparen():
    assert Tokenizer("(").get_tokens_as_string() == "(,<EOF>"

def test_sep_rparen():
    assert Tokenizer(")").get_tokens_as_string() == "),<EOF>"

def test_sep_lbrace():
    assert Tokenizer("{").get_tokens_as_string() == "{,<EOF>"

def test_sep_rbrace():
    assert Tokenizer("}").get_tokens_as_string() == "},<EOF>"

def test_sep_lbrack():
    assert Tokenizer("[").get_tokens_as_string() == "[,<EOF>"

def test_sep_rbrack():
    assert Tokenizer("]").get_tokens_as_string() == "],<EOF>"

def test_sep_semi():
    assert Tokenizer(";").get_tokens_as_string() == ";,<EOF>"

def test_sep_comma():
    assert Tokenizer(",").get_tokens_as_string() == ",,<EOF>"

def test_sep_colon():
    assert Tokenizer(":").get_tokens_as_string() == ":,<EOF>"

def test_sep_mixed():
    assert Tokenizer("{[()]}").get_tokens_as_string() == "{,[,(,),],},<EOF>"



def test_id_simple():
    assert Tokenizer("x").get_tokens_as_string() == "x,<EOF>"

def test_id_caps():
    assert Tokenizer("MyVar").get_tokens_as_string() == "MyVar,<EOF>"

def test_id_with_num():
    assert Tokenizer("var123").get_tokens_as_string() == "var123,<EOF>"

def test_id_underscore_start():
    assert Tokenizer("_temp").get_tokens_as_string() == "_temp,<EOF>"

def test_id_all_caps():
    assert Tokenizer("MAX_SIZE").get_tokens_as_string() == "MAX_SIZE,<EOF>"

def test_id_keyword_prefix():
    assert Tokenizer("autoVar").get_tokens_as_string() == "autoVar,<EOF>"

def test_id_mixed_case():
    assert Tokenizer("iNt").get_tokens_as_string() == "iNt,<EOF>"

def test_id_underscore_only():
    assert Tokenizer("_").get_tokens_as_string() == "_,<EOF>"

def test_id_sequence():
    assert Tokenizer("a b c").get_tokens_as_string() == "a,b,c,<EOF>"

def test_id_not_literal():
    assert Tokenizer("trueValue").get_tokens_as_string() == "trueValue,<EOF>"


def test_int_zero():
    assert Tokenizer("0").get_tokens_as_string() == "0,<EOF>"

def test_int_positive():
    assert Tokenizer("123").get_tokens_as_string() == "123,<EOF>"

def test_int_long():
    assert Tokenizer("1234567890").get_tokens_as_string() == "1234567890,<EOF>"

def test_float_simple():
    assert Tokenizer("1.23").get_tokens_as_string() == "1.23,<EOF>"

def test_float_start_dot():
    assert Tokenizer(".5").get_tokens_as_string() == ".5,<EOF>"

def test_float_scientific():
    assert Tokenizer("1e10").get_tokens_as_string() == "1e10,<EOF>"

def test_float_scientific_upper():
    assert Tokenizer("1E10").get_tokens_as_string() == "1E10,<EOF>"

def test_float_scientific_plus():
    assert Tokenizer("1.2e+3").get_tokens_as_string() == "1.2e+3,<EOF>"

def test_float_scientific_minus():
    assert Tokenizer("1.2e-3").get_tokens_as_string() == "1.2e-3,<EOF>"

def test_float_dot_scientific():
    assert Tokenizer(".5e-2").get_tokens_as_string() == ".5e-2,<EOF>"

def test_int_vs_float():
    assert Tokenizer("1 1.0").get_tokens_as_string() == "1,1.0,<EOF>"

def test_float_weird_1():
    assert Tokenizer("1.").get_tokens_as_string() == "1.,<EOF>" 

def test_float_weird_2():
    assert Tokenizer("1.e2").get_tokens_as_string() == "1.e2,<EOF>"

def test_num_sequence():
    assert Tokenizer("1 2.5 3").get_tokens_as_string() == "1,2.5,3,<EOF>"

def test_zero_float():
    assert Tokenizer("0.0").get_tokens_as_string() == "0.0,<EOF>"



def test_str_empty():
    assert Tokenizer('""').get_tokens_as_string() == ",<EOF>"

def test_str_simple():
    assert Tokenizer('"abc"').get_tokens_as_string() == "abc,<EOF>"

def test_str_space():
    assert Tokenizer('"a b c"').get_tokens_as_string() == "a b c,<EOF>"

def test_str_escape_quote():
    assert Tokenizer('"a\\"b"').get_tokens_as_string() == r"a\"b,<EOF>"

def test_str_escape_n():
    assert Tokenizer('"a\\nb"').get_tokens_as_string() == r"a\nb,<EOF>"

def test_str_escape_t():
    assert Tokenizer('"\\t"').get_tokens_as_string() == r"\t,<EOF>"

def test_str_escape_backslash():
    assert Tokenizer('"\\\\"').get_tokens_as_string() == r"\\,<EOF>"

def test_str_with_keywords():
    assert Tokenizer('"if else"').get_tokens_as_string() == "if else,<EOF>"

def test_str_with_ops():
    assert Tokenizer('"a+b"').get_tokens_as_string() == "a+b,<EOF>"

def test_str_multiple():
    assert Tokenizer('"hi" "there"').get_tokens_as_string() == "hi,there,<EOF>"



def test_comment_line():
    assert Tokenizer("// comments").get_tokens_as_string() == "<EOF>"

def test_comment_block():
    assert Tokenizer("/* block comment */").get_tokens_as_string() == "<EOF>"

def test_comment_block_multiline():
    assert Tokenizer("/* line 1 \n line 2 */").get_tokens_as_string() == "<EOF>"

def test_comment_mix():
    assert Tokenizer("int a; // decl").get_tokens_as_string() == "int,a,;,<EOF>"

def test_comment_in_string():
    assert Tokenizer('"//"').get_tokens_as_string() == "//,<EOF>"



def test_mix_decl():
    assert Tokenizer("int x = 5;").get_tokens_as_string() == "int,x,=,5,;,<EOF>"

def test_mix_expr():
    assert Tokenizer("a = (b + 1.5) * 2;").get_tokens_as_string() == \
        "a,=,(,b,+,1.5,),*,2,;,<EOF>"

def test_mix_loop():
    assert Tokenizer("for(int i=0;i<10;i++)").get_tokens_as_string() == \
        "for,(,int,i,=,0,;,i,<,10,;,i,++,),<EOF>"

def test_mix_array_access():
    assert Tokenizer("arr[i] = 1;").get_tokens_as_string() == \
        "arr,[,i,],=,1,;,<EOF>"

def test_mix_string_concat():
    assert Tokenizer('"a" + "b"').get_tokens_as_string() == "a,+,b,<EOF>"


def test_err_illegal_char():
    result = Tokenizer("#").get_tokens_as_string()
    assert "Error Token" in result

def test_err_illegal_char_2():
    result = Tokenizer("@").get_tokens_as_string()
    assert "Error Token" in result

def test_err_unclose_string():
    result = Tokenizer('"abc').get_tokens_as_string()
    assert "Unclosed String" in result

def test_err_unclose_string_newline():
    result = Tokenizer('"abc \n').get_tokens_as_string()
    assert "Unclosed String" in result

def test_err_illegal_escape():
    result = Tokenizer('"abc\\x"').get_tokens_as_string()
    assert "Illegal Escape" in result