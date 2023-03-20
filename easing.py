import math

# Linear
def linear(t):
    return t

# Quadratic
def ease_in_quad(t):
    return t*t

def ease_out_quad(t):
    return t*(2-t)

def ease_in_out_quad(t):
    if t < 0.5:
        return 2*t*t
    else:
        return (-2*t*t) + (4*t) - 1

# Cubic
def ease_in_cubic(t):
    return t*t*t

def ease_out_cubic(t):
    t -= 1
    return t*t*t + 1

def ease_in_out_cubic(t):
    if t < 0.5:
        return 4*t*t*t
    else:
        t -= 1
        return 4*t*t*t + 1

# Quartic
def ease_in_quart(t):
    return t*t*t*t

def ease_out_quart(t):
    t -= 1
    return 1 - t*t*t*t

def ease_in_out_quart(t):
    if t < 0.5:
        return 8*t*t*t*t
    else:
        t -= 1
        return 1 - 8*t*t*t*t

# Quintic
def ease_in_quint(t):
    return t*t*t*t*t

def ease_out_quint(t):
    t -= 1
    return t*t*t*t*t + 1

def ease_in_out_quint(t):
    if t < 0.5:
        return 16*t*t*t*t*t
    else:
        t -= 1
        return 16*t*t*t*t*t + 1

# Sine
def ease_in_sine(t):
    return 1 - math.cos(t * math.pi / 2)

def ease_out_sine(t):
    return math.sin(t * math.pi / 2)

def ease_in_out_sine(t):
    return 0.5 * (1 - math.cos(t * math.pi))

# Exponential
def ease_in_expo(t):
    return math.pow(2, 10 * (t - 1))

def ease_out_expo(t):
    return 1 - math.pow(2, -10 * t)

def ease_in_out_expo(t):
    if t < 0.5:
        return 0.5 * math.pow(2, 10 * (2*t - 1))
    else:
        return 0.5 * (2 - math.pow(2, -10 * (2*t - 1)))

# Circular
def ease_in_circ(t):
    return 1 - math.sqrt(1 - t*t)

def ease_out_circ(t):
    return math.sqrt(1 - (t - 1)*(t - 1))

def ease_in_out_circ(t):
    if t < 0.5:
        return 0.5 * (1 - math.sqrt(1 - 4*t*t))
    else:
        return 0.5 * (math.sqrt(-4 * (t - 2)*t + 3) + 1)

# Back
def ease_in_back(t):
    s = 1.70158
    return t*t*((s+1)*t - s)

def ease_out_back(t):
    s = 1.70158
    t -= 1
    return t*t*((s+1)*t + s) + 1

def ease_in_out_back(t):
    s = 1.70158 * 1.525
    if t < 0.5:
        return 2*t*t*((s+1)*2*t - s) / 2
    else:
        t -= 2
        return (2*t*t*((s+1)*2*t + s) + 2) / 2

# Elastic
def ease_in_elastic(t):
    c = 1
    p = 0.3
    if t == 0:
        return 0
    elif t == 1:
        return 1
    else:
        a = c
        s = p / (2*math.pi) * math.asin(1/a)
        t -= 1
        return -(a*math.pow(2, 10*t) * math.sin((t-s)*(2*math.pi)/p))

def ease_out_elastic(t):
    c = 1
    p = 0.3
    if t == 0:
        return 0
    elif t == 1:
        return 1
    else:
        a = c
        s = p / (2*math.pi) * math.asin(1/a)
        return a*math.pow(2, -10*t) * math.sin((t-s)*(2*math.pi)/p) + 1

def ease_in_out_elastic(t):
    c = 1
    p = 0.3*1.5
    if t == 0:
        return 0
    elif t == 1:
        return 1
    else:
        a = c
        s = p / (2*math.pi) * math.asin(1/a)
        t *= 2
        if t < 1:
            t -= 1
            return -0.5*(a*math.pow(2,10*t) * math.sin( (t-s)*(2*math.pi)/p ))
        else:
            t -= 1
            return a*math.pow(2,-10*t) * math.sin( (t-s)*(2*math.pi)/p )*0.5 + 1

# Bounce
def ease_in_bounce(t):
    return 1 - ease_out_bounce(1 - t)

def ease_out_bounce(t):
    if t < 4/11.0:
        return (121 * t * t) / 16.0
    elif t < 8/11.0:
        return (363/40.0 * t * t) - (99/10.0 * t) + 17/5.0
    elif t < 9/10.0:
        return (4356/361.0 * t * t) - (35442/1805.0 * t) + 16061/1805.0
    else:
        return (54/5.0 * t * t) - (513/25.0 * t) + 268/25.0

def ease_in_out_bounce(t):
    if t < 0.5:
        return 0.5 * ease_in_bounce(t*2)
    else:
        return 0.5 * ease_out_bounce(t*2 - 1) + 0.5
