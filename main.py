@namespace
class SpriteKind:
    PowerUps = SpriteKind.create()
    NotPartOfTheGame = SpriteKind.create()
    WhatIsThis = SpriteKind.create()
    Animations = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.UNTIL_DONE)
    Strawberry.set_position(randint(0, 160), randint(0, 120))
    info.change_score_by(25)
sprites.on_overlap(SpriteKind.player, SpriteKind.PowerUps, on_on_overlap)

def on_up_pressed():
    while controller.up.is_pressed():
        Character.set_image(assets.image("""
            Back Walk 0
            """))
        pause(100)
        Character.set_image(assets.image("""
            Back Walk 1
            """))
        pause(100)
        Character.set_image(assets.image("""
            Back Walk 2
            """))
        pause(100)
    Character.set_image(assets.image("""
        Back Walk 0
        """))
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_score():
    global Hamburger, canMove, Boss_Fight
    Hamburger = sprites.create(assets.image("""
            Hamburger
            """),
        SpriteKind.WhatIsThis)
    Character.say_text("Bro what is this?!", 5000, False)
    pause(5000)
    Hamburger.set_image(assets.image("""
        BurgerWithSpiks
        """))
    Hamburger.say_text("How DARE YOU eat all the apples", 5000, False)
    pause(5000)
    Hamburger.say_text("Your DEAD", 2000, False)
    pause(2000)
    canMove = False
    Hamburger.say_text("Ahhh Take THIS", 2000, False)
    pause(5000)
    Hamburger.say_text("Can't move huh?", 2000, False)
    pause(5000)
    canMove = True
    Hamburger.say_text("Hhh...HOW?!", 2000, False)
    pause(5000)
    Boss_Fight = True
info.on_score(1000, on_on_score)

def on_left_pressed():
    while controller.left.is_pressed():
        Character.set_image(assets.image("""
            Left Walk 0
            """))
        pause(100)
        Character.set_image(assets.image("""
            Left Walk 1
            """))
        pause(100)
    Character.set_image(assets.image("""
        Left Walk Idle
        """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_on_score2():
    global Strawberry
    Strawberry = sprites.create(assets.image("""
            Strawberry
            """),
        SpriteKind.PowerUps)
    Strawberry.set_position(randint(0, 160), randint(0, 120))
    Character.say_text("That's uhh new?", 5000, False)
info.on_score(30, on_on_score2)

def on_right_pressed():
    while controller.right.is_pressed():
        Character.set_image(assets.image("""
            Right Walk 0
            """))
        pause(100)
        Character.set_image(assets.image("""
            Right Walk 1
            """))
        pause(100)
    Character.set_image(assets.image("""
        Right Walk Idle
        """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap2(sprite2, otherSprite2):
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.UNTIL_DONE)
    Cherry.set_position(randint(0, 160), randint(0, 120))
    info.change_score_by(50)
sprites.on_overlap(SpriteKind.player,
    SpriteKind.NotPartOfTheGame,
    on_on_overlap2)

def on_down_pressed():
    while controller.down.is_pressed():
        Character.set_image(assets.image("""
            Front Walk 1
            """))
        pause(100)
        Character.set_image(assets.image("""
            Front Walk 2
            """))
        pause(100)
        Character.set_image(assets.image("""
            Front Walk 3
            """))
        pause(100)
    Character.set_image(assets.image("""
        Front Walk 0
        """))
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_on_score3():
    global Cherry
    Cherry = sprites.create(assets.image("""
            Cherry
            """),
        SpriteKind.NotPartOfTheGame)
    Cherry.set_position(randint(0, 160), randint(0, 120))
    Character.say_text("Cherry's? That's not part of the game?", 5000, False)
info.on_score(500, on_on_score3)

def on_on_overlap3(sprite3, otherSprite3):
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.UNTIL_DONE)
    Apple.set_position(randint(0, 160), randint(0, 120))
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap3)

Death_Animation: Sprite = None
Cherry: Sprite = None
Boss_Fight = False
Hamburger: Sprite = None
Strawberry: Sprite = None
Apple: Sprite = None
Character: Sprite = None
canMove = False
canMove = True
Character = sprites.create(assets.image("""
        Front Walk 0
        """),
    SpriteKind.player)
Apple = sprites.create(assets.image("""
    Apple0
    """), SpriteKind.food)
Character.set_stay_in_screen(True)
tiles.set_current_tilemap(tilemap("""
    level
    """))
Apple.set_position(randint(0, 160), randint(0, 120))
controller.move_sprite(Character)
Character.say_text("Collect as many apples as possible!", 2000, False)

def on_on_update():
    if canMove == True:
        controller.move_sprite(Character, 100, 100)
    else:
        controller.move_sprite(Character, 0, 0)
game.on_update(on_on_update)

def on_forever():
    global canMove, Death_Animation
    if Boss_Fight == True:
        Hamburger.follow(Character, 30)
        Hamburger.say_text("Ahhh Take THIS", 2000, False)
        if Character.overlaps_with(Hamburger):
            canMove = False
            Hamburger.say_text("HAHAHAAA... I GOT YOU!", 2000, False)
            pause(2000)
            sprites.destroy_all_sprites_of_kind(SpriteKind.player)
            sprites.destroy_all_sprites_of_kind(SpriteKind.projectile)
            sprites.destroy_all_sprites_of_kind(SpriteKind.food)
            sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
            sprites.destroy_all_sprites_of_kind(SpriteKind.PowerUps)
            sprites.destroy_all_sprites_of_kind(SpriteKind.NotPartOfTheGame)
            sprites.destroy_all_sprites_of_kind(SpriteKind.WhatIsThis)
            tiles.set_current_tilemap(tilemap("""
                Death Animation
                """))
            Death_Animation = sprites.create(assets.image("""
                Death 1
                """), SpriteKind.Animations)
            music.play(music.melody_playable(music.small_crash),
                music.PlaybackMode.UNTIL_DONE)
            pause(500)
            Death_Animation = sprites.create(assets.image("""
                Death 2
                """), SpriteKind.Animations)
            music.play(music.melody_playable(music.small_crash),
                music.PlaybackMode.UNTIL_DONE)
            pause(500)
            Death_Animation = sprites.create(assets.image("""
                Death 1
                """), SpriteKind.Animations)
            music.play(music.melody_playable(music.small_crash),
                music.PlaybackMode.UNTIL_DONE)
            pause(500)
            Death_Animation = sprites.create(assets.image("""
                Death 2
                """), SpriteKind.Animations)
            music.play(music.melody_playable(music.small_crash),
                music.PlaybackMode.UNTIL_DONE)
            pause(500)
            Death_Animation = sprites.create(assets.image("""
                Death 1
                """), SpriteKind.Animations)
            music.play(music.melody_playable(music.small_crash),
                music.PlaybackMode.UNTIL_DONE)
            pause(500)
            Death_Animation = sprites.create(assets.image("""
                Death 3
                """), SpriteKind.Animations)
            music.play(music.melody_playable(music.small_crash),
                music.PlaybackMode.UNTIL_DONE)
            pause(5000)
            game.game_over(False)
forever(on_forever)

def on_forever2():
    if Boss_Fight == True:
        pause(15000)
forever(on_forever2)
