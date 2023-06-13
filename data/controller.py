import pygame

from data.settings import SCREEN_SIZE, GAME_CAPTION


class Controller():
    """Controls the entire game. Contains the main game loop. Passes events to 
    states and handles updating the current state. """

    def __init__(self):
        self.done = False
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(GAME_CAPTION)
        self.fps = 60
        self.clock = pygame.time.Clock()

    def setup_states(self, states, initial_state):
        """Builds self.states and sets the initial state"""
        self.states = states
        self.state_name = initial_state
        self.state = self.states[self.state_name]

    def event_handler(self):
        """Checks if the game has been quit, and if it hasn't, 
        passes all events to the current state."""
        if pygame.event.get(pygame.QUIT):
            self.done = True
        else:
            self.state.handle_events(pygame.event.get())

    def change_state(self):
        """Changes the state and passes required information to new state."""
        next_state = self.state.next_state
        persistent = self.state.cleanup()
        self.state_name = next_state
        self.state = self.states[self.state_name]
        self.state.start(persistent)

    def update(self, dt):
        """Checks if the game is quit or state is done and updates the state."""
        if self.state.quit:
            self.done = True
        if self.state.done:
            self.change_state()
        self.state.update(dt)

    def draw(self):
        """Renders the current state"""
        self.state.draw(self.screen)

    def run(self):
        """Main game loop"""
        while not self.done:
            dt = self.clock.tick(60) / 1000
            self.event_handler()
            self.update(dt)
            self.draw()
            pygame.display.flip()
