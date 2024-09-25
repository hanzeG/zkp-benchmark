use poseidon;

fn main(plains: Field) -> pub Field {
    poseidon::bn254::hash_6([plains; 6])
}