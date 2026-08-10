# generate noise maps and linear interpolation stuff

import random


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


# linear interpolation thingy
def lerp(a: float, b: float, t: float) -> float:
    """Linearly interpolate between two values."""

    return a + (b - a) * t


# 2D version
def generate_interpolated_noise_map(
    width: int,
    height: int,
    seed: int | None = None,
) -> list[list[float]]:
    """Generate a 2D noise map using bilinear interpolation."""

    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be greater than zero.")

    base_map = generate_noise_map(width, height, seed)

    interpolated_map = []

    for y in range(height):
        row = []

        for x in range(width):
            x0 = max(x - 1, 0)
            x1 = min(x + 1, width - 1)

            y0 = max(y - 1, 0)
            y1 = min(y + 1, height - 1)

            horizontal = lerp(
                base_map[y][x0],
                base_map[y][x1],
                0.5,
            )

            vertical = lerp(
                base_map[y0][x],
                base_map[y1][x],
                0.5,
            )

            value = lerp(horizontal, vertical, 0.5)

            row.append(value)

        interpolated_map.append(row)

    return interpolated_map


# value noise
def generate_value_noise(
    width: int,
    height: int,
    scale: float = 8.0,
    seed: int | None = None,
) -> list[list[float]]:
    """Generate a smooth 2D noise map."""

    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be greater than zero.")

    if scale <= 0:
        raise ValueError("Scale must be greater than zero.")

    rng = random.Random(seed)

    grid_width = int(width / scale) + 2
    grid_height = int(height / scale) + 2

    grid = []

    for _ in range(grid_height):
        row = []

        for _ in range(grid_width):
            row.append(rng.random())

        grid.append(row)

    noise_map = []

    for y in range(height):
        row = []

        for x in range(width):
            gx = x / scale
            gy = y / scale

            x0 = int(gx)
            x1 = x0 + 1

            y0 = int(gy)
            y1 = y0 + 1

            sx = gx - x0
            sy = gy - y0

            n0 = lerp(
                grid[y0][x0],
                grid[y0][x1],
                sx,
            )

            n1 = lerp(
                grid[y1][x0],
                grid[y1][x1],
                sx,
            )

            value = lerp(n0, n1, sy)

            row.append(value)

        noise_map.append(row)

    return noise_map