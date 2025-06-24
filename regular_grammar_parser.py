# Regular Grammar Parser with Correct Traversal

# Store the grammar
grammar = {}

print("Enter regular grammar rules in the format: Non-terminal -> production1 | production2")
print("Example: S -> aA | bB")
print("Type 'done' when finished.\n")

# Input grammar rules
while True:
    rule = input("Enter a grammar rule (or type 'done' to finish): ")
    if rule.lower() == 'done':
        break
    try:
        lhs, rhs = rule.split("->")
        lhs = lhs.strip()
        productions = [prod.strip() for prod in rhs.split("|")]
        grammar[lhs] = productions
    except ValueError:
        print("Invalid format. Use 'Non-terminal -> production1 | production2'.")

# Function to check if the grammar is complete (i.e., every non-terminal has terminal productions)
def is_grammar_complete():
    for non_terminal, productions in grammar.items():
        # Check if any non-terminal in the productions is defined in the grammar
        for production in productions:
            for symbol in production:
                if symbol.isupper() and symbol not in grammar:
                    return False  # If the non-terminal is not fully defined
    return True

# Function to check if a string is valid according to the grammar
def is_valid(string):
    # First, check if the grammar is complete
    if not is_grammar_complete():
        print("❌ Incomplete grammar: Some non-terminals are not fully defined.")
        exit()
        return False

    current_states = ['S']  # Start from start symbol S
    for char in string:
        next_states = []
        for state in current_states:
            if state in grammar:
                for production in grammar[state]:
                    if len(production) >= 1 and production[0] == char:
                        if len(production) == 2:
                            next_states.append(production[1])  # Non-terminal transition
                        elif len(production) == 1:
                            next_states.append('')  # Accepting state (empty)
        current_states = next_states
        if not current_states:
            return False  # No valid transitions

    # After consuming the string, check if we are at an accepting state
    for state in current_states:
        if state == '' or (state in grammar and any(len(prod) == 1 for prod in grammar[state])):
            return True
    return False

# Input strings to test
print("\nEnter a string to test (or type 'exit' to quit):")
while True:
    string = input("> ")
    if string.lower() == 'exit':
        print("Exiting program...")
        break
    if is_valid(string):
        print(f"✅ '{string}' is a valid string.\n")
    else:
        print(f"❌ '{string}' is NOT a valid string.\n")
