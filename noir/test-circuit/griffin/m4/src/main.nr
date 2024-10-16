use dep::griffin;

fn main(plains: Field) -> pub Field {
    let mut root = plains;
    for i in 0..31 {
        root = griffin::bn254::hash_3([root; 3]);
    }

    root
}