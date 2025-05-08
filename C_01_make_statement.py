# Function go here
def make_statement(statement, decoration):
    """Emphasise headings by adding decoration
   at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


# Main Routine goes where
make_statement("Programming is Fun!", "👍")
