import pytest

import orjson
from .commons import (  # isort: skip
    assert_dict,
    assert_list,
    assert_float,
    
)

def test_array_no_comma():
    '''
    Should not parse an array with multiple entries with no comma separation
    '''
    data = "[1 true]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_invalid_utf8():
    data = "[ÿ]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_just_minus():
    data = "[-]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_bracket_key():
    '''
    Should not parse a bracket used as object key
    '''
    data = "{[: \"x\"}"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_two_commas_in_a_row():
    '''
    Should not parse two commas in a row in an object
    '''
    data = "{\"a\":\"\",,\"c\":\"d\"}"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_2_e_three():
    data = "[2.e-3]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_1_0_e():
    data = "[1.0e-]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_ascii_unicode_identifier():
    data = "aÃ¥"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_whitespace_formfeed():
    data = "[]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_lone_continuation_byte_in_key_and_trailing_comma():
    with open('fixtures/n_object_lone_continuation_byte_in_key_and_trailing_comma.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_no_data():
    data = ""
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_1eE2():
    data = "[1eE2]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_0_capital_E_plus():
    data = "[0E+]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_minus_space_1():
    data = "[- 1]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_angle_bracket_dot():
    data = "<.>"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_unclosed_object():
    data = '{"asd":"asd"'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_single_quote():
    data = '"{a:0}"'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_incomplete_false():
    data = "[fals]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_with_alpha_char():
    data = "[1.8011670033376514H-308]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_with_alpha():
    data = "[1.2a-3]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_minus_infinity():
    data = "[-Infinity]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_escaped_emoji():
    with open('fixtures/n_string_escaped_emoji.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_open_object_open_string():
    data = '{"a'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_single_space():
    data = " "
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_open_array_object():
    data = ""
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_array_trailing_garbage():
    data = "[1]x"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_hex_1_digit():
    data = "[0x1]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_incomplete_true():
    data = "[tru]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_real_without_fractional_part():
    data = "[1.]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_1_dot_0e():
    data = "[1.0e]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_0_1_2():
    data = "[0.1.2]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_unescaped_newline():
    with open('fixtures/n_string_unescaped_newline.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_nullbyte_outside_string():
    with open('fixtures/n_structure_nullbyte_outside_string', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_open_object_open_array():
    data = "{["
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_trailing_comment_slash_open_incomplete():
    data = '{"a":""}/'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_comma_instead_of_closing_brace():
    data = '{"x": true,"'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_unclosed_array_unfinished_true():
    data = "[ false, tru"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_angle_bracket_null():
    data = "[<null>]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_2_dot_e3():
    data = "[2.e3]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_escaped_ctrl_char_tab():
    with open('fixtures/n_string_escaped_ctrl_char_tab.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_open_object():
    data = "{"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_repeated_null_null():
    data = "{null:null,null:null}"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_single_quote():
    data = "['single quote']"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_no_colon():
    data = '"{"a""'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_incomplete_escaped_character():
    with open('fixtures/n_string_incomplete_escaped_character.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_unescaped_tab():
    data = '["  "]'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_trailing_comment_open():
    data = '{"a":""}/**//'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_unclosed():
    data = "["
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_end_array():
    data = "]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_open_array_open_object():
    data = "[{"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_invalid_unicode_escape():
    with open('fixtures/n_string_invalid_unicode_escape.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_infinity():
    data = "[Infinity]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_lone_open_bracket():
    data = "["
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_unterminated_value():
    data = '{"a":"a"'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_trailing_comment_slash_open():
    data = '{"a":""}//'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_neg_int_starting_with_zero():
    data = "[-012]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number__dash_1_0_dot():
    data = "[-1.0.]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_missing_semicolon():
    data = '{"a" ""}'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_comma_instead_of_colon():
    data = '{"x", null}'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_capitalized_True():
    data = "[True]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_whitespace_U_plus_2060_word_joiner():
    with open('fixtures/n_structure_whitespace_U_plus_2060_word_joiner.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_number_and_several_commas():
    data = "[1,,]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_several_trailing_commas():
    data = '{"id":0,,,,,}'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_double_array():
    data = "[][]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_with_leading_zero():
    data = "[012]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_NaN():
    data = "[NaN]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_unclosed_with_object_inside():
    data = "[{}"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_0_dot_3e_plus():
    data = "[0.3e+]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_unescaped_ctrl_char():
    with open('fixtures/n_string_unescaped_ctrl_char.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_single_star():
    data = "*"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_minus_01():
    data = "[-01]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_object_with_trailing_garbage():
    data = '{"a": true} "x"'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_0e_plpus():
    data = "[0e+]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_unescaped_LF_before_string():
    with open('fixtures/n_structure_unescaped_LF_before_string.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_trailing_comma():
    data = '{"id":0,}'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_open_array_apostrophe():
    data = "[']"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_double_comma():
    data = "[1,,2]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_open_array_string():
    data = '["a"'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_with_trailing_garbage():
    data = '{"a":""}#'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_bad_value():
    data = '["x", truth]'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_minus_sign_with_trailing_garbage():
    data = "[-foo]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_missing_value():
    data = '{"a":"'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_array_with_extra_array_close():
    data = "[1]]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_100000_opening_arrays():
    data = ""
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_plus_1():
    data = "[+1]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_backslash_00():
    with open('fixtures/n_string_backslash_00.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_close_unopened_array():
    data = "1]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_1_true_without_comma():
    data = "[1 true]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_emoji():
    data = "n_object_emoji.json"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_UTF8_BOM_no_data():
    with open('fixtures/n_structure_UTF8_BOM_no_data.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_comma_and_number():
    data = "[,1]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_invalid_negative_real():
    data = "[-123.123foo]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_with_trailing_garbage():
    data = '""x'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_incomplete_surrogate():
    with open('fixtures/n_string_incomplete_surrogate.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_newlines_unclosed():
    with open('fixtures/n_array_newlines_unclosed.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_incomplete_invalid_value():
    data = "[x"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_unclosed_array():
    data = "[1"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_trailing_comment():
    data = '{"a":""}/**/'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_spaces_vertical_tab_formfeed():
    with open('fixtures/n_array_spaces_vertical_tab_formfeed.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_plus_plus():
    data = "[++1234]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_unicode_identifier():
    data = "Ã¥"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_a_invalid_utf8():
    data = "[aå]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_double_extra_comma():
    data = '["x",,]'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_open_object_close_array():
    data = "{]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_1_surrogate_then_escape_u1x():
    with open('fixtures/n_string_1_surrogate_then_escape_u1x.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_extra_close():
    with open('fixtures/n_array_extra_close.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_accentuated_char_no_quotes():
    data = "[Ã©]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_missing_key():
    data = "{:\"\"}"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_incomplete_surrogate_escape_invalid():
    with open('fixtures/n_string_incomplete_surrogate_escape_invalid.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_9_e_plus():
    data = "[9.e+]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_unicode_CapitalU():
    with open('fixtures/n_string_unicode_CapitalU.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_single_string_no_double_quotes():
    data = "ac"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_invalid_utf8_after_escape():
    with open('fixtures/n_string_invalid_utf8_after_escape.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_number_and_comma():
    data = "[1,]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_Inf():
    data = "[Inf]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_2_e_plus_3():
    data = "[2.e+3]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_neg_real_without_int_part():
    data = "[-.123]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_colon_instead_of_comma():
    data = "[\"\": 1]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number__plus_Inf():
    data = "[+Inf]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_incomplete_UTF8_BOM():
    with open('fixtures/n_structure_incomplete_UTF8_BOM.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_1_surrogate_then_escape_u1():
    with open('fixtures/n_string_1_surrogate_then_escape.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_unclosed_trailing_comma():
    data = "[1,"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_lone_invalid_utf_8():
    data = "å"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_invalid_backslash_esc():
    with open('fixtures/n_string_invalid_backslash_esc.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_unclosed_array_unfinished_false():
    data = "[ true, fals"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_with_single_string():
    data = '{ "foo" : "ar", "a" }'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_star_inside():
    data = "[*]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_multidigit_number_then_00():
    with open('fixtures/n_multidigit_number_then_00.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_object_with_comment():
    data = '{"a":/*comment*/""}'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_extra_comma():
    data = "[\"\",]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_leading_uescaped_thinspace():
    with open('fixtures/n_string_leading_uescaped_thinspace.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_items_separated_by_semicolon():
    data = "[1:2]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_unquoted_key():
    data = "{a: \"\"}"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_missing_value():
    data = "[   , \"\"]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_incomplete():
    with open('fixtures/n_array_incomplete.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_hex_2_digits():
    data = "[0x42]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_non_string_key_but_huge_number_instead():
    data = "{9999E9999:1}"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_object_followed_by_closing_object():
    data = "{}}"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_real_garbage_after_e():
    data = "[1ea]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_0_3e():
    data = "[0.3e]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_invalid_utf_8_in_bigger_int():
    data = "[123å]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_key_with_single_quotes():
    data = "{key: 'value'}"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_unclosed_with_new_lines():
    with open('fixtures/n_array_unclosed_with_new_lines.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_neg_with_garbage_at_end():
    data = "[-1x]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_garbage_at_end():
    data = '{"a":"a" 123}'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_U_plus_FF11_fullwidth_digit_one():
    with open('fixtures/n_number_U+FF11_fullwidth_digit_one.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_single_doublequote():
    data = '"'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_escape_x():
    with open('fixtures/n_string_escape_x.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_1_0e_plus():
    data = "[1.0e+]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_open_array_comma():
    data = "[,"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_open_object_comma():
    data = "{,"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_0_capital_E():
    data = "[0E]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_no_quotes_with_bad_escape():
    data = "[\n]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_minus_NaN():
    data = "[-NaN]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_minus_2_dot():
    data = "[-2.]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_invalid_utf_8_in_int():
    with open('fixtures/n_number_invalid_utf_8_in_int.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_0_e1():
    data = "[0.e1]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_just_comma():
    data = "[,]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_missing_colon():
    data = '{"a" }'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_starting_with_dot():
    data = "[.123]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_single_eacute():
    data = "é"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_unclosed_array_partial_null():
    data = "[ false, nul"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_expression():
    data = "[1+2]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_real_with_invalid_utf8_after_e():
    data = "[1eå]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_inner_array_no_comma():
    data = "[3[4]]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_array_with_unclosed_string():
    data = '["asd]'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_number_with_trailing_garbage():
    data = "2@"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_invalid_utf8_in_escape():
    with open('fixtures/n_string_invalid-utf-8-in-escape.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_1_000():
    data = "[1 000.0]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_escaped_backslash_bad():
    with open('fixtures/n_string_escaped_backslash_bad.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_double_colon():
    data = '{"x"::""}'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_object_unclosed_no_value():
    data = "{\"\":"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_incomplete_escape():
    with open('fixtures/n_string_incomplete_escape.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_invalid_plus_minus():
    data = "[0e+-1]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_array_comma_after_close():
    data = "[\"\"],"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_start_escape_unclosed():
    with open('fixtures/n_string_start_escape_unclosed.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_U_plus_2060_word_joined():
    data = "[â ]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_0e():
    data = "[0e]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_open_array_open_string():
    data = '["a"'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_1_surrogate_then_escape():
    data = ''
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number__dot_2e_3():
    data = "[.2e-3]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number_invalid_utf_8_in_exponent():
    data = "[1e1å]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_number__dot_minus_1():
    data = "[.-1]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_open_open():
    with open('fixtures/n_structure_open_open.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_string_1_surrogate_then_escape_u():
    with open('fixtures/n_string_1_surrogate_then_escape_u.json', 'rb') as file:
        data = file.read()
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_open_object_string_with_apostrophes():
    data = '""{a""'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_incomplete_null():
    data = "[nul]"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_structure_trailing_hash():
    data = '{"a":""}#{}'
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
def test_object_non_string_key():
    data = "{1:1}"
    try:
        serialized_data = orjson.loads(data)
        pytest.fail()
    except Exception as e:
        pass
        
    
