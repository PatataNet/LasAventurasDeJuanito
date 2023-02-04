namespace SpriteKind {
    export const Nube = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile0`, function (sprite, location) {
    game.gameOver(true)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`transparency16`, function (sprite4, location4) {
    salto = 0
    if (Agachado == 1) {
        juanA.setVelocity(0, 50)
    } else if (Agachado == 0) {
        Juanito.setVelocity(0, 50)
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (salto == 1) {
        Juanito.setVelocity(0, 0)
        Juanito.y += -40
        pause(300)
        Juanito.setVelocity(0, 50)
        salto = 0
        Juanito.setVelocity(0, 0)
    } else if (salto == 2) {
        Juanito.setVelocity(0, 0)
        Juanito.y += -100
        pause(300)
        Juanito.setVelocity(0, 50)
        salto = 0
        Juanito.setVelocity(0, 0)
    }
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    juanA = sprites.create(assets.image`JuanitoAgachado`, SpriteKind.Player)
    juanA.x = Juanito.x
    juanA.y = Juanito.y
    controller.moveSprite(juanA, 100, 0)
    sprites.destroy(Juanito)
    Agachado = 1
    juanA.setStayInScreen(true)
    scene.cameraFollowSprite(juanA)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile1`, function (sprite2, location2) {
    Juanito.setVelocity(0, 5)
    salto = 2
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile`, function (sprite3, location3) {
    salto = 1
    if (Agachado == 1) {
        juanA.setVelocity(0, 0)
    } else if (Agachado == 0) {
        Juanito.setVelocity(0, 0)
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile3`, function (sprite2, location2) {
    game.gameOver(false)
})
controller.B.onEvent(ControllerButtonEvent.Released, function () {
    Juanito = sprites.create(assets.image`Juanito`, SpriteKind.Player)
    Juanito.x = juanA.x
    Juanito.y = juanA.y
    controller.moveSprite(Juanito, 100, 0)
    sprites.destroy(juanA)
    Agachado = 0
    Juanito.setStayInScreen(true)
    scene.cameraFollowSprite(Juanito)
})
let juanA: Sprite = null
let Agachado = 0
let salto = 0
let Juanito: Sprite = null
scene.setBackgroundColor(9)
tiles.setCurrentTilemap(tilemap`nivel1`)
Juanito = sprites.create(assets.image`Juanito`, SpriteKind.Player)
Juanito.setPosition(10, 40)
Juanito.setStayInScreen(true)
controller.moveSprite(Juanito, 100, 0)
scene.cameraFollowSprite(Juanito)
tiles.setWallAt(tiles.getTileLocation(0, 0), true)
