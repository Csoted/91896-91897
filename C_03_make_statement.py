# Function go here
def make_statement(statement, decoration, lines=1):
    """Create headings (3 lines), subheadings (2 lines) and emphasise text / mini-heading (1 line). Only use emoji for
   single line statements"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)

    elif lines == 2:
        print(middle)
        print(top_bottom)

    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


# Main Routine goes where
make_statement("Programming is Fun!", "=", 3)
make_statement("Programming is Still Fun!", "*", 2)
make_statement("Emoji in Action!", "👍")
