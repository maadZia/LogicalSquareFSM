class State:
    def handle_event(self, context):
        raise NotImplementedError('Subclasses must implement this method')


class State1a(State):
    def handle_event(self, context):
        # Assertion logic
        print('State1a: handling event (a and d)')

        # Transition logic
        event = context.event
        if event == 'tyyuu':
            print('Transitioning to State1b')
            context.set_state(State1b())
            return
        print('No valid transition for event')


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

