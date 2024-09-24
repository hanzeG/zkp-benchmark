use poseidon2;

fn main(plains: Field) -> pub Field {
    poseidon2::bn254::hash_8([plains; 8])
}