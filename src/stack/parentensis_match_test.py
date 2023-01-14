from .parentensis_matching import ParentesisMatching


def test_parentesis_matching():
    """Test for class init"""

    test_strings = ["[{((()))}]", "{((()))}"]
    for string in test_strings:
        parentesis_check = ParentesisMatching(string)
        assert isinstance(parentesis_check, ParentesisMatching)


def test_valid_strings():
    """Test for valid strings"""

    test_strings = ["[{((()))}]", "{((()))}"]
    for string in test_strings:
        parentesis_check = ParentesisMatching(string)
        assert parentesis_check.is_valid() is True, f"'{string}' is not a valid string"


def test_invalid_strings():
    """Test for invalid strings"""

    test_strings = ["(()))}]", "{(()]", "(({[", "{)"]
    for string in test_strings:
        parentesis_check = ParentesisMatching(string)
        assert parentesis_check.is_valid() is False, f"'{string}' is a valid string"
