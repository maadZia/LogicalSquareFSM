from transitions import Machine

states = ['State1b', 'State1c', 'State2a', 'State2b', 'State2c']
transitions = [
    {'trigger': 'event1', 'source': '1b', 'dest': '1c'}, 
    {'trigger': 'event2', 'source': '1b', 'dest': '2a'}, 
]

machine = Machine(states=states, transitions=transitions, initial='State1b')
