require "layouts/buttons"
require "layouts/colors"

spike = {}

function spike:new()
    local obj = {}
    setmetatable(obj, self)
    self.__index = self
    return obj
end

-- Game

function spike:start()
    buttons.clear()
    -- set image
end

-- If you press the current round button, reset to no round.  If you press a different round button, move to that round.

function spike:left()
    if buttons.left.color == colors.green and buttons.middle.color == colors.off and buttons.right.color == colors.off then
        spike:start()
    else
        buttons.set(buttons.left, colors.green)
        buttons.set(buttons.middle, colors.off)
        buttons.set(buttons.right, colors.off)

        -- set image
    end
end

function spike:middle()
    if buttons.middle.color == colors.green and buttons.right.color == colors.off then
        spike:start()
    else
        buttons.set(buttons.left, colors.green)
        buttons.set(buttons.middle, colors.green)
        buttons.set(buttons.right, colors.off)

        -- set image
    end
end

function spike:right()
    if buttons.right.color == colors.red then
        spike:start()
    else
        buttons.set(buttons.left, colors.green)
        buttons.set(buttons.middle, colors.green)
        buttons.set(buttons.right, colors.red)

        -- set image
    end
end