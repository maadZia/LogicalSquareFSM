from transitions import Machine

states = ['State1a', 'State1b', 'State1c']
transitions = [
]

machine = Machine(states=states, transitions=transitions, initial='State1a')
