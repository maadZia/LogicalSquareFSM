from transitions import Machine

states = ['State1a', 'State1b', 'State1c']
transitions = [
    {'trigger': 'cond', 'source': '1a', 'dest': '1b'}, 
]

machine = Machine(states=states, transitions=transitions, initial='State1a')
