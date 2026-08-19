# turn noise maps into images

from pathlib import Path

from PIL import Image


# turn 0.0 - 1.0 noise values into grayscale pixels
def noise_to_grayscale(
    noise_map: list[list[float]],
) -> Image.Image:
    """Turn a noise map into a grayscale image."""

    if not noise_map:
        raise ValueError("Noise map cannot be empty.")

    height = len(noise_map)
    width = len(noise_map[0])

    if width == 0:
        raise ValueError("Noise map cannot contain empty rows.")

    for row in noise_map:
        if len(row) != width:
            raise ValueError("All rows must have the same width.")

    pixels = []

    for row in noise_map:
        for value in row:
            if not 0.0 <= value <= 1.0:
                raise ValueError("Noise values must be between 0.0 and 1.0.")

            pixel = round(value * 255)
            pixels.append(pixel)

    image = Image.new("L", (width, height))
    image.putdata(pixels)

    return image


# save a noise map as a png
def save_heightmap(
    noise_map: list[list[float]],
    output_path: str | Path,
) -> None:
    """Save a noise map as a grayscale PNG."""

    image = noise_to_grayscale(noise_map)

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    image.save(output_path, format="PNG")