document.addEventListener('DOMContentLoaded', function() {
	var image = document.getElementById("flagcounterimg");
	if (image.complete) {
		if (image.naturalWidth === 0) {
			document.getElementById("flagcounternotice").style.display = "block";
		}
	} else {
		image.addEventListener('error', function() {
			document.getElementById("flagcounternotice").style.display = "block";
		});
		image.addEventListener('load', function() {
			document.getElementById("flagcounternotice").style.display = "none";
		});
	}
});
