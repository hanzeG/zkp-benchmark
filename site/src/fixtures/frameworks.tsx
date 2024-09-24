import benchmarks from './benchmarks.json'
import noirLogo from '@/img/frameworks/noir.svg'
import boojumLogo from '@/img/frameworks/boojum.png'
import circomLogo from '@/img/frameworks/circom.png'
import halo2Logo from '@/img/frameworks/halo2.png'
import starkyLogo from '@/img/frameworks/starky.png'

export const frameworks = [
  {
    id: 'circom',
    name: 'Circom (SnarkJS)',
    logo: {
      height: 30,
      width: 30,
      src: {
        light: circomLogo,
        dark: circomLogo,
      },
    },
    url: 'https://github.com/iden3/circom',
    frontend: 'Circom (DSL)',
    zk: 'SNARK',
    zkHash: ['MiMC', 'GMiMC', 'Poseidon', 'Poseidon2', 'Neptune', 'Rescue', 'Anemoi', 'Monolith'],
    hash: ['SHA-256', 'Blake2'],
    metrics: benchmarks.frameworks.polylang,
    // lib: ['CircomLib'],
    // libUrl: ['https://github.com/iden3/circomlib'],
  },
  {
    id: 'boojum',
    name: 'Boojum',
    logo: {
      height: 30,
      width: 30,
      src: {
        light: boojumLogo,
        dark: boojumLogo,
      },
    },
    url: 'https://github.com/matter-labs/era-boojum',
    frontend: 'Rust',
    zk: 'STARK',
    zkHash: ['Poseidon', 'Poseidon2'],
    hash: ['SHA-256', 'Blake2'],
    metrics: benchmarks.frameworks.polylang,
    // lib: ['Gadgets'],
    // libUrl: ['https://github.com/privacy-scaling-explorations/poseidon-gadget/tree/main'],
  },
  {
    id: 'halo2',
    name: 'Halo2-KZG',
    logo: {
      height: 30,
      width: 30,
      src: {
        light: halo2Logo,
        dark: halo2Logo,
      },
    },
    url: 'https://github.com/privacy-scaling-explorations/halo2',
    frontend: 'Rust',
    zk: 'SNARK',
    zkHash: ['MiMC', 'Poseidon', 'Poseidon2', 'Anemoi'],
    hash: ['SHA-256', 'Blake2'],
    metrics: benchmarks.frameworks.miden,
    // lib: ['Gadgets'],
    // libUrl: ['https://github.com/privacy-scaling-explorations/poseidon-gadget/tree/main'],
  },
  {
    id: 'starky',
    name: 'Starky',
    logo: {
      height: 30,
      width: 30,
      src: {
        light: starkyLogo,
        dark: starkyLogo,
      },
    },
    url: 'https://github.com/0xPolygonZero/plonky2',
    frontend: 'Rust',
    zk: 'STARK',
    zkHash: ['GMiMC', 'Poseidon', 'Poseidon2', 'Rescue', 'Tip5', 'Monolith'],
    hash: ['SHA-256', 'Blake2'],
    metrics: benchmarks.frameworks.noir,
    // lib: ['Gadgets'],
    // libUrl: ['https://github.com/0xPolygonZero/plonky2/tree/0e363e16a37a2eacd3349946bd071a460485ad26/plonky2/src/gadgets'],
  },
  {
    id: 'noir',
    name: 'Noir (Barretenberg)',
    logo: {
      height: 30,
      width: 80,
      src: {
        light: noirLogo,
        dark: noirLogo,
      },
    },
    url: 'https://noir-lang.org',
    frontend: 'Rust-like',
    zk: 'SNARK',
    zkHash: ['MiMC', 'GMiMC', 'Poseidon', 'Poseidon2', 'Griffin'],
    hash: ['SHA-256', 'Blake2'],
    metrics: benchmarks.frameworks.noir,
    // lib: ['TaceoLabs'],
    // libUrl: ['https://github.com/TaceoLabs'],
  }
]
