from PyQt5.QtCore import QState, QStateMachine

machine = QStateMachine()

State1a = QState()
machine.addState(State1a)
State1b = QState()
machine.addState(State1b)
State1c = QState()
machine.addState(State1c)
State2a = QState()
machine.addState(State2a)
State2b = QState()
machine.addState(State2b)
State2c = QState()
machine.addState(State2c)

# Define transitions
State1a.addTransition(State1b)
State1a.addTransition(State2a)
State2c.addTransition(State2a)

# Set initial state
machine.setInitialState(State1a)
machine.start()

# Example usage:
print('Qt State Machine initialized and running')
