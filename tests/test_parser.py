"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser


def test_parser_01_empty():
    assert Parser("").parse() == "success"

def test_parser_02_single_int():
    assert Parser("1;").parse() == "success"

def test_parser_03_single_id():
    assert Parser("a;").parse() == "success"

def test_parser_04_string():
    assert Parser("\"hello\";").parse() == "success"

def test_stmt_01_int():
    assert Parser("1;").parse() == "success"

def test_stmt_02_float():
    assert Parser("1.5;").parse() == "success"

def test_stmt_03_id():
    assert Parser("a;").parse() == "success"

def test_stmt_04_string():
    assert Parser("\"hi\";").parse() == "success"

def test_stmt_05_bool():
    assert Parser("true;").parse() == "success"

def test_stmt_06_multi_stmt():
    assert Parser("a; b; 1;").parse() == "success"

def test_stmt_07_missing_semi():
    assert "Error" in Parser("a").parse()

def test_stmt_08_invalid_start():
    assert "Error" in Parser(";").parse()

def test_stmt_09_only_semi():
    assert "Error" in Parser(";").parse()

def test_stmt_10_empty_program():
    assert Parser("").parse() == "success"

def test_expr_01_add():
    assert Parser("1+2;").parse() == "success"

def test_expr_02_precedence():
    assert Parser("1+2*3;").parse() == "success"

def test_expr_03_paren():
    assert Parser("(1+2)*3;").parse() == "success"

def test_expr_04_rel():
    assert Parser("a < b;").parse() == "success"

def test_expr_05_eq():
    assert Parser("a == b;").parse() == "success"

def test_expr_06_logic():
    assert Parser("a && b || c;").parse() == "success"

def test_expr_07_unary():
    assert Parser("-a;").parse() == "success"

def test_expr_08_not():
    assert Parser("!true;").parse() == "success"

def test_expr_09_nested():
    assert Parser("!(a + b * (c - d));").parse() == "success"

def test_expr_10_error():
    assert "Error" in Parser("1 + ;").parse()

def test_decl_01_single_int():
    assert Parser("int a;").parse() == "success"

def test_decl_02_single_float():
    assert Parser("float x;").parse() == "success"

def test_decl_03_multi_id():
    assert Parser("int a, b, c;").parse() == "success"

def test_decl_04_init():
    assert Parser("int a = 1;").parse() == "success"

def test_decl_05_multi_init():
    assert Parser("int a = 1, b = 2;").parse() == "success"

def test_decl_06_expr_init():
    assert Parser("float x = 1 + 2 * 3;").parse() == "success"

def test_decl_07_bool():
    assert Parser("bool flag = true;").parse() == "success"

def test_decl_08_string():
    assert Parser("string s = \"hi\";").parse() == "success"

def test_decl_09_missing_semi():
    assert "Error" in Parser("int a").parse()

def test_decl_10_missing_id():
    assert "Error" in Parser("int ;").parse()

def test_decl_11_assign_no_expr():
    assert "Error" in Parser("int a = ;").parse()

def test_decl_12_comma_end():
    assert "Error" in Parser("int a, ;").parse()

def test_decl_13_wrong_type():
    assert "Error" in Parser("integer a;").parse()

def test_decl_14_expr_not_allowed():
    assert "Error" in Parser("int 1a;").parse()

def test_decl_15_mix_stmt():
    assert Parser("int a; a + 1;").parse() == "success"

def test_block_01_empty():
    assert Parser("{}").parse() == "success"

def test_block_02_single_decl():
    assert Parser("{ int a; }").parse() == "success"

def test_block_03_multi_stmt():
    assert Parser("{ int a; a + 1; }").parse() == "success"

def test_block_04_nested():
    assert Parser("{ int a; { int b; } }").parse() == "success"

def test_block_05_deep_nested():
    assert Parser("{ { { int a; } } }").parse() == "success"

def test_block_06_block_in_program():
    assert Parser("{ int a; } int b;").parse() == "success"

def test_block_07_stmt_after_block():
    assert Parser("{ int a; } a + 1;").parse() == "success"

def test_block_08_missing_rbrace():
    assert "Error" in Parser("{ int a; ").parse()

def test_block_09_missing_lbrace():
    assert "Error" in Parser("int a; }").parse()

def test_block_10_stmt_no_semi():
    assert "Error" in Parser("{ int a a + 1; }").parse()

def test_block_11_unexpected_token():
    assert "Error" in Parser("{ ; }").parse()

def test_block_12_only_rbrace():
    assert "Error" in Parser("}").parse()

def test_block_13_only_lbrace():
    assert "Error" in Parser("{").parse()

def test_block_14_nested_error():
    assert "Error" in Parser("{ { int a; }").parse()

def test_block_15_decl_after_error():
    assert "Error" in Parser("{ int a } int b;").parse()

def test_if_01_simple():
    assert Parser("if (a) a + 1;").parse() == "success"

