# NoiseGen

NoiseGen is a Python-based procedural noise generator designed for creating smooth, continuous noise maps for terrain generation and experimentation.

The primary goal of the project is to generate numerical noise values that can be represented visually as grayscale heightmaps and eventually used to create terrain for Minecraft.

## Project Goals

* Generate smooth 2D procedural noise.
* Represent noise as continuous values between `0.0` and `1.0`.
* Convert numerical noise values into grayscale images.
* Generate heightmaps suitable for terrain generation.
* Support deterministic generation through seeds.
* Experiment with different interpolation and noise algorithms.
* Combine multiple layers of noise to create natural terrain.
* Optimize generation performance as the project grows.
* Eventually provide Minecraft-oriented terrain generation controls.

## Noise Representation

NoiseGen uses normalized floating-point values:

```text
0.0 ─────────────────────────────── 1.0
 │                                  │
Black                              White
```

Example values:

```text
0.00 → Black
0.10 → Very Dark Gray
0.25 → Dark Gray
0.50 → Gray
0.75 → Light Gray
0.90 → Very Light Gray
1.00 → White
```

Each generated position will contain a numerical value rather than simply being classified as black or white.

For example:

```python
0.183
0.421
0.537
0.762
0.914
```

These values can then be mapped to grayscale intensity.

## Planned Development

### Phase 1 — Basic Noise

* Create a 2D noise map.
* Generate deterministic random values.
* Implement interpolation.
* Produce smooth continuous noise.
* Normalize values to `0.0–1.0`.

### Phase 2 — Visualization

* Convert noise values to grayscale.
* Generate PNG heightmaps.
* Add configurable map dimensions.
* Add configurable output paths.

### Phase 3 — Advanced Noise

* Add multiple noise scales.
* Implement octaves.
* Experiment with fractal Brownian motion (fBm).
* Add persistence and lacunarity.
* Experiment with different noise algorithms.

### Phase 4 — Terrain Generation

* Convert noise values into terrain heights.
* Create terrain-specific controls.
* Experiment with mountains, plains, valleys, oceans, and coastlines.
* Generate Minecraft-oriented heightmaps.

### Phase 5 — Optimization

* Profile generation performance.
* Reduce unnecessary calculations.
* Experiment with efficient data structures.
* Investigate parallelization where appropriate.
* Benchmark different implementations.

## Example Target

A future NoiseGen output may look conceptually like:

```text
Low elevation                    High elevation

████████▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░
██████▓▓▓▓▒▒▒▒░░░░░░░░▒▒▒▒▓▓▓▓█
████▓▓▓▓▒▒░░░░░░▒▒▒▒▓▓▓▓███████
██▓▓▓▒▒░░░░▒▒▒▒▓▓▓▓████████████
▓▓▓▒▒░░▒▒▒▓▓▓██████████████████
```

The visual representation is only a visualization of the underlying numerical data.

## Project Structure

```text
NoiseGen/
├── README.md
├── src/
│   └── noisegen/
│       ├── __init__.py
│       └── noise.py
├── tests/
├── examples/
└── output/
```

## Technology

* Python
* NumPy — planned for later experimentation and optimization
* Pillow — planned for image generation
* Git / GitHub

Dependencies will be introduced as they become necessary.

## Learning Objectives

This project is also intended as a software-engineering learning project.

While developing NoiseGen, I want to understand:

* Python fundamentals
* Functions and classes
* Modules and packages
* Random number generation
* Arrays and numerical data
* Interpolation
* Procedural generation
* Algorithms
* Data structures
* Testing
* Profiling and optimization
* Git and version control

The implementation should be understood rather than treated as a black box.

## Status

**Early Development**

The repository currently contains the initial project structure. The first implementation will focus on understanding and generating basic 2D noise before adding more advanced algorithms.
