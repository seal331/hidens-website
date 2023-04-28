function randInt(size) {
	return Math.ceil(Math.random() * size);
}
  
function getFact(jNum) {
	const facts = {
		1: "This site was brought online on May 10th, 2021. It has greatly evolved since then. <a href=/static/unused/old/page/original%20index/index.html>You can view a glimpse of what it looked like then if you'd like</a>.",
		2: "This site was hosted on an ex-friend's now non-existent spare laptop until June 26th, 2021. It was hosted on GitHub pages until November 5th, 2021. Since then, it was self-hosted.",
		3: "The best letter of the alphabet is objectively H.",
		4: "This site had had a total of 7 extended downtimes in the ~2 years it's been active.",
		5: "The site is running inside a Debian 11 LXC container.",
		6: "Before was was was, was was is.",
		7: "Mitochondria is the powerhouse of the cell."
	};
  
	return facts[jNum];
}
  
document.write(getFact(randInt(7)));
  