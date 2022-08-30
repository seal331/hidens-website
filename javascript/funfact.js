function randInt(size) {
	return Math.ceil(Math.random()*size);
}

	function getFact(jNum) {
		var Fact = new Array();

		Fact[1] = "This site was brought online on May 10th, 2021. It has greatly evolved since then. <a class=stuffboxcontenttxt href=/static/unused/old/page/frontpage_index.html>You can view a glimpse of what it looked like then if you'd like</a>.";
		Fact[2] = "This site was hosted on an ex-friend's spare laptop until June 26th, 2021. It was hosted on GitHub pages until November 5th, 2021. Since then, it was self-hosted.";
		Fact[3] = "The best letter of the alphabet is objectively H."
		Fact[4] = "This site had had a total of 3 - 5 extended downtimes in the ~1 year it's been active."
		Fact[5] = "The web server this site runs on runs Fedora Linux."
		Fact[6] = "The backend of this site has a massive spaghetti code problem. It works, at least."
		Fact[7] = "Mitochondria is the powerhouse of the cell."

		return Fact[jNum];
	}

document.write(getFact(randInt(7)));