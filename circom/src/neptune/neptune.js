const { swap } = require("../utils");
const { getCurveFromName } = require("ffjavascript");
const NeptuneParams = require("./neptune_paras");

class Neptune {
    constructor(F, neptuneParas) {
        this.F = F;
        this.paras = neptuneParas;
    }

    External4(input) {
        const F = this.F;
        let out = swap(input, 1, 3);

        let current_state = out.map(a => F.e(a));

        let sum1 = F.add(current_state[0], current_state[2]);
        let sum2 = F.add(current_state[1], current_state[3]);

        current_state[0] = F.add(current_state[0], sum1);
        current_state[1] = F.add(current_state[1], sum2);
        current_state[2] = F.add(current_state[2], sum1);
        current_state[3] = F.add(current_state[3], sum2);

        out = current_state.map(a => F.toObject(a));

        return out;
    }

    ExternalMatmul(input) {
        const t = this.paras.t;

        if (t === 4) {
            return this.External4(input);
        }
    }

    ExternalSboxPrime(input) {
        const F = this.F;
        const ABC = this.paras.ABC;

        let inp = input.map(a => F.e(a));
        let abc = ABC.map(a => F.e(a));

        let x1 = inp[0];
        let x2 = inp[1];

        let zi = F.sub(x1, x2);
        let zib = F.square(zi);

        // first terms
        let sum = F.add(x1, x2);
        let y1 = F.add(sum, x1);
        let y2 = F.add(sum, x2);
        y2 = F.add(y2, x2);

        // middle terms
        let tmp1 = F.add(zib, zib);
        let tmp2 = tmp1;
        tmp1 = F.add(tmp1, zib);
        tmp2 = F.add(tmp2, tmp2);
        y1 = F.add(y1, tmp1);
        y2 = F.add(y2, tmp2);

        // third terms
        let tmp = zi;
        tmp = F.sub(tmp, x2);
        tmp = F.sub(tmp, zib);
        tmp = F.add(tmp, abc[2]);
        tmp = F.square(tmp);
        y1 = F.add(y1, tmp);
        y2 = F.add(y2, tmp);

        return [F.toObject(y1), F.toObject(y2)];
    }

    ExternalSbox(input) {
        const F = this.F;
        const t = this.paras.t;

        let out = Array(t);

        let t2 = t / 2;
        for (let i = 0; i < t2; i++) {
            let in1 = input[i * 2];
            let in2 = input[i * 2 + 1];
            let [out1, out2] = this.ExternalSboxPrime([in1, in2]);
            out[2 * i] = out1;
            out[2 * i + 1] = out2;
        }

        return out;
    }

    ExternalRound(input, r) {
        const F = this.F;
        const t = this.paras.t;

        const RC = this.paras.round_constants;

        let current_state = this.ExternalSbox(input);

        current_state = this.ExternalMatmul(current_state);

        current_state = current_state.map(a => F.e(a));

        for (let i = 0; i < t; i++) {
            current_state[i] = F.add(current_state[i], F.e(RC[r][i]));
        }

        let out = current_state.map(a => F.toObject(a));

        return out;
    }

    InternalSbox(input) {
        const F = this.F;
        const t = this.paras.t;

        let current_state = input.map(a => F.e(a));

        const pow5 = a => F.mul(a, F.square(F.square(a)));

        current_state[0] = pow5(current_state[0]);

        let out = current_state.map(a => F.toObject(a));

        return out;
    }

    InternalMatmul(input) {
        const F = this.F;
        const t = this.paras.t;
        const U = this.paras.U;

        let current_state = input.map(a => F.e(a));
        let UU = U.map(a => F.e(a));

        let sum = current_state.reduce((acc, el) => F.add(acc, el));

        for (let i = 0; i < t; i++) {
            current_state[i] = F.mul(current_state[i], UU[i]);
            current_state[i] = F.add(current_state[i], sum);
        }

        let out = current_state.map(a => F.toObject(a));

        return out;
    }

    InternalRound(input, r) {
        const F = this.F;
        const t = this.paras.t;
        const RC = this.paras.round_constants;

        let current_state = this.InternalSbox(input);

        current_state = this.InternalMatmul(current_state);

        current_state = current_state.map(a => F.e(a));

        for (let i = 0; i < t; i++) {
            current_state[i] = F.add(current_state[i], F.e(RC[r][i]));
        }

        let out = current_state.map(a => F.toObject(a));

        return out;
    }

    Permutation(input) {
        const roundsF_beginning = this.paras.roundsF_beginning;
        const roundsF_end = this.paras.roundsF_end;
        const roundsP = this.paras.roundsP;

        let current_state = this.ExternalMatmul(input);

        for (let i = 0; i < roundsF_beginning; i++) {
            current_state = this.ExternalRound(current_state, i);
        }

        for (let i = 0; i < roundsP; i++) {
            current_state = this.InternalRound(current_state, i + roundsF_beginning);
        }

        for (let i = 0; i < roundsF_end; i++) {
            current_state = this.ExternalRound(current_state, i + roundsF_beginning + roundsP);
        }

        let out = current_state;

        return out;
    }
}

module.exports = Neptune;

async function main() {
    let prime;
    let F;

    prime = await getCurveFromName("bn128", true);
    F = prime.Fr;

    const np = new NeptuneParams(F, 4, 5, 6, 68);
    const npp = new Neptune(F, np);
    // let abc = np.round_constants.map(a => F.toObject(a))
    let abc = npp.Permutation([1n, 2n, 3n, 4n]);
    let abcac = npp.Permutation([1n, 2n, 3n, 3n]);
    console.log(abc);
    console.log(abcac);
}

main();