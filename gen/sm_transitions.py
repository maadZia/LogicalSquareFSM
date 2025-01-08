from transitions import Machine

states = ['State1b', 'State1c', 'State2a', 'State2c', 'State3a', 'State3b', 'State3c']
transitions = [
]

machine = Machine(states=states, transitions=transitions, initial='State1b')
