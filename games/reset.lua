require "layouts/buttons"
require "layouts/colors"

reset = {}

function reset:new()
    local obj = {}
    setmetatable(obj, self)
    self.__index = self
    return obj
end

-- Games

function reset:start()
    buttons.set(buttons.left, colors.yellow)
    buttons.set(buttons.middle, colors.blue)
    buttons.set(buttons.right, colors.purple)
    -- set image
end

function reset:left()
    game = games.spike()
end

function reset:middle()
    game = games.shift()
end

function reset:right()
    game = games.hintaro()
end