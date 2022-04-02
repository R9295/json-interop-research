import pytest

import orjson
from .commons import (  # isort: skip
    assert_dict,
    assert_list,
    assert_float,
    
)

def test_object_long_strings():
    data = "''"
    expected = ''
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_unicodeEscapedBackslash():
    with open('fixtures/y_string_unicodeEscapedBackslash.json', 'rb') as file:
        data = file.read()
    expected = ["/"]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_number_int_with_exp():
    data = "[20e1]"
    expected = [200.0]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_array_with_trailing_space():
    data = "[2] "
    expected = [2]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_double_escape_a():
    with open('fixtures/y_string_double_escape_a.json', 'rb') as file:
        data = file.read()
    expected = ""
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_number_negative_one():
    data = "[-1]"
    expected = [-1]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_number_real_capital_e():
    data = "[1E12]"
    expected = [1000000000000.0]
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_number_real_capital_e_two():
    data = "[1E22]"
    expected = [1e+22]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_allowed_escapes():
    with open('fixtures/y_string_allowed_escapes.json', 'rb') as file:
        data = file.read()
    expected = ""
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_structure_true_in_array():
    data = "[true]"
    expected = [True]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_structure_lonely_negative_real():
    data = "-0.1"
    expected = -0.1
    serialized_data = orjson.loads(data)
    assert assert_float(serialized_data, expected)
    
def test_object_with_newlines():
    with open('fixtures/y_object_with_newlines.json', 'rb') as file:
        data = file.read()
    expected = {"a":"b"}
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_unicode_U_plus_1FFFE_nonchar():
    with open('fixtures/y_string_unicode_U_plus_1FFFE_nonchar.json', 'rb') as file:
        data = file.read()
    expected = ""
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_nonCharacterInUTF_minus_8_U_plus10FFFF():
    with open('fixtures/y_string_nonCharacterInUTF_minus_8_U_plus10FFFF.json', 'rb') as file:
        data = file.read()
    expected = ""
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_number_real_exponent():
    data = "[123e45]"
    expected = [1.23e+47]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_object_duplicated_key():
    with open('fixtures/y_object_duplicated_key.json', 'rb') as file:
        data = file.read()
    expected = {"a":"c"}
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_object_basic():
    with open('fixtures/y_object_basic.json', 'rb') as file:
        data = file.read()
    expected = {"a":"b","a":"c"}
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_last_surrogates_1_and_2():
    with open('fixtures/y_string_last_surrogates_1_and_2.json', 'rb') as file:
        data = file.read()
    expected = ""
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_number_real_pos_exponent():
    data = "[1e+2]"
    expected = 100.0
    serialized_data = orjson.loads(data)
    assert assert_float(serialized_data, expected)
    
