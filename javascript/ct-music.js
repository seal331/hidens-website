function randInt(size) {
	return Math.ceil(Math.random()*size);
}

	function getSong(jNum) {
		var Song = new Array();

		Song[1] = "<audio controls autoplay><source src=/././static/music/ct/jingban.mp3 id=ct-song type=audio/mpeg loop></source></audio>"
		Song[2] = "<audio controls autoplay><source src=/././static/music/ct/AllIWantForChristmasIsYou.mp3 id=ct-song type=audio/mpeg loop></source></audio><!-- :trollface: -->"
		Song[3] = "<audio controls autoplay><source src=/././static/music/ct/JingleBells.mp3 id=ct-song type=audio/mpeg loop></source></audio>"
		Song[4] = "<audio controls autoplay><source src=/././static/music/ct/JingleBellRock.mp3 id=ct-song type=audio/mpeg loop></source></audio>"
		Song[5] = "<audio controls autoplay><source src=/././static/music/ct/ramranch.mp3 id=ct-song type=audio/mpeg loop></source></audio>"
		Song[6] = "<audio controls autoplay><source src=/././static/music/ct/rainingblood.mp3 id=ct-song type=audio/mpeg loop></source></audio>"

		return Song[jNum];
	}

document.write(getSong(randInt(6)));