use poseidon;

fn main(plains: Field) -> pub Field {
    poseidon::bn254::hash_7([plains; 7])
}