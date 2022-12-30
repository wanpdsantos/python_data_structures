class ParentesisMatching:
    """Parentesis Matching checker"""

    def __init__(self, string: str):
        self.pointer = -1
        self.string = string
        self.stack = []

    def add_element(self, element: str):
        """Add new element to the stack"""

        self.stack.append(element)
        self.pointer += 1

    def remove_element(self):
        """Remove an element from the stack"""
        self.stack.pop(self.pointer)
        self.pointer -= 1

    def is_valid(self):
        """Check if the string as a valid parentesis matching"""
        for char in self.string:
            if char in ("(", "[", "{"):
                self.add_element(char)

            elif char == ")" and self.stack[self.pointer] == "(":
                self.remove_element()

            elif char == "]" and self.stack[self.pointer] == "[":
                self.remove_element()

            elif char == "}" and self.stack[self.pointer] == "{":
                self.remove_element()

        if len(self.stack) != 0:
            return False
        return True


def test_cases():
    """First test case"""

    test_strings = ["[{((()))}]", "{[{((()))}]", "{[{(]"]
    for string in test_strings:
        parentesis_check = ParentesisMatching(string)
        assert parentesis_check.is_valid() is True, f"'{string}' is not a valid string"


def main():
    """Main code here"""

    test_cases()


if __name__ == "__main__":
    main()
