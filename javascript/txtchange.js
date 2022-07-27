var txt = ['WHAT H', 'Foo', 'Bar', 'h', 'H', 'Test-Text-For-A-Test-Thing'];
	textSequence(0);
	function textSequence(i) {
		if (txt.length > i) {
			setTimeout(function() {
				document.getElementById("sequence").innerHTML = txt[i];
				textSequence(++i);
			}, 1000); 
		} else if (txt.length == i) {
			textSequence(0);
		}
	}