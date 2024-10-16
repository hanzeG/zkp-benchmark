use poseidon2;

fn main(plains: Field) -> pub Field {
    let mut root = plains;
    for i in 0..3 {
        root = poseidon2::bn254::hash_2([root; 2]);
    }

    root
}