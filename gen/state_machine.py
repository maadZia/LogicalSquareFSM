class State:
    def handle_event(self, context):
        raise NotImplementedError('Subclasses must implement this method')


class State1a(State):
    def handle_event(self, context):
        # Assertion logic
        print('State1a: handling event (a and i)')

        # Transition logic
        event = context.event
        if event == 'c1':
            print('Transitioning to State1b')
            context.set_state(State1b())
            return
        if event == 'c2':
            print('Transitioning to State2a')
            context.set_state(State2a())
            return
        print('No valid transition for event')


class State1b(State):
    def handle_event(self, context):
        # Assertion logic
        print('State1b: handling event (i and o)')

        print('No transitions defined for State1b')


class State2a(State):
    def handle_event(self, context):
        # Assertion logic
        print('State2a: handling event (ii and oo)')

        print('No transitions defined for State2a')


class State2b(State):
    def handle_event(self, context):
        # Assertion logic
        print('State2b: handling event (oo and ee)')

        # Transition logic
        event = context.event
        if event == 'c3':
            print('Transitioning to State1b')
            context.set_state(State1b())
            return
        print('No valid transition for event')


class StateMachineContext:
    def __init__(self):
        # Attributes
        self.a = False
        self.e = False
        self.i = False
        self.o = False
        self.ee = False
        self.ii = False
        self.oo = False
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

