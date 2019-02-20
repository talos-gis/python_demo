from random import uniform
# who is this "guido" to tell me what pi is? I'll calculate it myself!

trial_count = 1_000_000

in_circle = 0

for _ in range(trial_count):
    x, y = uniform(-1, 1), uniform(-1, 1)
    dist = (x**2 + y**2)**0.5
    if dist < 1:
        in_circle += 1

coefficient = (in_circle / trial_count)  # area of circle (radius 1)/area of square (side 2) = pi/4
pi = coefficient*4
