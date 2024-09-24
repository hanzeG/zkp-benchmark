use poseidon;

fn main(plains: Field) -> pub Field {
    poseidon::bn254::hash_4([plains; 4])
}