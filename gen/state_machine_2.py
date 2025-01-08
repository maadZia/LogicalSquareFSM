from transitions import Machine

states = ['State1a', 'State1b', 'State2a', 'State2b', 'State2c']
transitions = [
    {'trigger': 'cond1', 'source': '1a', 'dest': '1b'}, 
    {'trigger': 'cond2', 'source': '1a', 'dest': '2a'}, 
    {'trigger': 'cond3', 'source': '2c', 'dest': '2a'}, 
]

machine = Machine(states=states, transitions=transitions, initial='State 0')
