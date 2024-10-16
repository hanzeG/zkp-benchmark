use poseidon;

fn main(plains: Field) -> pub Field {
    let mut root = plains;
    for i in 0..31 {
        root = poseidon::bn254::hash_2([root; 2]);
    }

    root
}