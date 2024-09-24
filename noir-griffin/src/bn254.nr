mod consts;
mod perm;
mod math;

#[field(bn254)]
pub fn hash_3(input: [Field; 3]) -> Field {
    perm::x5_3(input)[0]
}

#[field(bn254)]
pub fn hash_4(input: [Field; 4]) -> Field {
    perm::x5_4(input)[0]
}

#[field(bn254)]
pub fn hash_8(input: [Field; 8]) -> Field {
    perm::x5_8(input)[0]
}

#[field(bn254)]
pub(crate) fn squeeze<O>(mut state: [Field; 3]) -> [Field; O] {
    if O == 1 {
        let mut out = [0; O];
        out[0] = state[0];
        out
    } else if O == 2 {
        let mut output = [0; O];
        output[0] = state[0];
        output[1] = state[1];
        output
    } else {
        let mut output = [0; O];
        output[0] = state[0];
        output[1] = state[1];
        let mut counter = 2;

        for i in 2..O {
            if counter == 2 {
                //squeeze on every second element
                state = perm::x5_3(state);
                counter = 0;
            }
            output[i] = state[counter];
            counter += 1;
        }
        output
    }
}
