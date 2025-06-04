import pygame
import threading
import time
from typing import List, Tuple

class XBoxControllerReaderSync:
    def __init__(self, joy_device_index: int = 0, poll_interval: float = 0.05):
        self.joy_device_index = joy_device_index
        self.poll_interval = poll_interval

        self.button_states: List[int] = []
        self.ball_states: List[Tuple[int, int]] = []
        self.axis_states: List[float] = []
        self.hat_states: List[Tuple[int, int]] = []

        self._running = False
        self._thread = None
        self._joystick = None

    def start(self):
        self._running = True
        self._thread = threading.Thread(target=self._poll_loop, daemon=True)
        self._thread.start()

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join()
        pygame.quit()
        print("GamepadReader stopped and pygame quit.")

    def _poll_loop(self):
        print("Initializing pygame...")
        pygame.init()
        pygame.joystick.init()

        count = pygame.joystick.get_count()
        print(f"Detected {count} joystick(s)")

        if count == 0:
            raise RuntimeError("No joystick detected, pygame.joystick.get_count()=0")

        self._joystick = pygame.joystick.Joystick(self.joy_device_index)
        self._joystick.init()
        print(f"Joystick {self._joystick.get_name()} initialized.")
        
        while self._running:
            try:
                pygame.event.pump()
                self.button_states = [
                    self._joystick.get_button(i)
                    for i in range(self._joystick.get_numbuttons())
                ]
                self.ball_states = [
                    self._joystick.get_ball(i)
                    for i in range(self._joystick.get_numballs())
                ]
                self.axis_states = [
                    self._joystick.get_axis(i)
                    for i in range(self._joystick.get_numaxes())
                ]
                self.hat_states = [
                    self._joystick.get_hat(i)
                    for i in range(self._joystick.get_numhats())
                ]
            except pygame.error as e:
                print(f"Pygame error during polling: {e}")
            time.sleep(self.poll_interval)

    def get_button_states(self) -> List[int]:
        return self.button_states

    def get_axis_states(self) -> List[float]:
        return self.axis_states

    def get_ball_states(self) -> List[Tuple[int, int]]:
        return self.ball_states

    def get_hat_states(self) -> List[Tuple[int, int]]:
        return self.hat_states
