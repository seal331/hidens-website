function randInt(size) {
	return Math.ceil(Math.random()*size);
}

	function getSong(jNum) {
		var Song = new Array();

		Song[1] = "Leper Messiah - Metallica"
		Song[2] = "The Frayed Ends Of Sanity - Metallica"
		Song[3] = "Dyers Eve - Metallica"
		Song[4] = "Blackend - Metallica"
		Song[5] = "Blind - Korn"
		Song[6] = "Self Bias Resistor - Fear Factory"
		Song[7] = "Holy Wars... The Punishment Due - Megadeth"
		Song[8] = "Goddamn Eletric - Pantera"
		Song[9] = "Heresey - Pantera"
		Song[10] = "Slaughtered - Pantera"
		Song[11] = "I'm Broken - Pantera"
		Song[12] = "Pretty much all of Vulgar Display of Power - Pantera"
		// defintely missing some but i can't remember them

		return Song[jNum];
	}

document.write(getSong(randInt(12)));