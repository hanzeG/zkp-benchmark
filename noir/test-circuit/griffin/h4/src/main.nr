use griffin;

fn main(plains: Field) -> pub Field {
    griffin::bn254::hash_4([plains; 4])
}