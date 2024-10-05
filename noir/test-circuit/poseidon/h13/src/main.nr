use poseidon;

fn main(plains: Field) -> pub Field {
    poseidon::bn254::hash_13([plains; 13])
}