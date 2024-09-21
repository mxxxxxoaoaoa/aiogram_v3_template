def validate_markdown(string):
    string = str(string)
    quotes = [
        "`",
        "_",
        "*",
        "~",
        "[",
        "]",
        ">",
        "#",
        "+",
        "=",
        "|",
        "{",
        "}",
        "!",
        "-",
        "(",
        ")",
        "."
    ]
    for quote in quotes:
        string = string.replace(quote, "\{}".format(quote))
    return string

