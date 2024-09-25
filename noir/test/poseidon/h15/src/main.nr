use poseidon;

fn main(plains: Field) -> pub Field {
    poseidon::bn254::hash_15([plains; 15])
}