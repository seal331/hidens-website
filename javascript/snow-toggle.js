function toggleSnow() {
	var snowScript = document.getElementById('snow-script');
	if (snowScript) {
	  snowScript.parentNode.removeChild(snowScript);
	} else {
	  var newScript = document.createElement('script');
	  newScript.setAttribute('src', '/js/ct-snow.js');
	  newScript.setAttribute('id', 'snow-script');
	  document.body.appendChild(newScript);
	}
  }
  