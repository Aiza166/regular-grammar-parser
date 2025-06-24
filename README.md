# Regular Grammar Parser

A Python-based command-line tool to define and parse regular grammars, generate symbolic regular expressions, simulate finite automata, and test string acceptance based on user-defined grammar rules.

---

📄 Description  
This project was developed as part of an academic course on automata theory. It allows users to input grammar rules in right-linear form (e.g., `A -> aB | b`) and test whether specific strings can be derived from the grammar. The tool simulates how regular languages relate to finite automata and demonstrates the connection between regular grammars, regular expressions, and language recognition.

---

⚙️ Features  

- **Grammar Rule Parsing**  
  Accepts multiple productions per non-terminal in the format `A -> aB | b`. Validates structure and parses rules interactively.

- **Symbolic Regex Generation**  
  Converts the input grammar into a symbolic regular expression using recursive expansion logic. Helps visualize language generation patterns.

- **Transition Table Construction**  
  Automatically builds a state transition table based on grammar rules, mapping terminals to next states.

- **Finite Automaton Simulation**  
  Recursively evaluates input strings against the constructed transitions to determine acceptance or rejection.

- **Interactive CLI Interface**  
  Users can test strings in real time after defining grammar rules. The program reports whether each string is accepted by the defined grammar.

---

🧰 Tech Stack  
- Python 3  
- Regular Expressions (`re` module)  
- Command-line interface (CLI)

---

🛠 Getting Started  

1. Clone the repository  
2. Run the parser:
   ```bash
   python regular_grammar_parser.py
3. Input grammar rules in the form S -> aA | b

4. Test strings interactively to check if they are accepted by the grammar

---

👩‍💻 Author
Aiza Gazyani

---

🪪 License
This project is licensed under the MIT License.
