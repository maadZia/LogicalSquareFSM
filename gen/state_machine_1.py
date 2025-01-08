class State:
    def handle_event(self, context):
        raise NotImplementedError('Subclasses must implement this method')


class State1a(State):
    def handle_event(self, context):
        # Assertion logic
        print('State1a: Name1: handling event (a and c)')

        # Transition logic
        event = context.event
        if event == 'cond1':
            print('Transitioning to State1b')
            context.set_state(State1b())
            return
        if event == 'cond2':
            print('Transitioning to State2a')
            context.set_state(State2a())
            return
        print('No valid transition for event')


class State1b(State):
    def handle_event(self, context):
        # Assertion logic
        print('State1b: Name2: handling event (c and d)')

        print('No transitions defined for State1b')


class State2a(State):
    def handle_event(self, context):
        # Assertion logic
        print('State2a: Name3: handling event (a and w)')

        print('No transitions defined for State2a')


class State2b(State):
    def handle_event(self, context):
        # Assertion logic
        print('State2b: handling event (w and e)')

        print('No transitions defined for State2b')


class State2c(State):
    def handle_event(self, context):
        # Assertion logic
        print('State2c: handling event (e and q)')

        # Transition logic
        event = context.event
        if event == 'cond3':
            print('Transitioning to State2a')
            context.set_state(State2a())
            return
        print('No valid transition for event')


class StateMachineContext:
    def __init__(self):
        # Attributes
        self.a = False
        self.b = False
        self.c = False
        self.d = False
        self.q = False
        self.w = False
        self.e = False
        self.event = None

        # Initial state
        self.current_state = State1a()

    def set_state(self, state):
        print(f'Transitioning to {state.__class__.__name__}')
        self.current_state = state

    def handle_event(self, event):
        if self.current_state is None:
            print('Error: No state to handle event')
            return
        self.event = event
        self.current_state.handle_event(self)

