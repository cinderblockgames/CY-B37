require "keybow"
require "layouts/button_state"

buttons = {}

-- Keybow MINI is upside down in CY-B37, so these are reversed numerically.
buttons.left = button_state:new(2)
buttons.middle = button_state:new(1)
buttons.right = button_state:new(0)

function buttons.setup()
    keybow.use_mini()
    keybow.auto_lights(false)
    keybow.clear_lights()

    _G.handle_key_00 = function(pressed)
        handle_minikey_02(pressed)
    end
    _G.handle_key_06 = function(pressed)
        handle_minikey_00(pressed)
    end
end

function buttons.set(button, color)
    keybow.set_pixel(button.pixel, table.unpack(color))
    button.color = color
end

function buttons.flip(button, color)
    if button.color == colors.off then
        buttons.set(button, color)
    else
        buttons.set(button, colors.off)
    end
end

function buttons.clear()
    buttons.set(buttons.left, colors.off)
    buttons.set(buttons.middle, colors.off)
    buttons.set(buttons.right, colors.off)
end