from PyQt5.QtCore import QState, QStateMachine

machine = QStateMachine()

State1a = QState()
machine.addState(State1a)
State1b = QState()
machine.addState(State1b)
State1c = QState()
machine.addState(State1c)

# Define transitions
State1a.addTransition(State1b)

# Set initial state
machine.setInitialState(State1a)
machine.start()

# Example usage:
print('Qt State Machine initialized and running')
