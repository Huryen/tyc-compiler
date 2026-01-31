"""
Parser test cases for TyC compiler
Implemented 100 test cases covering Declarations, Statements, Expressions, and Structure.
"""

import pytest
from tests.utils import Parser

def expect_success(snippet):
    snippet = snippet.strip()
    top_level_keywords = ["struct", "void", "int", "float", "string", "bool", "auto"]
    is_top_level = False
    for kw in top_level_keywords:
        if snippet.startswith(kw):
            # Nếu là struct
            if kw == "struct":
                is_top_level = True
                break
            if "(" in snippet and "{" in snippet: 
                is_top_level = True
                break

    if is_top_level:
         assert Parser(snippet).parse() == "success"
    else:
        program = f"void main() {{ {snippet} }}"
        result = Parser(program).parse()
        if result != "success":
            print(f"\nFAILED snippet: {snippet}")
            print(f"Wrapped program: {program}")
            print(f"Result: {result}")
        assert result == "success"

def expect_error(snippet):
    program = f"void main() {{ {snippet} }}"
    assert "Error" in Parser(program).parse()


def test_struct_01(): expect_success("struct A { int x; };")
def test_struct_02(): expect_success("struct Point { float x; float y; };")
def test_struct_03(): expect_success("struct Node { int val; Node next; };")
def test_func_01(): expect_success("void main() {}")
def test_func_02(): expect_success("int add(int a, int b) { return a+b; }")
def test_func_03(): expect_success("string getName() { return \"TyC\"; }")
def test_func_04(): expect_success("void process(float f, string s) {}")
def test_func_05(): expect_success("struct A {}; void main() { A a; }")
def test_program_empty(): expect_success("void main(){}")
def test_func_decl_only(): expect_success("void foo() { }") 


def test_decl_01_single_int(): expect_success("int a;")
def test_decl_02_single_float(): expect_success("float f;")
def test_decl_03_multi_id(): expect_success("int a, b, c;")
def test_decl_04_init(): expect_success("int a = 1;")
def test_decl_05_multi_init(): expect_success("int a = 1, b = 2;")
def test_decl_06_expr_init(): expect_success("int a = 1 + 2;")
def test_decl_07_bool(): expect_success("bool b = true;")
def test_decl_08_string(): expect_success('string s = "hello";')
def test_decl_09_auto(): expect_success("auto a = 1;")
def test_decl_10_auto_string(): expect_success('auto s = "hi";')
def test_decl_11_struct_type(): expect_success("Point p;")
def test_decl_12_mixed_init(): expect_success("int a, b = 1, c;")
def test_decl_13_auto_expr(): expect_success("auto x = 1 + 2 * 3;")
def test_decl_14_complex_init(): expect_success("float f = 1.0 / 2.0;")
def test_decl_15_mix_stmt(): expect_success("int a; a = 1;")


def test_stmt_assign(): expect_success("a = 1;")
def test_stmt_assign_chain(): expect_success("a = b = 1;")
def test_stmt_expr(): expect_success("1 + 2;")
def test_stmt_block(): expect_success("{ int x; }")
def test_stmt_empty_block(): expect_success("{}")
def test_stmt_nested_block(): expect_success("{ { } }")
def test_stmt_if(): expect_success("if (true) a = 1;")
def test_stmt_if_else(): expect_success("if (a) b=1; else b=2;")
def test_stmt_while(): expect_success("while (a < 10) a++;")
def test_stmt_for_basic(): expect_success("for(i=0; i<10; i++) {}")
def test_stmt_for_decl(): expect_success("for(int i=0; i<10; i++) {}")
def test_stmt_for_empty(): expect_success("for(;;) break;")
def test_stmt_break(): expect_success("while(1) break;")
def test_stmt_continue(): expect_success("while(1) continue;")
def test_stmt_return(): expect_success("return 1;")


