A benchmarking tool for circuit-level performance, covering multiple popular ZK development libraries, including **Circom**, **Halo2-PSE**, **Noir**, **Boojum**, **Plonky2**, and **Plonky3**. These libraries encompass a range of widely-used ZK Layer2 technology stacks, such as **Scroll**, **Polygon**, **Aztec**, **Taiko**, and **ZKsync**.

# Getting Started

## Prerequisites

- Install `wget` (macOS with Homebrew: `brew install wget`)
- Install [`Rust`](https://www.rust-lang.org/tools/install)
- Install [`Nargo`](https://noir-lang.org/docs/getting_started/installation/)
- Install [`Circom`](https://github.com/iden3/circom)

## Benchmarking

- `git clone https://github.com/hanzeG/zkp-benchmark.git`
- `cd zkp-benchmark`

Run the test script, which by default takes the average of ten runs: `/bin/bash "./scripts/run_ave.bash"`
The results are saved in `results_ave.json` (the single-run test script is in `run.bash`, and the results are in `results.json`).

## Front-end

- `cd site`
- `npm run dev`

The benchmarking results are saved in `site/src/fixtures/benchmarks.json`.

## Tests

Tests are using variable libraries including `Circomlib`, `Noir stdlib`: 

- mimc: MiMC hash of the input, with input lenth of `{2, 3, 4, …, 16}`.
- poseidon: Poseidon hash of the input, with input lenth of `{2, 3, 4, …, 16}`.
- poseidon2: Poseidon hash of the input, with input lenth of `{2, 3, 4, …, 16}`.
- griffin: Griffin hash of the input, with input lenth of `{2, 3, 8}`.
- sha256: SHA-256 hash of the input.

## Example Results

Example results from a trial run on an M1 MacBook Pro:

```json
{
  "griffin": {
    "h3": {
      "op_codes": "180",
      "witness": {
        "user_time": "0.542",
        "max_resident_size": "181826355"
      },
      "prove": {
        "user_time": "0.089",
        "max_resident_size": "9361818"
      },
      "write_vk": {
        "user_time": "0.060",
        "max_resident_size": "9456845"
      },
      "verify": {
        "user_time": "0.040",
        "max_resident_size": "7423590"
      }
    },
    "h4": {
      "op_codes": "217",
      "witness": {
        "user_time": "0.542",
        "max_resident_size": "182575104"
      },
      "prove": {
        "user_time": "0.060",
        "max_resident_size": "9945088"
      },
      "write_vk": {
        "user_time": "0.060",
        "max_resident_size": "9928704"
      },
      "verify": {
        "user_time": "0.040",
        "max_resident_size": "7318733"
      }
    },
    "h8": {
      "op_codes": "433",
      "witness": {
        "user_time": "0.547",
        "max_resident_size": "186669466"
      },
      "prove": {
        "user_time": "0.063",
        "max_resident_size": "13510246"
      },
      "write_vk": {
        "user_time": "0.060",
        "max_resident_size": "13511885"
      },
      "verify": {
        "user_time": "0.040",
        "max_resident_size": "7384269"
      }
    }
  }
