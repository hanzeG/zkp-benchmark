use std::hash::sha256;

fn main(plains: [u8; 128]) -> pub [u8; 32] {
    sha256(plains)
}