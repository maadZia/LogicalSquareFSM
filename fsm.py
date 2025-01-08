from state import State
from string import ascii_lowercase
from code_generator import (
    generate_class_code,
    generate_code_3,
    generate_code_3_qt,
    generate_assertion_code,
)

class LogicalSquareFSM:
    def __init__(self):
        """
        Tworzy pusty span tree dla FSM.
        """
        self.span_tree = {}  # Drzewo przechowujące stany i przejścia
        self.root = 0  # Korzeń drzewa, reprezentuje initial state
        self.span_tree[self.root] = {"state": "State 0", "children": []}
        self.current_id = 1  # Unikalne ID dla każdego stanu
        self.suffix_index = 0
        self.attributes = []
        self.latest_states = []  # Lista ID stanów, które mogą być rozwinięte
        self.transitions = []  # lista przejść
        self.state_transitions_map = {}

    def add_attribute(self, attribute):
        """
        Dodaje atrybut do listy 'attributes' (jeśli nie istnieje już na liście).
        Usuwamy 'not' tylko w przypadku dodawania do listy atrybutów.
        Jeśli wyrażenie zawiera spacje to zamieniamy je na "_"
        :param attribute: Atrybut do dodania.
        """
        attribute_copy = attribute
        if attribute.lower().startswith("not "):
            attribute_copy = attribute[4:].strip()

        if attribute_copy not in self.attributes and attribute_copy != "true":
            self.attributes.append(attribute_copy)

    def get_next_state_id(self):
        """
        Generuje kolejny identyfikator stanu w formacie {kwadrat_counter}{litera}.
        Przykład: 1a, 1b, 1c, 2a, 2b...
        """
        suffix = ascii_lowercase[self.suffix_index]
        state_id = f"{self.current_id}{suffix}"
        self.suffix_index += 1  # Przejście do następnej litery
        return state_id

    def create_logical_square(self, a, e, i, o):
        """
        Tworzy nowy kwadrat logiczny na podstawie interaktywnych danych wejściowych.
        Obsługuje sytuacje pominięcia dowolnego wierzchołka (A, E, I, O).
        :return: Lista stanów [{A, I}, {I, O}, opcjonalnie {O, E}]
        """
        self.add_attribute(a)
        self.add_attribute(e)
        self.add_attribute(i)
        self.add_attribute(o)

        states = []
        self.suffix_index = 0

        # Logika dla pary (A, I)
        if i != "true" and a != "true":
            state_id = self.get_next_state_id()
            state = State(state_id, f"({a} and {i})")
            states.append(state)
            # self.current_id += 1

        # Logika dla pary (I, O)
        if i != "true" and o != "true":
            state_id = self.get_next_state_id()
            state = State(state_id, f"({i} and {o})")
            states.append(state)
            # self.current_id += 1

        # Logika dla pary (O, E)
        if o != "true" and e != "true":
            state_id = self.get_next_state_id()
            state = State(state_id, f"({o} and {e})")
            states.append(state)
            # self.current_id += 1

        self.current_id += 1
        return states

    def assign_name_to_state(self, state_id, name):
        """
        Przypisuje nazwę do istniejącego stanu na podstawie jego ID.
        :param state_id: ID stanu, któremu chcemy przypisać nazwę.
        :param name: Nowa nazwa stanu.
        """
        if state_id in self.span_tree:
            state = self.span_tree[state_id]["state"]
            if isinstance(state, State):
                state.name = name
                print(f"Przypisano nazwę '{name}' do stanu o ID {state_id}.")
            else:
                print(f"Błąd: Stan o ID {state_id} nie jest instancją klasy State.")
        else:
            print(f"Błąd: Nie znaleziono stanu o ID {state_id}.")

    def add_square(self, a, e, i, o, parent_id=0):
        """
        Dodaje nowy kwadrat logiczny, rozwijając wybrany stan.
        :param parent_id: ID stanu, który będzie rozwijany
        """

        new_states = self.create_logical_square(a, e, i, o)

        # Aktualizuje drzewo: dodaje dzieci do wybranego stanu
        if parent_id in self.span_tree:
            self.span_tree[parent_id]["children"] = [s.state_id for s in new_states]

        # Dodaje nowe stany jako dzieci
        for state in new_states:
            self.span_tree[state.state_id] = {"state": state, "children": []}

        # Aktualizuje listę najnowszych stanów
        self.latest_states = [s.state_id for s in new_states]

    def display_tree(self, node_id=None, level=0, tree_list=None):
        """
        Zwraca drzewo stanów jako listę zagnieżdżonych stringów.
        """
        if node_id is None:
            node_id = self.root

        node = self.span_tree[node_id]["state"]
        tree_str = " " * (2 * level) + str(node) + "\n"  # Dodajemy nową linię po każdym stanie
        for child_id in self.span_tree[node_id]["children"]:
            tree_str += self.display_tree(child_id, level + 1)

        return tree_str

    def add_transition(self, from_state, to_state, event):
        """
        Dodaje przejście między stanami i aktualizuje mapę przejść.
        """
        self.transitions.append((from_state, to_state, event))
        # from_state = int(from_state)
        # to_state = int(to_state)

        if from_state not in self.state_transitions_map:
            self.state_transitions_map[from_state] = {}
        self.state_transitions_map[from_state][event] = to_state

        return f"State{from_state}  ->  State{to_state}  on event  '{event}'"

    def get_initial_state(self):
        initial_states = [state_id for state_id, node in self.span_tree.items() if not node["children"]]
        initial_state_id = min(initial_states)
        return initial_state_id

    def generate_class_code(self):
        return generate_class_code(self)

    def generate_assertion_code(self, assertion):
        return generate_assertion_code(assertion)

    def generate_code_3(self):
        return generate_code_3(self)

    def generate_code_3_qt(self):
        return generate_code_3_qt(self)

    # def generate_class_code(self):
    #     """
    #     Generuje kod klasy maszyny stanowej z dynamicznymi klasami dla aktualnych nierozwiniętych stanów.
    #     """
    #     class_code = ""
    #
    #     # 1. Definiowanie klasy bazowej State
    #     class_code += "class State:\n"
    #     class_code += "    def handle_event(self, context):\n"
    #     class_code += "        raise NotImplementedError('Subclasses must implement this method')\n\n\n"
    #
    #     # 2. Generowanie klas dla aktualnych nierozwiniętych stanów
    #     for state_id, node in self.span_tree.items():
    #         # Sprawdź, czy stan jest nierozwinięty (nie ma dzieci)
    #         if not node["children"]:
    #             state_name = f"State{state_id}"
    #             class_code += f"class {state_name}(State):\n"
    #             class_code += f"    def handle_event(self, context):\n"
    #
    #             # Dodajemy asercje dla stanu (jeśli istnieją)
    #             state = node["state"]
    #             if state:
    #                 assertion = state.assert_state()
    #                 assertion_code = self.generate_assertion_code(assertion)
    #                 if assertion_code:
    #                     class_code += f"        # Assertion logic\n"
    #                     class_code += f"        print('State{state_id}: handling event {assertion}')\n"
    #             class_code += "\n"
    #
    #             # Logika przejść dla tego stanu
    #             transitions_for_state = self.state_transitions_map.get(state_id, {})
    #             if transitions_for_state:
    #                 class_code += f"        # Transition logic\n"
    #                 class_code += "        event = context.event\n"
    #                 for event, to_state in transitions_for_state.items():
    #                     class_code += f"        if event == '{event}':\n"
    #                     class_code += f"            print('Transitioning to State{to_state}')\n"
    #                     class_code += f"            context.set_state(State{to_state}())\n"
    #                     class_code += f"            return\n"
    #                 class_code += f"        print('No valid transition for event')\n"
    #             else:
    #                 class_code += f"        print('No transitions defined for {state_name}')\n"
    #             class_code += "\n\n"
    #
    #
    #     # 3. Generowanie klasy kontekstowej StateMachineContext
    #     class_code += "class StateMachineContext:\n"
    #     class_code += "    def __init__(self):\n"
    #     class_code += "        # Attributes\n"
    #     for attribute in self.attributes:
    #         sanitized_attribute = attribute.replace(" ", "_")
    #         class_code += f"        self.{sanitized_attribute} = False\n"
    #     class_code += "        self.event = None\n"  # Dodanie eventu w kontekście
    #
    #     # Ustalanie stanu początkowego
    #     # initial_states = [state_id for state_id, node in self.span_tree.items() if not node["children"]]
    #     initial_state_id = self.get_initial_state()
    #
    #     if initial_state_id is not None:
    #         class_code += f"\n        # Initial state\n"
    #         class_code += f"        self.current_state = State{initial_state_id}()\n"
    #     else:
    #         class_code += f"\n        # Initial state\n"
    #         class_code += f"        self.current_state = None\n"
    #         class_code += "        print('Error: No initial state available')\n"
    #
    #     # Metoda set_state
    #     class_code += "\n    def set_state(self, state):\n"
    #     class_code += "        print(f'Transitioning to {state.__class__.__name__}')\n"
    #     class_code += "        self.current_state = state\n"
    #
    #     # Metoda handle_event
    #     class_code += "\n    def handle_event(self, event):\n"
    #     class_code += "        if self.current_state is None:\n"
    #     class_code += "            print('Error: No state to handle event')\n"
    #     class_code += "            return\n"
    #     class_code += "        self.event = event\n"  # Ustawienie eventu w kontekście
    #     class_code += "        self.current_state.handle_event(self)\n\n"
    #
    #     return class_code
    #
    # def generate_assertion_code(self, assertion):
    #     """
    #     Generuje kod dla asercji, zamieniając zmienne na self.<zmienna>.
    #     Na przykład: (engine on and not door closed) -> (self.engine_on and not self.door_closed).
    #     """
    #     if assertion.startswith("(") and assertion.endswith(")"):
    #         assertion = assertion[1:-1]  # Usuwamy nawiasy na początku i końcu
    #
    #     tokens = assertion.split()
    #     processed_tokens = []
    #
    #     current_variable = []  # Tymczasowa lista do przechowywania zmiennej wielowyrazowej
    #     for token in tokens:
    #         if token in {"and", "not"}:
    #             if current_variable:  # Jeśli wcześniej zgromadzono zmienną
    #                 variable = "_".join(current_variable)  # Łączymy zmienną wielowyrazową za pomocą podkreślnika
    #                 processed_tokens.append(f"context.{variable}")
    #                 current_variable = []  # Reset tymczasowej listy
    #             processed_tokens.append(token)
    #         else:
    #             current_variable.append(token)
    #
    #     if current_variable:
    #         variable = "_".join(current_variable)
    #         processed_tokens.append(f"context.{variable}")
    #
    #     return " ".join(processed_tokens)
    #
    # def generate_code_3(self):
    #
    #     states = []
    #     for state_id, node in self.span_tree.items():
    #         if not node["children"]:
    #             state_name = f"State{state_id}"
    #             states.append(state_name)
    #
    #     code = "from transitions import Machine\n\n"
    #     code += "states = " + repr(states) + "\n"
    #     code += "transitions = [\n"
    #
    #     for from_state, to_state, event in self.transitions:
    #         code += f"    {{'trigger': '{event}', 'source': '{from_state}', 'dest': '{to_state}'}}, \n"
    #
    #     code += "]\n\n"
    #     code += "machine = Machine(states=states, transitions=transitions, initial='{}')\n".format(
    #         self.span_tree[self.root].get('state'))
    #
    #     return code
    #
    # def generate_code_3_qt(self):
    #
    #     code = "from PyQt5.QtCore import QState, QStateMachine\n\n"
    #     code += "machine = QStateMachine()\n\n"
    #
    #     state_objects = {f'{state_id}': f"State{state_id}" for state_id, node in self.span_tree.items() if
    #                      state_id != 0}
    #     for state, obj_name in state_objects.items():
    #         code += f"{obj_name} = QState()\n"
    #         code += f"machine.addState({obj_name})\n"
    #
    #     code += "\n# Define transitions\n"
    #     for from_state, to_state, event in self.transitions:
    #         print(from_state, to_state, event)
    #         code += f"{state_objects[from_state]}.addTransition({state_objects[to_state]})\n"
    #
    #     initial_state_id = self.get_initial_state()
    #     code += "\n# Set initial state\n"
    #     print(initial_state_id)
    #     print(state_objects.get(initial_state_id))
    #     code += f"machine.setInitialState(State{initial_state_id})\n"
    #
    #     code += "machine.start()\n"
    #     code += "\n# Example usage:\n"
    #     code += "print('Qt State Machine initialized and running')\n"
    #
    #     return code
    #
    # def export_to_dot(self, filename="gen/fsm_tree.dot"):
    #     """
    #     Eksportuje drzewo stanów do pliku w formacie DOT, a następnie generuje obrazek PNG.
    #     """
    #     # Eksport do pliku DOT
    #     with open(filename, "w") as f:
    #         f.write("digraph FSM {\n")
    #         f.write("    rankdir=TB;\n")  # Układ drzewa (od góry do dołu)
    #
    #         for state_id, node in self.span_tree.items():
    #             state_label = str(node["state"])
    #             f.write(f'    {state_id} [label="{state_label}"];\n')
    #             for child_id in node["children"]:
    #                 f.write(f'    {state_id} -> {child_id};\n')
    #
    #         f.write("}\n")
    #     print(f"Drzewo stanów zapisane do pliku {filename}.")
    #
    #     # Konwersja pliku DOT na PNG za pomocą graphviz
    #     try:
    #         # Tworzenie obiektu Source, który obsługuje generowanie obrazu
    #         source = Source.from_file(filename)
    #
    #         # Wskazanie formatu i ścieżki zapisu obrazu PNG
    #         png_filename = filename.replace(".dot", ".png")
    #         source.render(png_filename, format="png", cleanup=True)
    #
    #         print(f"Obrazek PNG zapisany jako {png_filename}.")
    #     except Exception as e:
    #         print(f"Błąd podczas konwersji pliku DOT na PNG: {e}")
