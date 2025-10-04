import pytest
import sys
from io import StringIO
from unittest.mock import patch
from src.calc import calc
from src.Tokenezator import Tokenxix
from src.prnv import check_rpn
from src.main import main
from src.isdigit import isnumber
from src.replacer import replaceunar
from src.skobki_check import check_skobki
from src.vychisl import schet

def capture_calc_output(expr):
    with patch('sys.stdout', new=StringIO()) as fake_out:
        with patch('sys.exit') as mock_exit:
            try:
                result = calc(expr)
                output = fake_out.getvalue().strip()
                return result, output, None
            except SystemExit:
                output = fake_out.getvalue().strip()
                return None, output, 'SystemExit'
            except Exception as e:
                return None, '', str(e)

class TestTokenxix:
    """Тесты для токенизатора Tokenxix."""
    
    def test_simple_expression(self):
        assert Tokenxix("2 3 +") == ['2', '3', '+']
    
    def test_unary_minus(self):
        assert Tokenxix("~3 2 +") == ['~3', '2', '+']
    
    def test_decimal_dot(self):
        assert Tokenxix("2.5 3 +") == ['2.5', '3', '+']
    
    def test_decimal_comma(self):
        assert Tokenxix("2,5 3 +") == ['2,5', '3', '+']
    
    def test_power(self):
        assert Tokenxix("2 ** 3") == ['2', '**', '3']
    
    def test_floor_div(self):
        assert Tokenxix("5 // 2") == ['5', '//', '2']
    
    def test_brackets(self):
        assert Tokenxix("( 2 3 + )") == ['(', '2', '3', '+', ')']
    
    def test_separate_minus(self):
        assert Tokenxix("-5 3 +") == ['-', '5', '3', '+']
    
    def test_invalid_token_ignored(self):
        assert Tokenxix("2 abc +") == ['2', '+'] 
    
    def test_modulo(self):
        assert Tokenxix("10 % 3") == ['10', '%', '3']
    
    def test_nested_brackets(self):
        assert Tokenxix("((2 + 3))") == ['(', '(', '2', '+', '3', ')', ')']

class TestReplaceunar:
    """Тесты для замены унарных операторов."""
    
    def test_replace_tilde(self):
        tokens = ['~3', '2']
        assert replaceunar(tokens) == ['-3', '2']
    
    def test_replace_comma(self):
        tokens = ['2,5', '3']
        assert replaceunar(tokens) == ['2.5', '3']
    
    def test_replace_dollar(self):
        tokens = ['$+3', '2']
        assert replaceunar(tokens) == ['+3', '2']
    
    def test_no_change(self):
        tokens = ['2', '3', '+']
        assert replaceunar(tokens) == ['2', '3', '+']
    
    def test_multiple_replaces(self):
        tokens = ['~2,5', '$-3.0']
        assert replaceunar(tokens) == ['-2.5', '-3.0']

class TestIsnumber:
    """Тесты для проверки числа."""
    
    def test_positive_int(self):
        assert isnumber('5') is True
    
    def test_negative_int(self):
        assert isnumber('-5') is True
    
    def test_decimal_dot(self):
        assert isnumber('2.5') is True
    
    def test_decimal_comma(self):
        assert isnumber('2,5') is True

    def test_float_start_dot(self):
        assert isnumber('.5') is True
    
    def test_positive_float(self):
        assert isnumber('+3.14') is True
    
    def test_invalid_double_minus(self):
        assert isnumber('--3') is False
    
    def test_invalid_end_dot(self):
        assert isnumber('5.') is False
    
    def test_invalid_end_comma(self):
        assert isnumber('5,') is False
    
    def test_non_number(self):
        assert isnumber('+') is False
        assert isnumber('abc') is False

class TestSchet:
    
    def test_add(self):
        assert schet('2', '3', '+') == 5.0
    
    def test_sub(self):
        assert schet('3', '2', '-') == -1.0 
    
    def test_mul(self):
        assert schet('2', '3', '*') == 6.0
    
    def test_div(self):
        assert schet('2', '10', '/') == 5.0
    
    def test_power(self):
        assert schet('3', '2', '**') == 8.0
    
    def test_floor_div_int(self):
        assert schet('2', '5', '//') == 2
    
    def test_mod_int(self):
        assert schet('2', '5', '%') == 1

