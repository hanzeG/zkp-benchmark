use poseidon;

fn main(plains: Field) -> pub Field {
    poseidon::bn254::hash_9([plains; 9])
}