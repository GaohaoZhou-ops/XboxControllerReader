import pygame, os, time

def read_gamepad_buttons(joy_device_index:int=0):
    pygame.init()
    pygame.joystick.init()
    
    if pygame.joystick.get_count() == 0:
        print("No joystick detected, pygame.joystick.get_count()=0")
        return None
    
    joystick = pygame.joystick.Joystick(joy_device_index)
    joystick.init()
    
    button_states = {}
    
    try:
        while True:
            time.sleep(0.1)
            pygame.event.pump()
            button_states = []
            balls_states = []
            axes_states = []
            hat_states = []
            for i in range(joystick.get_numbuttons()):
                button_states.append(joystick.get_button(i))
            for i in range(joystick.get_numballs()):
                balls_states.append(joystick.get_ball(i))
            for i in range(joystick.get_numaxes()):
                axes_states.append(joystick.get_axis(i))
            for i in range(joystick.get_numhats()):
                hat_states.append(joystick.get_hat(i))
            print('-' * 50)
            print(f'Button {len(button_states)}: {button_states}')
            print(f'Balls  {len(balls_states)}: {balls_states}')
            print(f'Axes   {len(axes_states)}: {axes_states}')
            print(f'Hat    {len(hat_states)}: {hat_states}')
    except KeyboardInterrupt:
        print("JoyStick Read Done")
    finally:
        pygame.quit()
    
    return button_states

if __name__ == '__main__':
    read_gamepad_buttons(0)