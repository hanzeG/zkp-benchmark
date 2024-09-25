const { rescue } = require("./rescue/rescue.js");
const { getCurveFromName } = require("ffjavascript");

async function main() {
    let prime = await getCurveFromName("bn128", true);
    let F = prime.Fr;
    let buff5 = F.e(0x26b6a528b427b35493736af8679aad17535cb9d394945a0dcfe7f7a98ccccccdn);
    let buffin = F.toObject(buff5);
    console.log(buff5);
    console.log(buffin);
}

main();