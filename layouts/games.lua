require "games/reset"
require "games/spike"
require "games/shift"
require "games/hintaro"

games = {}

function games.start(target)
    local obj = target:new()
    obj:start()
    return obj
end

function games.reset()
    return games.start(reset)
end

function games.spike()
    return games.start(spike)
end

function games.shift()
    return games.start(shift)
end

function games.hintaro()
    return games.start(hintaro)
end