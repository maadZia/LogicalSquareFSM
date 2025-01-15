from transitions import Machine

states = ['State1b', 'State1c', 'State2a', 'State2b', 'State2c']
transitions = [
]

machine = Machine(states=states, transitions=transitions, initial='State1b')
