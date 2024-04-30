require "layouts/colors"

button_state = {}

function button_state:new(pixel)
    local obj = {}
    obj.parent = self

    obj.color = colors.off
    obj.pressed = false
    obj.pixel = pixel

    return obj
end