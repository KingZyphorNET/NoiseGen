from noisegen.noise import lerp 

start = 0.2
end = 0.8
steps = 10

# Test the lerp function with different values of t
for i in range(steps + 1):
    t = i / steps
    value = lerp(start, end, t)

    print(f"t={t:.2f} output={value:.2f}")
