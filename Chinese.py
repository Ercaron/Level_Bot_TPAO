import time
import threading
from pynput.mouse import Button, Controller
from pynput import keyboard


button = Button.left
key_meditate = keyboard.KeyCode(char='q')
lanzar_btn_pos = (1057, 485)
current = set()

INTERACT_KEYS = [
    { keyboard.KeyCode(char='x'), keyboard.KeyCode(char='c')}
   # {keyboard.Key.shift, keyboard.KeyCode(char='E')}
]

CLOSE_KEYS = [
    {keyboard.KeyCode(char='x'), keyboard.KeyCode(char='b')}
    #{keyboard.Key.shift, keyboard.KeyCode(char='R')}
]


class ClickMouse(threading.Thread):
    start_pos = (0,0)
    def __init__(self, button):
        super(ClickMouse, self).__init__()
        print("Init ClickMouse")
        self.button = button
        self.clicking = False
        self.running= True

    def change_clicking_state(self):
        self.clicking = not self.clicking

    def stop_clicking(self):
        self.clicking = False
    
    def exit(self):
        self.stop_clicking()
        self.running = False
    
    def run(self):
        while self.running:
            while self.clicking:
                mouse.position = lanzar_btn_pos
                mouse.click(self.button)
                mouse.position = self.start_pos
                time.sleep(0.05)
                mouse.click(self.button)
                keyboard.Controller().press(key_meditate)
                time.sleep(0.025)
                keyboard.Controller().release(key_meditate)
                time.sleep(0.05)

                

mouse = Controller()
click_thread = ClickMouse(button)
click_thread.start()



def on_press(key):
    
    #If one of the action keys is pressed, we add it to the list
    if any([key in COMBO for COMBO in INTERACT_KEYS]):
        if(not key in current):
            current.add(key)      
        
        #If all of the action required keys are pressed, change the state of the bot
        if any(all(k in current for k in COMBO) for COMBO in INTERACT_KEYS):
            click_thread.start_pos = mouse.position
            click_thread.change_clicking_state()
            print("Change State")


    #Same as above but for closing the bot
    if any([key in COMBO for COMBO in CLOSE_KEYS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in CLOSE_KEYS):
            click_thread.exit()
            listener.stop()
            print("Close App")
   
    

def on_release(key):
    if any([key in COMBO for COMBO in INTERACT_KEYS]):
        if key in current:
            current.remove(key)
    elif any([key in COMBO for COMBO in CLOSE_KEYS]):
        if key in current:
            current.remove(key)

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    print("Input Available")
    listener.join()