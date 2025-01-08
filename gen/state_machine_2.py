from transitions import Machine

states = ['State1a', 'State1b', 'State2a', 'State2b', 'State2c']
transitions = [
    {'trigger': 'cond1', 'source': '1a', 'dest': '1b'}, 
    {'trigger': 'cond2', 'source': '1a', 'dest': '2a'}, 
    {'trigger': 'codn3', 'source': '2a', 'dest': '1b'}, 
]

machine = Machine(states=states, transitions=transitions, initial='State 0')
