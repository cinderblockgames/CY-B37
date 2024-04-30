sounds = {}

function setup()
    __pwm = require('periphery').PWM
end

function sounds.question()
    -- Open PWM chip 0, channel 0
    local pwm = __pwm(0, 0)

    -- Set frequency to 1 kHz
    pwm.frequency = 1e3
    -- Set duty cycle to 75%
    pwm.duty_cycle = 0.75

    -- Enable PWM output
    pwm:enable()

    pwm:close()
end