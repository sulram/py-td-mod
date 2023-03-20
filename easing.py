import math

def cubic_bezier_point(t, y0, y1, y2, y3):
    """
    Calculates a point on a cubic Bezier curve for a given value of t.

    Args:
        t (float): The value of t (between 0 and 1) to calculate the point for.
        y0 (float): The starting y-coordinate of the curve.
        y1 (float): The first control point y-coordinate of the curve.
        y2 (float): The second control point y-coordinate of the curve.
        y3 (float): The ending y-coordinate of the curve.

    Returns:
        The y-coordinate on the cubic Bezier curve for the given value of t.
    """
    # Calculate the point on the curve using the cubic Bezier equation
    return (
        pow(1 - t, 3) * y0 +
        3 * pow(1 - t, 2) * t * y1 +
        3 * (1 - t) * pow(t, 2) * y2 +
        pow(t, 3) * y3
    )


def custom_ease(easing_func, t, b, c, d):
    """
    Animate a value using a normalized easing function.

    Args:
        easing_func: A reference to a normalized easing function.
        t: The current time value for the animation.
        b: The starting value of the animation.
        c: The total change in value for the animation.
        d: The total duration of the animation.

    Returns:
        The eased value for the current time, mapped to the range of values you want.
    """
    # Normalize t to a value between 0 and 1
    t = t / d
    # Call the specified easing function with the normalized value of t
    eased_t = easing_func(t)
    # Map the eased value to the range of values you want
    return b + eased_t * c

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
def ease_in_back(t, overshoot=1.70158):
    return t*t*((overshoot+1)*t - overshoot)

def ease_out_back(t, overshoot=1.70158):
    t -= 1
    return t*t*((overshoot+1)*t + overshoot) + 1

def ease_in_out_back(t, overshoot=1.70158):
    overshoot *= 1.525
    t *= 2
    if t < 1:
        return 0.5*(t*t*((overshoot+1)*t - overshoot))
    else:
        t -= 2
        return 0.5*(t*t*((overshoot+1)*t + overshoot) + 2)

# Elastic
def ease_in_elastic(t, amplitude=1, period=0.3):
    return 1 - ease_out_elastic(1 - t, amplitude=amplitude, period=period)

def ease_out_elastic(t, amplitude=1, period=0.3):
    if t == 0 or t == 1:
        return t

    s = period / (2 * math.pi) * math.asin(1 / amplitude)
    return amplitude * math.pow(2, -10 * t) * math.sin((t - s) * (2 * math.pi) / period) + 1

def ease_in_out_elastic(t, amplitude=1, period=0.3):
    if t == 0 or t == 1:
        return t

    t *= 2
    if t < 1:
        return 0.5 * ease_in_elastic(t, amplitude=amplitude, period=period)
    else:
        return 0.5 * ease_out_elastic(t - 1, amplitude=amplitude, period=period) + 0.5


# Bounce
def ease_in_bounce(t):
    return 1 - ease_out_bounce(1 - t)

def ease_out_bounce(t):
    if t < 1 / 2.75:
        return 7.5625 * t ** 2
    elif t < 2 / 2.75:
        t -= 1.5 / 2.75
        return 7.5625 * t ** 2 + 0.75
    elif t < 2.5 / 2.75:
        t -= 2.25 / 2.75
        return 7.5625 * t ** 2 + 0.9375
    else:
        t -= 2.625 / 2.75
        return 7.5625 * t ** 2 + 0.984375

def ease_in_out_bounce(t):
    if t < 0.5:
        return 0.5 * ease_in_bounce(t * 2)
    else:
        return 0.5 * ease_out_bounce(t * 2 - 1) + 0.5
