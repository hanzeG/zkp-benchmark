use poseidon;

fn main(plains: Field) -> pub Field {
    poseidon::bn254::hash_8([plains; 8])
}