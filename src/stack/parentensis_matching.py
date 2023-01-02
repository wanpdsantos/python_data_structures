class ParentesisMatching:
    """Parentesis Matching checker"""

    def __init__(self, string: str):
        self.pointer = -1
        self.string = string
        self.stack = []

    def _add_element(self, element: str):
        """Add new element to the stack"""

        self.stack.append(element)
        self.pointer += 1

    def _remove_element(self):
        """Remove an element from the stack"""

        self.stack.pop(self.pointer)
        self.pointer -= 1

    def is_valid(self):
        """Check if the string as a valid parentesis matching"""

        for char in self.string:
            if char in ("(", "[", "{"):
                self._add_element(char)
            else:
                if self.pointer < 0:
                    return False
                if char == ")" and self.stack[self.pointer] == "(":
                    self._remove_element()

                elif char == "]" and self.stack[self.pointer] == "[":
                    self._remove_element()

                elif char == "}" and self.stack[self.pointer] == "{":
                    self._remove_element()
        if len(self.stack) == 0:
            return True
        return False