def test_string_unicode_U_plus_FFFE_nonchar():
    with open('fixtures/y_string_unicode_U_plus_FFFE_nonchar.json', 'rb') as file:
        data = file.read()
    expected = ""
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_uEscape():
    with open('fixtures/y_string_uEscape.json', 'rb') as file:
        data = file.read()
    expected = ""
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_two_byte_utf_8():
    with open('fixtures/y_string_two_byte_utf_8.json', 'rb') as file:
        data = file.read()
    expected = ""
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_in_array_with_leading_space():
    with open('fixtures/y_string_in_array_with_leading_space.json', 'rb') as file:
        data = file.read()
    expected = ["asd"]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_array_with_1_and_newline():
    with open('fixtures/y_array_with_1_and_newline.json', 'rb') as file:
        data = file.read()
    expected = [1]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_number_real_capital_e_neg_exp():
    data = "[1E-2]"
    expected = [0.01]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_escaped_control_character():
    with open('fixtures/y_string_escaped_control_character.json', 'rb') as file:
        data = file.read()
    expected = ""
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_array_with_leading_space():
    data = " [1]"
    expected = [1]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_one_byte_utf_8():
    with open('fixtures/y_string_one_byte_utf_8.json', 'rb') as file:
        data = file.read()
    expected = ""
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_number_real_fraction_exponent():
    data = "[123.456e78]"
    expected = [1.23456e+80]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_object_extreme_numbers():
    with open('fixtures/y_object_extreme_numbers.json', 'rb') as file:
        data = file.read()
    expected = {"min": -1e+28, "max": 1e+28}
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_object_duplicated_key_and_value():
    with open('fixtures/y_object_duplicated_key_and_value.json', 'rb') as file:
        data = file.read()
    expected = {"a":"b"}
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_array_empty():
    data = "[]"
    expected = []
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_array_heterogeneous():
    with open('fixtures/y_array_heterogeneous.json', 'rb') as file:
        data = file.read()
    expected = [None, 1, "1", {}]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_number_double_close_to_zero():
    data = "[-0.000000000000000000000000000000000000000000000000000000000000000000000000000001]"
    expected = [-1e-78]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_pi():
    with open('fixtures/y_string_pi.json', 'rb') as file:
        data = file.read()
    expected = ["π"]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_unicode_escaped_double_quote():
    with open('fixtures/y_string_unicode_escaped_double_quote.json', 'rb') as file:
        data = file.read()
    expected = ['"']
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_array_empty_string():
    with open('fixtures/y_array_empty_string.json', 'rb') as file:
        data = file.read()
    expected = [""]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_array_false():
    data = "[false]"
    expected = [False]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_unicode_U_plus_2064_invisible_plus():
    with open('fixtures/y_string_unicode_U_plus_2064_invisible_plus.json', 'rb') as file:
        data = file.read()
    expected = ["+"]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_object_string_unicode():
    with open('fixtures/y_object_string_unicode.json', 'rb') as file:
        data = file.read()
    expected = {}
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_object_escaped_null_in_key():
    with open('fixtures/y_object_escaped_null_in_key.json', 'rb') as file:
        data = file.read()
    expected = {'foo\x00bar': 42}
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_simple_ascii():
    with open('fixtures/y_string_simple_ascii.json', 'rb') as file:
        data = file.read()
    expected = ["asd "]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_unicode_U_plus_FDD0_nonchar():
    with open('fixtures/y_string_unicode_U_plus_FDD0_nonchar.json', 'rb') as file:
        data = file.read()
    expected = ["\ufdd0"]
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_nonCharacterInUTF_8_U_plus_FFFF():
    with open('fixtures/y_string_nonCharacterInUTF_8_U_plus_FFFF.json', 'rb') as file:
        data = file.read()
    expected = [""]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_number_0e_plus_1():
    data = "[0e+1]"
    expected = [0.0]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_unescaped_char_delete():
    with open('fixtures/y_string_unescaped_char_delete.json', 'rb') as file:
        data = file.read()
    expected = [""]
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_number_real_capital_e_pos_exp():
    data = "[1E+2]"
    expected = [100.0]
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_unicode_U_plus_200B_ZERO_WIDTH_SPACE():
    with open('fixtures/y_string_unicode_U_plus_200B_ZERO_WIDTH_SPACE.json', 'rb') as file:
        data = file.read()
    expected = ["\u200b"]
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_u_plus_2028_line_sep():
    with open('fixtures/y_string_u_plus_2028_line_sep.json', 'rb') as file:
        data = file.read()
    expected = [" "]
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_accepted_surrogate_pair():
    with open('fixtures/y_string_accepted_surrogate_pair.json', 'rb') as file:
        data = file.read()
    expected = ["\udd1ea"]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_object_empty_key():
    with open('fixtures/y_object_empty_key.json', 'rb') as file:
        data = file.read()
    expected = {"":0}
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_number_simple_real():
    data = "[123.456789]"
    expected = [123.456789]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_uescaped_newline():
    with open('fixtures/y_string_uescaped_newline.json', 'rb') as file:
        data = file.read()
    expected = ''
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_backslash_doublequotes():
    with open('fixtures/y_string_backslash_doublequotes.json', 'rb') as file:
        data = file.read()
    expected = ["\""]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_object():
    with open('fixtures/y_object.json', 'rb') as file:
        data = file.read()
    expected = {"asd":"sdf", "dfg":"fgh"}
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_utf8():
    with open('fixtures/y_string_utf8.json', 'rb') as file:
        data = file.read()
    expected = ["€𝄞"]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_structure_string_empty():
    data = "''"
    expected = ""
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_null_escape():
    with open('fixtures/y_string_null_escape.json', 'rb') as file:
        data = file.read()
    expected = ["\x00"]
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_space():
    data = " "
    expected = ''
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_array_with_several_null():
    data = "[1,null,null,null,2]"
    expected = [1, None, None, None, 2]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_number_negative_int():
    data = "[-123]"
    expected = [-123]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_structure_lonely_false():
    data = "false"
    expected = False
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_accepted_surrogate_pairs():
    with open('fixtures/y_string_accepted_surrogate_pairs.json', 'rb') as file:
        data = file.read()
    expected = ["😹💍"]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_three_byte_utf_8():
    with open('fixtures/y_string_three_byte_utf_8.json', 'rb') as file:
        data = file.read()
    expected = [""]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_structure_lonely_null():
    data = "null"
    expected = None
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_structure_lonely_true():
    data = "true"
    expected = True
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_in_array():
    with open('fixtures/y_string_in_array.json', 'rb') as file:
        data = file.read()
    expected = ["asd"]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_unicode_U_plus_10FFFE_nonchar():
    with open('fixtures/y_string_unicode_U_plus_10FFFE_nonchar.json', 'rb') as file:
        data = file.read()
    expected = ""
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_unicode_2():
    with open('fixtures/y_string_unicode_2.json', 'rb') as file:
        data = file.read()
    expected = ["⍂㈴⍂"]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_number():
    data = "[123e65]"
    expected = [1.23e+67]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_array_null():
    data = "[null]"
    expected = [None]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_double_escape_n():
    with open('fixtures/y_string_double_escape_n.json', 'rb') as file:
        data = file.read()
    expected = ["\n"]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_structure_lonely_int():
    data = "42"
    expected = 42
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_backslash_and_u_escaped_zero():
    with open('fixtures/y_string_backslash_and_u_escaped_zero.json', 'rb') as file:
        data = file.read()
    expected = ["\x00"]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_escaped_noncharacter():
    with open('fixtures/y_string_escaped_noncharacter.json', 'rb') as file:
        data = file.read()
    expected = ["\uffff"]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_with_del_character():
    with open('fixtures/y_string_with_del_character.json', 'rb') as file:
        data = file.read()
    expected = ["a\x7fa"]
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_object_empty():
    data = "{}"
    expected = {}
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_nbsp_uescaped():
    with open('fixtures/y_string_nbsp_uescaped.json', 'rb') as file:
        data = file.read()
    expected = ["new\xa0line"]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_reservedCharacterInUTF_8_U_plus_1BFFF():
    with open('fixtures/y_string_reservedCharacterInUTF_8_U_plus_1BFFF.json', 'rb') as file:
        data = file.read()
    expected = ["𛿿"]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_number_real_neg_exp():
    data = "[1e-2]"
    expected = [0.01]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_1_2_3_bytes_UTF_8_sequences():
    with open('fixtures/y_string_1_2_3_bytes_UTF_8_sequences.json', 'rb') as file:
        data = file.read()
    expected = ["`Īካ"]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_array_arraysWithSpaces():
    data = "[[]   ]"
    expected = [[]]
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_number_minus_zero():
    data = "[-0]"
    expected = [0]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_structure_trailing_newline():
    with open('fixtures/y_structure_trailing_newline.json', 'rb') as file:
        data = file.read()
    expected = ["a"]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_surrogates_U_plus_MUSICAL_SYMBOL_G():
    with open('fixtures/y_string_surrogates_U_plus_1D11E_MUSICAL_SYMBOL_G_CLEF.json', 'rb') as file:
        data = file.read()
    expected = ["𝄞"]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_structure_lonely_string():
    data = "asd"
    expected = "asd"
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_structure_whitespace_array():
    data = " [] "
    expected = []
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_string_unicode():
    with open('fixtures/y_string_unicode.json', 'rb') as file:
        data = file.read()
    expected = []
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_number_0e1():
    data = "[0e1]"
    expected = [0.0]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_object_simple():
    with open('fixtures/y_object_simple.json', 'rb') as file:
        data = file.read()
    expected = {"a":[]}
    serialized_data = orjson.loads(data)
    assert assert_dict(serialized_data, expected)
    
def test_array_ending_with_newline():
    with open('fixtures/y_array_ending_with_newline.json', 'rb') as file:
        data = file.read()
    expected = ["a"]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_u_plus_2029_par_sep():
    with open('fixtures/y_string_u_plus_2029_par_sep.json', 'rb') as file:
        data = file.read()
    expected = [" "]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_number_negative_zero():
    data = "[-0]"
    expected = [0]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_number_after_space():
    data = "[ 4]"
    expected = [4]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_number_simple_int():
    data = "[123]"
    expected = [123]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
def test_string_comments():
    with open('fixtures/y_string_comments.json', 'rb') as file:
        data = file.read()
    expected = ["a/*b*/c/*d//e"]
    serialized_data = orjson.loads(data)
    assert assert_list(serialized_data, expected)
    
