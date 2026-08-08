
from noisegen.noise import generate_noise_map

noise_map = generate_noise_map(10, 10, seed=42)

# Prints the generated noise map
for row in noise_map:
    print(" ".join(f"{value:.2f}" for value in row))
