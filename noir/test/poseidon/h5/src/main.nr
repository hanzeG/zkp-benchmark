use poseidon;

fn main(plains: Field) -> pub Field {
    poseidon::bn254::hash_5([plains; 5])
}