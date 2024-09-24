use poseidon;

fn main(plains: Field) -> pub Field {
    poseidon::bn254::hash_11([plains; 11])
}