def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' characters.

    Args:
    - text (str): The input text.

    Raises:
    - TypeError: If text is not a string.
    """

    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty string to store the indented text
    indented_text = ""

    # Iterate through each character in the input text
    for char in text:
        # Append the current character to the indented_text
        indented_text += char

        # Check if the current character is '.', '?', or ':'
        if char in ['.', '?', ':']:
            # Add 2 new lines after the punctuation mark
            indented_text += '\n\n'

    # Print the resulting indented text
    print(indented_text, end='')
