namespace SpriteKind {
    export const PowerUps = SpriteKind.create()
    export const NotPartOfTheGame = SpriteKind.create()
    export const WhatIsThis = SpriteKind.create()
    export const Animations = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.PowerUps, function (sprite, otherSprite) {
    music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
    Strawberry.setPosition(randint(0, 160), randint(0, 120))
    info.changeScoreBy(25)
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    while (controller.up.isPressed()) {
        Character.setImage(assets.image`Back Walk 0`)
        pause(100)
        Character.setImage(assets.image`Back Walk 1`)
        pause(100)
        Character.setImage(assets.image`Back Walk 2`)
        pause(100)
    }
    Character.setImage(assets.image`Back Walk 0`)
})
info.onScore(1000, function () {
    Hamburger = sprites.create(assets.image`Hamburger`, SpriteKind.WhatIsThis)
    Character.sayText("Bro what is this?!", 5000, false)
    pause(5000)
    Hamburger.setImage(assets.image`BurgerWithSpikes`)
    Hamburger.sayText("How DARE YOU eat all the apples", 5000, false)
    pause(5000)
    Hamburger.sayText("Your DEAD", 2000, false)
    pause(2000)
    canMove = false
    Hamburger.sayText("Ahhh Take THIS", 2000, false)
    pause(5000)
    Hamburger.sayText("Can't move huh?", 2000, false)
    pause(5000)
    canMove = true
    Hamburger.sayText("Hhh...HOW?!", 2000, false)
    pause(5000)
    Boss_Fight = true
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    while (controller.left.isPressed()) {
        Character.setImage(assets.image`Left Walk 0`)
        pause(100)
        Character.setImage(assets.image`Left Walk 1`)
        pause(100)
    }
    Character.setImage(assets.image`Left Walk Idle`)
})
info.onScore(30, function () {
    Strawberry = sprites.create(assets.image`Strawberry`, SpriteKind.PowerUps)
    Strawberry.setPosition(randint(0, 160), randint(0, 120))
    Character.sayText("That's uhh new?", 5000, false)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    while (controller.right.isPressed()) {
        Character.setImage(assets.image`Right Walk 0`)
        pause(100)
        Character.setImage(assets.image`Right Walk 1`)
        pause(100)
    }
    Character.setImage(assets.image`Right Walk Idle`)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.NotPartOfTheGame, function (sprite, otherSprite) {
    music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
    Cherry.setPosition(randint(0, 160), randint(0, 120))
    info.changeScoreBy(50)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    while (controller.down.isPressed()) {
        Character.setImage(assets.image`Front Walk 1`)
        pause(100)
        Character.setImage(assets.image`Front Walk 2`)
        pause(100)
        Character.setImage(assets.image`Front Walk 3`)
        pause(100)
    }
    Character.setImage(assets.image`Front Walk 0`)
})
info.onScore(500, function () {
    Cherry = sprites.create(assets.image`Cherry`, SpriteKind.NotPartOfTheGame)
    Cherry.setPosition(randint(0, 160), randint(0, 120))
    Character.sayText("Cherry's? That's not part of the game?", 5000, false)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
    Apple.setPosition(randint(0, 160), randint(0, 120))
    info.changeScoreBy(1)
})
let Death_Animation: Sprite = null
let Cherry: Sprite = null
let Boss_Fight = false
let Hamburger: Sprite = null
let Strawberry: Sprite = null
let Apple: Sprite = null
let Character: Sprite = null
let canMove = false
canMove = true
Character = sprites.create(assets.image`Front Walk 0`, SpriteKind.Player)
Apple = sprites.create(assets.image`Apple0`, SpriteKind.Food)
Character.setStayInScreen(true)
tiles.setCurrentTilemap(tilemap`level`)
Apple.setPosition(randint(0, 160), randint(0, 120))
controller.moveSprite(Character)
Character.sayText("Collect as many apples as possible!", 2000, false)
game.onUpdate(function () {
    if (canMove == true) {
        controller.moveSprite(Character, 100, 100)
    } else {
        controller.moveSprite(Character, 0, 0)
    }
})
forever(function () {
    if (Boss_Fight == true) {
        Hamburger.follow(Character, 30)
        Hamburger.sayText("Ahhh Take THIS", 2000, false)
        if (Character.overlapsWith(Hamburger)) {
            canMove = false
            Hamburger.sayText("HAHAHAAA... I GOT YOU!", 2000, false)
            pause(2000)
            sprites.destroyAllSpritesOfKind(SpriteKind.Player)
            sprites.destroyAllSpritesOfKind(SpriteKind.Projectile)
            sprites.destroyAllSpritesOfKind(SpriteKind.Food)
            sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
            sprites.destroyAllSpritesOfKind(SpriteKind.PowerUps)
            sprites.destroyAllSpritesOfKind(SpriteKind.NotPartOfTheGame)
            sprites.destroyAllSpritesOfKind(SpriteKind.WhatIsThis)
            tiles.setCurrentTilemap(tilemap`Death Animation`)
            Death_Animation = sprites.create(assets.image`Death 1`, SpriteKind.Animations)
            music.play(music.melodyPlayable(music.smallCrash), music.PlaybackMode.UntilDone)
            pause(500)
            Death_Animation = sprites.create(assets.image`Death 2`, SpriteKind.Animations)
            music.play(music.melodyPlayable(music.smallCrash), music.PlaybackMode.UntilDone)
            pause(500)
            Death_Animation = sprites.create(assets.image`Death 1`, SpriteKind.Animations)
            music.play(music.melodyPlayable(music.smallCrash), music.PlaybackMode.UntilDone)
            pause(500)
            Death_Animation = sprites.create(assets.image`Death 2`, SpriteKind.Animations)
            music.play(music.melodyPlayable(music.smallCrash), music.PlaybackMode.UntilDone)
            pause(500)
            Death_Animation = sprites.create(assets.image`Death 1`, SpriteKind.Animations)
            music.play(music.melodyPlayable(music.smallCrash), music.PlaybackMode.UntilDone)
            pause(500)
            Death_Animation = sprites.create(assets.image`Death 3`, SpriteKind.Animations)
            music.play(music.melodyPlayable(music.smallCrash), music.PlaybackMode.UntilDone)
            pause(5000)
            game.gameOver(false)
        }
    }
})
forever(function () {
    if (Boss_Fight == true) {
        pause(10000)
    }
})
