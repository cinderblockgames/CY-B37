require "layouts/buttons"
require "layouts/colors"
require "layouts/games"

require "sounds/sounds"

function error ( err )
    local num = err.c_errno

    local left = colors.none
    local middle = colors.none
    local right = colors.none

    if num % 2 == 1 then left = colors.red; num = num - 1 end
    if num % 4 == 2 then middle = colors.red; num = num - 2 end
    if num % 8 == 4 then right = colors.red; num = num - 4 end
    
    if num % 16 == 8 then
        if left == colors.red then left = colors.blue else left = colors.green end
        num = num - 8
    end
    if num % 32 == 16 then
        if middle == colors.red then middle = colors.blue else middle = colors.green end
        num = num - 16
    end
    if num % 64 == 32 then
        if right == colors.red then right = colors.blue else right = colors.green end
        num = num - 32
    end
    
    if num >= 64 then
        left = colors.white
        middle = colors.white
        right = colors.white
    end

    buttons.set(buttons.left, left)
    buttons.set(buttons.middle, middle)
    buttons.set(buttons.right, right)
end

function setup()
    buttons.setup()
    game = games.reset()
end

local function check_for_reset()
    if buttons.left.pressed and buttons.right.pressed then
        game = games.reset()
        cancel_left = true
        cancel_right = true
    end
end

cancel_left = false
function handle_minikey_00(pressed)
    xpcall(sounds.question, error)

    buttons.left.pressed = pressed
    if pressed then
        check_for_reset()
    elseif cancel_left then
        cancel_left = false
    else
        game.left()
    end
end

function handle_minikey_01(pressed)
    buttons.middle.pressed = pressed
    if not pressed then
        game.middle()
    end
end

cancel_right = false
function handle_minikey_02(pressed)
    buttons.right.pressed = pressed
    if pressed then
        check_for_reset()
    elseif cancel_right then
        cancel_right = false
    else
        game.right()
    end
end