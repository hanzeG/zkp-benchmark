use poseidon;

fn main(plains: Field) -> pub Field {
    poseidon::bn254::hash_16([plains; 16])
}