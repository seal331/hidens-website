function randInt(size) {
    return Math.ceil(Math.random()*size);
}

    function getFact(jNum) {
        var Fact = new Array();

        Fact[1] = "This site was brought online on May 10th, 2021. It has greatly evolved since then.";
        Fact[2] = "This site was hosted on HM's secondary laptop until June 26th, 2021. It was hosted on GitHub pages until November 5th, 2021. Since then, it was self-hosted.";
        Fact[3] = "The best letter of the alphabet is objectively H."

        return Fact[jNum];
    }

document.write(getFact(randInt(3)));