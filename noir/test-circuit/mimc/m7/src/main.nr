use std::hash::mimc;

fn main(plains: Field) -> pub Field {
    let mut root = plains;
    for i in 0..255 {
       root =  mimc::mimc_bn254([root; 2]);
    }

    root
}