class TestCheckRpn:
    """Тесты для проверки и вычисления RPN."""
    
    def test_valid_simple(self):
        tokens = ['2', '3', '+']
        assert check_rpn(tokens, 0) is True
        assert check_rpn(tokens, 1) == 5.0
    
    def test_valid_complex(self):
        tokens = ['2', '3', '+', '4', '*']
        assert check_rpn(tokens, 0) is True
        assert check_rpn(tokens, 1) == 20.0
    
    def test_invalid_too_few(self):
        tokens = ['2', '+']
        assert check_rpn(tokens, 0) is False
    
    def test_invalid_too_many(self):
        tokens = ['2', '3', '4', '+']
        assert check_rpn(tokens, 0) is False
    
    def test_ignore_brackets(self):
        tokens = ['(', '2', '3', '+', ')']
        assert check_rpn(tokens, 0) is True
        assert check_rpn(tokens, 1) == 5.0
    
    def test_invalid_token(self):
        tokens = ['2', 'abc', '+']
        assert check_rpn(tokens, 0) is False
    
    def test_unary_in_tokens(self):
        tokens = ['-2', '3', '+']
        assert check_rpn(tokens, 0) is True
        assert check_rpn(tokens, 1) == 1.0

class TestCheckSkobki:
    """Тесты для проверки скобок."""
    
    def test_no_brackets(self):
        tokens = ['2', '3', '+']
        assert check_skobki(tokens) is True
    
    def test_simple_brackets(self):
        tokens = ['(', '2', '3', '+', ')']
        assert check_skobki(tokens) is True
    
    def test_nested_brackets(self):
        tokens = ['(', '(', '2', '3', '+', ')', '4', '*', ')']
        assert check_skobki(tokens) is True
    
    def test_mismatched_open(self):
        tokens = ['(', '2', '3', '+']
        assert check_skobki(tokens) is False
    
    def test_mismatched_close(self):
        tokens = ['2', '3', '+', ')']
        assert check_skobki(tokens) is False
    
    def test_invalid_sub_rpn(self):
        tokens = ['(', '2', '+', ')']
        assert check_skobki(tokens) is False
    

class TestCalcFunction:
    """Тесты для основной функции calc."""
    
    def test_empty(self):
        result, output, exc = capture_calc_output("")
        assert result == 0
        assert output == "Ошибка, Введена пустая строка"
        assert exc is None
    
    def test_whitespace(self):
        result, output, exc = capture_calc_output("   ")
        assert result == 0
        assert output == "Ошибка, Введена пустая строка"
    
    def test_simple_add(self):
        result, output, exc = capture_calc_output("2 3 +")
        assert exc is None
        assert output == "5.0"
    
    def test_unary_minus(self):
        result, output, exc = capture_calc_output("~2 3 +")
        assert output == "1.0"
    
    def test_sub_negative(self):
        result, output, exc = capture_calc_output("2 3 -")
        assert output == "-1.0"
    
    def test_decimal_comma(self):
        result, output, exc = capture_calc_output("2,5 3 +")
        assert output == "5.5"
    
    def test_div(self):
        result, output, exc = capture_calc_output("10 2 /")
        assert output == "5.0"
    
    def test_power(self):
        result, output, exc = capture_calc_output("2 3 **")
        assert output == "8.0"
    
    def test_floor_div(self):
        result, output, exc = capture_calc_output("5 2 //")
        assert output == "2"
    
    def test_mod(self):
        result, output, exc = capture_calc_output("5 2 %")
        assert output == "1"
    
    def test_brackets(self):
        result, output, exc = capture_calc_output("( 2 3 + ) 4 *")
        assert output == "20.0"
    
    def test_nested_brackets(self):
        result, output, exc = capture_calc_output("(( 2 3 + ) 4 * ) 5 -")
        assert output == "15.0"
    
    def test_invalid_rpn(self):
        result, output, exc = capture_calc_output("2 +")
        assert output == ""
    
    def test_separate_minus_invalid(self):
        result, output, exc = capture_calc_output("-5 3 +")
        assert output == ""
    
    def test_div_zero(self):
        result, output, exc = capture_calc_output("2 0 /")
        assert exc == 'SystemExit'
        assert "Деление на 0 невозможно" in output
    
    def test_floor_div_float(self):
        result, output, exc = capture_calc_output("5.5 2 //")
        assert exc == 'SystemExit'
        assert "Операции // и % только для целых чисел" in output
    
    def test_mod_float(self):
        result, output, exc = capture_calc_output("5.5 2 %")
        assert exc == 'SystemExit'
        assert "Операции // и % только для целых чисел" in output
    
    def test_unknown_op(self):
        result, output, exc = capture_calc_output("2 3 &")
        assert output == ""
    
    
    def test_zero(self):
        result, output, exc = capture_calc_output("0 5 +")
        assert output == "5.0"
    
    def test_invalid_brackets(self):
        result, output, exc = capture_calc_output("( 2 3 +")
        assert output == "Открывающих скобок больше чем закрывающих"
    
    def test_brackets_invalid_sub(self):
        result, output, exc = capture_calc_output("( 2 + )")
        assert output == "Выражение в скобках не является обратной польской записью"
    
