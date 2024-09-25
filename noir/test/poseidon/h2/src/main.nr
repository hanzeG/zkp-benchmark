use poseidon;

fn main(plains: Field) -> pub Field {
    poseidon::bn254::hash_2([plains; 2])
}