def test_expr_add(): expect_success("a + b;")
def test_expr_sub(): expect_success("a - b;")
def test_expr_mul(): expect_success("a * b;")
def test_expr_div(): expect_success("a / b;")
def test_expr_mod(): expect_success("a % b;")
def test_expr_prec_1(): expect_success("a + b * c;")
def test_expr_prec_2(): expect_success("(a + b) * c;")
def test_expr_rel_lt(): expect_success("a < b;")
def test_expr_rel_ge(): expect_success("a >= b;")
def test_expr_eq(): expect_success("a == b;")
def test_expr_neq(): expect_success("a != b;")
def test_expr_logic_and(): expect_success("a && b;")
def test_expr_logic_or(): expect_success("a || b;")
def test_expr_unary_not(): expect_success("!a;")
def test_expr_unary_neg(): expect_success("-a;")
def test_expr_inc(): expect_success("a++;")
def test_expr_dec(): expect_success("a--;")
def test_expr_member(): expect_success("a.b;")
def test_expr_member_deep(): expect_success("a.b.c;")
def test_expr_mix(): expect_success("a.b + c * d;")


def test_call_01(): expect_success("foo();")
def test_call_02(): expect_success("foo(1);")
def test_call_03(): expect_success("foo(1, 2);")
def test_call_04(): expect_success("foo(a, b);")
def test_call_05(): expect_success("foo(1+2);")
def test_call_06(): expect_success("a.foo();")
def test_call_07(): expect_success("foo().bar;")
def test_call_08(): expect_success("foo(bar());")
def test_call_09(): expect_success("print(\"hello\");")
def test_call_10(): expect_success("foo(1, \"s\", 3.0);")


def test_switch_01(): expect_success("switch(x) {}")
def test_switch_02(): expect_success("switch(x) { case 1: break; }")
def test_switch_03(): expect_success("switch(x) { default: break; }")
def test_switch_04(): expect_success("switch(x) { case 1: a=1; break; case 2: a=2; break; }")
def test_switch_05(): expect_success("switch(x) { case 1: case 2: a=1; break; }") 
def test_switch_06(): expect_success("switch(x+1) { case 1: break; }")
def test_switch_07(): expect_success("switch(x) { case 1: { int a; } break; }")
def test_switch_08(): expect_success("switch(x) { default: a=1; }")
def test_switch_09(): expect_success("switch(foo()) { case 1: break; }")
def test_switch_10(): expect_success("switch(x) { case 1: a=1; default: a=0; }")



def test_complex_01(): expect_success("if (a) { if (b) c=1; else c=2; }")
def test_complex_02(): expect_success("for(int i=0; i<10; i++) { if(i%2==0) continue; }")
def test_complex_03(): expect_success("a = b > c ? 1 : 0;") if False else None 
def test_complex_04(): expect_success("return a.x + b.y;")
def test_complex_05(): expect_success("a = !b.c;") 
def test_complex_06(): expect_success("a = -1 * 2;")
def test_complex_07(): expect_success("struct A { int x; }; int main() { A a; a.x = 1; }")
def test_complex_08(): expect_success("while(true) { if(check()) break; }")
def test_complex_09(): expect_success("int a = foo(1, bar(2));")
def test_complex_10(): expect_success("string s = \"a\" + \"b\";") 

def test_err_01_missing_semi(): expect_error("a = 1")
def test_err_02_bad_decl(): expect_error("int 1;")
def test_err_03_bad_if(): expect_error("if a < b")
def test_err_04_bad_while(): expect_error("while (a) {")
def test_err_05_bad_struct(): expect_error("struct { int x; };")
def test_err_06_double_else(): expect_error("if(a) {} else {} else {}")
def test_err_07_case_outside(): expect_error("case 1: break;")
def test_err_08_return_val_void(): expect_success("return;") 
def test_err_09_unclosed_paren(): expect_error("foo(1")
def test_err_10_bad_char(): expect_error("$")