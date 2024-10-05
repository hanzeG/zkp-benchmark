use std::hash::mimc;

fn main(plains: Field) -> pub Field {
    mimc::mimc_bn254([plains; 4])
}