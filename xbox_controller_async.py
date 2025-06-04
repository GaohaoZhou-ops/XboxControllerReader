import pygame
import asyncio
from typing import List, Tuple

class XBoxControllerReaderAsync:
    def __init__(self, joy_device_index: int = 0, poll_interval: float = 0.05):
        self.joy_device_index = joy_device_index
        self.poll_interval = poll_interval

        self.button_states: List[int] = []
        self.ball_states: List[Tuple[int, int]] = []
        self.axis_states: List[float] = []
        self.hat_states: List[Tuple[int, int]] = []

        self._running = False
        self._task = None
        self._joystick = None

    async def start(self):
        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() == 0:
            raise RuntimeError("No joystick detected, pygame.joystick.get_count()=0")

        self._joystick = pygame.joystick.Joystick(self.joy_device_index)
        self._joystick.init()

        self._running = True
        self._task = asyncio.create_task(self._poll_loop())

    async def stop(self):
        self._running = False
        if self._task:
            await self._task
        pygame.quit()

    async def _poll_loop(self):
        while self._running:
            pygame.event.pump()
            self.button_states = [
                self._joystick.get_button(i) for i in range(self._joystick.get_numbuttons())
            ]
            self.ball_states = [
                self._joystick.get_ball(i) for i in range(self._joystick.get_numballs())
            ]
            self.axis_states = [
                self._joystick.get_axis(i) for i in range(self._joystick.get_numaxes())
            ]
            self.hat_states = [
                self._joystick.get_hat(i) for i in range(self._joystick.get_numhats())
            ]
            await asyncio.sleep(self.poll_interval)

    def get_button_states(self) -> List[int]:
        return self.button_states

    def get_axis_states(self) -> List[float]:
        return self.axis_states

    def get_ball_states(self) -> List[Tuple[int, int]]:
        return self.ball_states

    def get_hat_states(self) -> List[Tuple[int, int]]:
        return self.hat_states

