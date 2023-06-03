document.addEventListener('DOMContentLoaded', function() {
	var image = document.getElementById("flagcounterimg");
	var flagcounternotice = document.getElementById("flagcounternotice");
  
	image.addEventListener('error', function() {
	  flagcounternotice.style.display = "block";
	});
  
	image.addEventListener('load', function() {
	  flagcounternotice.style.display = "none";
	});
  
	if (!image.complete) {
	  flagcounternotice.style.display = "none";
	}
  });
  