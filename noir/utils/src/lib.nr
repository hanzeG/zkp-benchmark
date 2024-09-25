use poseidon;
use poseidon2;
use griffin;

// griffin
pub fn griffin_hash3(plains: [Field; 3]) -> pub Field {
    griffin::bn254::hash_3(plains)
}
pub fn griffin_hash4(plains: [Field; 4]) -> pub Field {
    griffin::bn254::hash_4(plains)
}
pub fn griffin_hash8(plains: [Field; 8]) -> pub Field {
    griffin::bn254::hash_8(plains)
}

// poseidon
pub fn poseidon_hash1(plains: [Field; 1]) -> pub Field {
    poseidon::bn254::hash_1(plains)
}
pub fn poseidon_hash2(plains: [Field; 2]) -> pub Field {
    poseidon::bn254::hash_2(plains)
}
pub fn poseidon_hash3(plains: [Field; 3]) -> pub Field {
    poseidon::bn254::hash_3(plains)
}
pub fn poseidon_hash4(plains: [Field; 4]) -> pub Field {
    poseidon::bn254::hash_4(plains)
}
pub fn poseidon_hash5(plains: [Field; 5]) -> pub Field {
    poseidon::bn254::hash_5(plains)
}
pub fn poseidon_hash6(plains: [Field; 6]) -> pub Field {
    poseidon::bn254::hash_6(plains)
}
pub fn poseidon_hash7(plains: [Field; 7]) -> pub Field {
    poseidon::bn254::hash_7(plains)
}
pub fn poseidon_hash8(plains: [Field; 8]) -> pub Field {
    poseidon::bn254::hash_8(plains)
}
pub fn poseidon_hash9(plains: [Field; 9]) -> pub Field {
    poseidon::bn254::hash_9(plains)
}
pub fn poseidon_hash10(plains: [Field; 10]) -> pub Field {
    poseidon::bn254::hash_10(plains)
}
pub fn poseidon_hash11(plains: [Field; 11]) -> pub Field {
    poseidon::bn254::hash_11(plains)
}
pub fn poseidon_hash12(plains: [Field; 12]) -> pub Field {
    poseidon::bn254::hash_12(plains)
}
pub fn poseidon_hash13(plains: [Field; 13]) -> pub Field {
    poseidon::bn254::hash_13(plains)
}
pub fn poseidon_hash14(plains: [Field; 14]) -> pub Field {
    poseidon::bn254::hash_14(plains)
}
pub fn poseidon_hash15(plains: [Field; 15]) -> pub Field {
    poseidon::bn254::hash_15(plains)
}
pub fn poseidon_hash16(plains: [Field; 16]) -> pub Field {
    poseidon::bn254::hash_16(plains)
}

// poseidon2
pub fn poseidon2_hash2(plains: [Field; 2]) -> pub Field {
    poseidon2::bn254::hash_2(plains)
}
pub fn poseidon2_hash3(plains: [Field; 3]) -> pub Field {
    poseidon2::bn254::hash_3(plains)
}
pub fn poseidon2_hash4(plains: [Field; 4]) -> pub Field {
    poseidon2::bn254::hash_4(plains)
}
pub fn poseidon2_hash8(plains: [Field; 8]) -> pub Field {
    poseidon2::bn254::hash_8(plains)
}
pub fn poseidon2_hash12(plains: [Field; 12]) -> pub Field {
    poseidon2::bn254::hash_12(plains)
}
pub fn poseidon2_hash16(plains: [Field; 16]) -> pub Field {
    poseidon2::bn254::hash_16(plains)
}
