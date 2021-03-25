import wrap_py, wrap_py.ru, plan

speed_y = 0

wrap_py.world.create_world(1200, 700)
fd = wrap_py.sprite.add_sprite('rocket_man', 50, 50)
# wrap_py.sprite.change_height_proportionally(fd,100)
wrap_py.world.set_world_background_color_rgb(50, 200, 10)
bi_d = wrap_py.sprite.add_sprite('flappy_bird', 100, 350)
wrap_py.app.set_title('flappy_bird')
wrap_py.sprite.add_sprite('flappy_bird', 500, 350, True, 'img')
ki=wrap_py.sprite.add_sprite('fon',300,100)



@wrap_py.always(20)
def fly():
    global speed_y
    speed_y += 0.02
    de_b = wrap_py.sprite.get_sprite_final_angle(bi_d)
    wrap_py.sprite.move_sprite_by(bi_d, 0, speed_y)
    if 180 != de_b:
        wrap_py.sprite.rotate_to_angle(bi_d, de_b + 1)


@wrap_py.on_key_down(wrap_py.K_SPACE)
def jump():
    global speed_y, be
    speed_y = -1
    wrap_py.sprite.rotate_to_angle(bi_d, speed_y)
