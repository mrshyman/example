def on_forever():
    pass
    basic.show_icon(IconNames.HEART)
basic.forever(on_forever)

def on_button_pressed_a():
    pass
    basic.show_icon(IconNames.SURPRISED)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pass
    basic.show_icon(IconNames.SNAKE)
input.on_button_pressed(Button.B, on_button_pressed_b)