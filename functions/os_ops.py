from AppOpener import open
from pynput.keyboard import Controller,Key
import time

def open_app(app):
    open(app)

def increase_volume():
    keyboard = Controller()
    for i in range(10):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        time.sleep(0.1)

def decrease_volume():
    keyboard = Controller()
    for i in range(10):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        time.sleep(0.1)

def mute_volume():
    keyboard = Controller()
    keyboard.press(Key.media_volume_mute)
    keyboard.release(Key.media_volume_mute)
    time.sleep(0.1)

def play_next():
    keyboard = Controller()
    keyboard.press(Key.media_next)
    keyboard.release(Key.media_next)
    time.sleep(0.1)

def play_previous():
    keyboard = Controller()
    keyboard.press(Key.media_previous)
    keyboard.release(Key.media_previous)
    time.sleep(0.1)

def pause():
    keyboard = Controller()
    keyboard.press(Key.media_play_pause)
    keyboard.release(Key.media_play_pause)
    time.sleep(0.1)