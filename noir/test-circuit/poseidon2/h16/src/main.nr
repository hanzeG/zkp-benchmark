use poseidon2;

fn main(plains: Field) -> pub Field {
    poseidon2::bn254::hash_16([plains; 16])
}