def test_if_02_block():
    assert Parser("if (a) { a + 1; }").parse() == "success"

def test_if_03_if_else():
    assert Parser("if (a) a + 1; else a + 2;").parse() == "success"

def test_if_04_if_else_block():
    assert Parser("if (a) { a + 1; } else { a + 2; }").parse() == "success"

def test_if_05_nested_if():
    assert Parser("if (a) if (b) a + 1;").parse() == "success"

def test_if_06_dangling_else():
    assert Parser(
        "if (a) if (b) a + 1; else a + 2;"
    ).parse() == "success"

def test_if_07_else_block():
    assert Parser(
        "if (a) if (b) { a + 1; } else { a + 2; }"
    ).parse() == "success"

def test_if_08_stmt_after_if():
    assert Parser("if (a) a + 1; a + 2;").parse() == "success"

def test_if_09_if_in_block():
    assert Parser("{ if (a) a + 1; }").parse() == "success"

def test_if_10_if_else_in_block():
    assert Parser("{ if (a) a + 1; else a + 2; }").parse() == "success"

def test_if_11_missing_paren():
    assert "Error" in Parser("if a) a + 1;").parse()

def test_if_12_missing_rparen():
    assert "Error" in Parser("if (a a + 1;").parse()

def test_if_13_missing_stmt():
    assert "Error" in Parser("if (a)").parse()

def test_if_14_else_no_if():
    assert "Error" in Parser("else a + 1;").parse()

def test_if_15_else_no_stmt():
    assert "Error" in Parser("if (a) a + 1; else").parse()

def test_if_16_if_no_condition():
    assert "Error" in Parser("if () a + 1;").parse()

def test_if_17_if_incomplete():
    assert "Error" in Parser("if (a)").parse()

def test_if_18_nested_missing_stmt():
    assert "Error" in Parser("if (a) if (b)").parse()

def test_if_19_extra_else():
    assert "Error" in Parser("if (a) a + 1; else else a + 2;").parse()

def test_if_20_only_if():
    assert "Error" in Parser("if").parse()

def test_while_01():
    assert Parser("while(a) b;").parse() == "success"

def test_while_02():
    assert Parser("while(true) a;").parse() == "success"

def test_while_03():
    assert Parser("while(a) { b; c; }").parse() == "success"

def test_while_04():
    assert Parser("while(a) while(b) c;").parse() == "success"

def test_while_05():
    assert Parser("while(a) if(b) c; else d;").parse() == "success"

def test_while_06():
    assert Parser("""
        {
            while(a) b;
            c;
        }
    """).parse() == "success"

def test_for_01():
    assert Parser("for(i=0;i<10;i=i+1) a;").parse() == "success"

def test_for_02():
    assert Parser("for(;i<10;i=i+1) a;").parse() == "success"

def test_for_03():
    assert Parser("for(i=0;;i=i+1) a;").parse() == "success"

def test_for_04():
    assert Parser("for(i=0;i<10;) a;").parse() == "success"

def test_for_05():
    assert Parser("for(;;) a;").parse() == "success"

def test_for_06():
    assert Parser("for(i=0;i<10;i=i+1){a;b;}").parse() == "success"

def test_break():
    assert Parser("break;").parse() == "success"

def test_continue():
    assert Parser("continue;").parse() == "success"

def test_return_empty():
    assert Parser("return;").parse() == "success"

def test_return_expr():
    assert Parser("return a+1;").parse() == "success"

def test_return_in_block():
    assert Parser("{ return 1; }").parse() == "success"

def test_return_in_if():
    assert Parser("if(a) return; else return 1;").parse() == "success"

def test_nested_if():
    src = "if(a) if(b) c; else d;"
    assert Parser(src).parse() == "success"

def test_while_if():
    src = "while(a) if(b) break;"
    assert Parser(src).parse() == "success"

def test_for_if_return():
    src = "for(i=0;i<10;i=i+1) if(i==5) return;"
    assert Parser(src).parse() == "success"

def test_block_multi_stmt():
    src = "{ int a; a=1; if(a) return; }"
    assert Parser(src).parse() == "success"

def test_nested_block():
    src = "{ { a; } { b; } }"
    assert Parser(src).parse() == "success"

def test_error_missing_semi():
    src = "a"
    assert "Error" in Parser(src).parse()

def test_error_unmatched_brace():
    src = "{ a;"
    assert "Error" in Parser(src).parse()

def test_parser_100_everything():
    src = """
    {
        int i, sum = 0;
        string s = "hello";

        for(i = 0; i < 10; i = i + 1) {
            if(i == 5) continue;
            sum = sum + i;

            while(sum < 50) {
                if(sum == 30) break;
                sum = sum + 1;
            }
        }

        if(sum > 0 && true || false)
            return;
        else {
            s = "done";
            return;
        }
    }
    """
    assert Parser(src).parse() == "success"

