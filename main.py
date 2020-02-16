import os

import game
import drawing_tools
import tank

player = tank.Tank()
player.create_canvas()
player.set_zone()
elem = {}
elem['x'] = player.postion['x']
elem['y'] = player.postion['y']
elem['face'] = player.face

player.render()

drawing_tools.Draw().draw_elem("@")


from pynput import keyboard

def on_press(key):
    try:
        if key == keyboard.KeyCode.from_char("a"):
            print("Moving Left")
            player.create_canvas()
            player.set_zone()
            player.move_left()
            player.update(player.postion['x'], player.postion['y'], player.face)
            player.render()
        elif key == keyboard.KeyCode.from_char("d"):
            print("Moving Right")
            player.create_canvas()
            player.set_zone()
            player.move_right()
            player.update(player.postion['x'], player.postion['y'], player.face)
            player.render()
        elif key == keyboard.KeyCode.from_char("w"):
            print("Moving Up")
            player.create_canvas()
            player.set_zone()
            player.move_up()
            player.update(player.postion['x'], player.postion['y'], player.face)
            player.render()
        elif key == keyboard.KeyCode.from_char("s"):
            print("Moving Down")
            player.create_canvas()
            player.set_zone()
            player.move_down()
            player.update(player.postion['x'], player.postion['y'], player.face)
            player.render()
        else:
            print("Not moving")
    except AttributeError:
        print("No More")

def on_release(key):
    if key == keyboard.KeyCode.from_char("a"):
        print("Moving Left")
        player.create_canvas()
        player.set_zone()
        player.move_left()
        player.update(player.postion['x'], player.postion['y'], player.face)
        player.render()
    elif key == keyboard.KeyCode.from_char("d"):
        print("Moving Right")
        player.create_canvas()
        player.set_zone()
        player.move_right()
        player.update(player.postion['x'], player.postion['y'], player.face)
        player.render()
    elif key == keyboard.KeyCode.from_char("w"):
        print("Moving Up")
        player.create_canvas()
        player.set_zone()
        player.move_up()
        player.update(player.postion['x'], player.postion['y'], player.face)
        player.render()
    elif key == keyboard.KeyCode.from_char("s"):
        print("Moving Down")
        player.create_canvas()
        player.set_zone()
        player.move_down()
        player.update(player.postion['x'], player.postion['y'], player.face)
        player.render()
    else:
        print("Not moving")


    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()