use poseidon;

fn main(plains: Field) -> pub Field {
    poseidon::bn254::hash_14([plains; 14])
}