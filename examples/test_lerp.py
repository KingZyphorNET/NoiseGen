# simple test for the lerp function
from noisegen.noise import lerp

start = 0.5
end = 0.5

print(lerp(start, end, 0.0))
print(lerp(start, end, 0.25))
print(lerp(start, end, 0.5))
print(lerp(start, end, 0.75))
print(lerp(start, end, 1.0))