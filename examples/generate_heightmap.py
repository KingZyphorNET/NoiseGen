# generate a test heightmap

from noisegen.image import save_heightmap
from noisegen.noise import generate_octave_noise


def main() -> None:
    width = 512
    height = 512
    scale = 64
    octaves = 5
    persistence = 0.5
    lacunarity = 2.0
    seed = 42

    noise_map = generate_octave_noise(
        width=width,
        height=height,
        scale=scale,
        octaves=octaves,
        persistence=persistence,
        lacunarity=lacunarity,
        seed=seed,
    )

    save_heightmap(
        noise_map,
        "output/heightmap.png",
    )

    print("generated output/heightmap.png")


if __name__ == "__main__":
    main()