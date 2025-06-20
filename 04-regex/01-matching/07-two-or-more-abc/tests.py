import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
    ("", False),
    ("abc", False),
    ("abcabc", True),
    ("abcabcabc", True),
    ("abcabcabcabc", True),
    ("abcabcabcabcabc", True),
    ("aabbccc", False),
    ("abcx", False),
    ("xabc", False),
    ("abca", False),
    ("abcab", False)
])
def test_function(string, expected):
    function_name = 'two_or_more_abc'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = bool(student_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
