class MyInt(int):
    """MyInt class inheriting from int with inverted == and != operators."""

    def __eq__(self, other):
        """Override the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator."""
        return super().__eq__(other)

