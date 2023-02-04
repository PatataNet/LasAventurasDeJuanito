@namespace
class SpriteKind:
    Nube = SpriteKind.create()

def on_overlap_tile(sprite, location):
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    global salto
    Juanito.set_velocity(0, 5)
    salto = 2
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
    """),
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    global salto
    salto = 1
    if Agachado == 1:
        juanA.set_velocity(0, 0)
    elif Agachado == 0:
        Juanito.set_velocity(0, 0)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile3)

def on_a_pressed():
    global salto
    if salto == 1:
        Juanito.set_velocity(0, 0)
        Juanito.y += -40
        pause(300)
        Juanito.set_velocity(0, 50)
        salto = 0
        Juanito.set_velocity(0, 0)
    elif salto == 2:
        Juanito.set_velocity(0, 0)
        Juanito.y += -100
        pause(300)
        Juanito.set_velocity(0, 50)
        salto = 0
        Juanito.set_velocity(0, 0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_b_pressed():
    global juanA, Agachado
    juanA = sprites.create(assets.image("""
        JuanitoAgachado
    """), SpriteKind.player)
    juanA.x = Juanito.x
    juanA.y = Juanito.y
    controller.move_sprite(juanA, 100, 0)
    sprites.destroy(Juanito)
    Agachado = 1
    juanA.set_stay_in_screen(True)
    scene.camera_follow_sprite(juanA)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_overlap_tile4(sprite4, location4):
    global salto
    salto = 0
    if Agachado == 1:
        juanA.set_velocity(0, 50)
    elif Agachado == 0:
        Juanito.set_velocity(0, 50)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        transparency16
    """),
    on_overlap_tile4)

def on_b_released():
    global Juanito, Agachado
    Juanito = sprites.create(assets.image("""
        Juanito
    """), SpriteKind.player)
    Juanito.x = juanA.x
    Juanito.y = juanA.y
    controller.move_sprite(Juanito, 100, 0)
    sprites.destroy(juanA)
    Agachado = 0
    Juanito.set_stay_in_screen(True)
    scene.camera_follow_sprite(Juanito)
controller.B.on_event(ControllerButtonEvent.RELEASED, on_b_released)

juanA: Sprite = None
Agachado = 0
salto = 0
Juanito: Sprite = None
scene.set_background_color(9)
tiles.set_current_tilemap(tilemap("""
    nivel1
"""))
Juanito = sprites.create(assets.image("""
    Juanito
"""), SpriteKind.player)
Juanito.set_position(10, 40)
Juanito.set_stay_in_screen(True)
controller.move_sprite(Juanito, 100, 0)
scene.camera_follow_sprite(Juanito)
tiles.set_wall_at(tiles.get_tile_location(0, 0), True)