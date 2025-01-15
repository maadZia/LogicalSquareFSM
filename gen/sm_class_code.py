class State:
    def handle_event(self, context):
        raise NotImplementedError('Subclasses must implement this method')


class State1b(State):
    def handle_event(self, context):
        # Assertion logic
        print('State1b: handling event (d and f)')

        print('No transitions defined for State1b')


class State1c(State):
    def handle_event(self, context):
        # Assertion logic
        print('State1c: handling event (f and s)')

        print('No transitions defined for State1c')


class State2a(State):
    def handle_event(self, context):
        # Assertion logic
        print('State2a: handling event (e and t)')

        print('No transitions defined for State2a')


class State2b(State):
    def handle_event(self, context):
        # Assertion logic
        print('State2b: handling event (t and y)')

        print('No transitions defined for State2b')


class State2c(State):
    def handle_event(self, context):
        # Assertion logic
        print('State2c: handling event (y and r)')

        print('No transitions defined for State2c')


class StateMachineContext:
    def __init__(self):
        # Attributes
        self.a = False
        self.s = False
        self.d = False
        self.f = False
        self.e = False
        self.r = False
        self.t = False
        self.y = False
        self.event = None

        # Initial state
        self.current_state = State1b()

    def set_state(self, state):
        print(f'Transitioning to {state.__class__.__name__}')
        self.current_state = state

    def handle_event(self, event):
        if self.current_state is None:
            print('Error: No state to handle event')
            return
        self.event = event
        self.current_state.handle_event(self)

