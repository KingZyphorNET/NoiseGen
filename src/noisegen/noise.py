# module for generating noise maps and performing linear interpolation

import random

# basic noise function
def generate_noise_map(
    
    width: int,
    height: int,
    seed: int | None = None,
) -> list[list[float]]:
    """Generate a 2D map of random values between 0.0 and 1.0."""

    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be greater than zero.")

    if seed is not None:
        random.seed(seed)

    noise_map = []

    for _ in range(height):
        row = []

        for _ in range(width):
            value = random.random()
            row.append(value)

        noise_map.append(row)

    return noise_map


# stuff for lerp
def lerp(a: float, b: float, t: float) -> float:
    """Linearly interpolate between two values."""
    return a + (b - a) * t

