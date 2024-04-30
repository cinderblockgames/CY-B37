require "layouts/buttons"
require "layouts/colors"

shift = {}

function shift:new()
    local obj = {}
    setmetatable(obj, self)
    self.__index = self
    return obj
end

-- Game

function shift:start()
    buttons.clear()
    buttons.set(buttons.left, colors.red)
    buttons.set(buttons.middle, colors.green)
    buttons.set(buttons.right, colors.white)

    shift.tracking = {}

    -- set image
end

function shift:pick_target()
    buttons.set(buttons.left, colors.light_pink)
    buttons.set(buttons.middle, colors.hot_pink)
    buttons.set(buttons.right, colors.grey)
    
    -- set image
end

function shift:pick_suit()
    buttons.set(buttons.left, colors.yellow)
    buttons.set(buttons.middle, colors.orange)
    buttons.set(buttons.right, colors.purple)

    -- set image
end

function shift:play()
    buttons.set(buttons.left, colors.off)
    buttons.set(buttons.middle, colors.off)
    buttons.set(buttons.right, colors.grey)

    -- set image
end

function shift:left()
    if shift.tracking.positive == nil then
        shift.tracking.positive = false
        shift:pick_target()
    elseif shift.tracking.target == nil then
        shift.tracking.target = 5
        shift:pick_suit()
    elseif shift.tracking.suit == nil then
        shift.tracking.suit = "circle"
        shift:play()
    end
end

function shift:middle()
    if shift.tracking.positive == nil then
        shift.tracking.positive = true
        shift:pick_target()
    elseif shift.tracking.target == nil then
        shift.tracking.target = 10
        shift:pick_suit()
    elseif shift.tracking.suit == nil then
        shift.tracking.suit = "triangle"
        shift:play()
    end
end

function shift:right()
    if shift.tracking.target == nil then
        shift.tracking.positive = true
        shift.tracking.target = 0
        shift:pick_suit()
    elseif shift.tracking.suit == nil then
        shift.tracking.suit = "square"
        shift:play()
    else
        shift:start()
    end
end