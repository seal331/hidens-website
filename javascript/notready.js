function randInt(size) {
	return Math.ceil(Math.random()*size);
}

	function getImg(jNum) {
		var NRImg = new Array();

		NRImg[1] = "<img src=/static/notready/1.gif>";
		NRImg[2] = "<img src=/static/notready/2.gif>";
		NRImg[3] = "<img src=/static/notready/3.gif>";
		NRImg[4] = "<img src=/static/notready/4.gif>";

		return NRImg[jNum];
	}

document.write(getImg(randInt(4)));