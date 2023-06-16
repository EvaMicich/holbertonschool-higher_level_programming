#!/usr/bin/python3
"""
Module: 5-text_indentation
text printed with 2 new lines after chars .?:
"""


def text_indentation(text):
    """
    indents text

    argument:
    text: text to be printed with 2 new lines after chars . ? :

    return:
    void
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text_update = str(text)
    after_new_line = False
    for c in text_update:
        if after_new_line:
            if c == " ":
                continue
            after_new_line = False
        if c == '.' or c == '?' or c == ':':
            print("")
            print("")
            after_new_line = True
        else:
            print(c, end="")
