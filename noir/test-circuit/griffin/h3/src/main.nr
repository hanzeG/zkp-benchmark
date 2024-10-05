use dep::griffin;

fn main(plains: Field) -> pub Field {
    griffin::bn254::hash_3([plains; 3])
}