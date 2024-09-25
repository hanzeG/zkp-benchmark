use poseidon;

fn main(plains: Field) -> pub Field {
    poseidon::bn254::hash_10([plains; 10])
}