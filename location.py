import defines
import canvas
import tank


# Rewrite this method to universdal update method
# Incoming type -> dict or point
def update():
    """
    This function must creating new canvas with elements what change them position.
    Each of this changes is a one tic
    """
    set_zone()
    player = tank.Tank() # This fragment to be able to movable
    player.set_tank("3")
    canv.get_canvas()[defines.DEFAULT_POSITION["y"]][defines.DEFAULT_POSITION["x"]] = player.create_tank()

# Temporary function
def set_zone():  # may return SIZE
    for x in range(defines.SIZE["height"]):
        for y in range(defines.SIZE["width"]-2):
            if y == 0 or y == defines.SIZE["width"]-3:
                canv.get_canvas()[x][y] = "|"
            elif x == 0 or x == defines.SIZE["height"]-1:
                canv.get_canvas()[x][y] = "-"