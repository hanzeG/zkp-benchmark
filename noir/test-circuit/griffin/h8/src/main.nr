use griffin;

fn main(plains: Field) -> pub Field {
    griffin::bn254::hash_8([plains; 8])
}