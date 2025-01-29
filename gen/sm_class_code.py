class State:
    def __init__(self, state_id, assertion, name=None):
        self.state_id = state_id
        self.assertion = assertion
        self.name = name
    def handle_event(self, context):
        raise NotImplementedError('Subclasses must implement this method')


class State1a(State):
    def __init__(self):
        super().__init__(state_id='1a', assertion='(a and d)', name='None')

    def handle_event(self, context):
        # Assertion logic
        print('State1a: handling event (a and d)')

        print('No transitions defined for State1a')


class State1b(State):
    def __init__(self):
        super().__init__(state_id='1b', assertion='(d and f)', name='None')

    def handle_event(self, context):
        # Assertion logic
        print('State1b: handling event (d and f)')

        print('No transitions defined for State1b')


class State1c(State):
    def __init__(self):
        super().__init__(state_id='1c', assertion='(f and s)', name='None')

    def handle_event(self, context):
        # Assertion logic
        print('State1c: handling event (f and s)')

        print('No transitions defined for State1c')


class StateMachineContext:
    def __init__(self):
        # Attributes
        self.a = False
        self.s = False
        self.d = False
        self.f = False
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

