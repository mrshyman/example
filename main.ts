input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Surprised)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Snake)
    music.play(music.stringPlayable("A F E F D G E F ", 120), music.PlaybackMode.UntilDone)
})
basic.forever(function () {
    basic.showIcon(IconNames.Heart)
})
