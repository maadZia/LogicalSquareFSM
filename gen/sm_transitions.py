from transitions import Machine

states = ['State1a', 'State1b', 'State1c']
transitions = [
    {'trigger': 'aa', 'source': '1a', 'dest': '1a'}, 
    {'trigger': 'bb', 'source': '1a', 'dest': '1b'}, 
    {'trigger': 'ee', 'source': '1a', 'dest': '1c'}, 
]

machine = Machine(states=states, transitions=transitions, initial='State1a')
