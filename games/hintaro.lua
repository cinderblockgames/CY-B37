require "layouts/buttons"

hintaro = {}

function hintaro:new()
    local obj = {}
    setmetatable(obj, self)
    self.__index = self
    return obj
end

-- Game

function hintaro:start()
    buttons.clear()
    -- set image
end

function hintaro:left()
    -- hintaro doesn't have any additional functionality
end

function hintaro:middle()
    -- hintaro doesn't have any additional functionality
end

function hintaro:right()
    -- hintaro doesn't have any additional functionality
end