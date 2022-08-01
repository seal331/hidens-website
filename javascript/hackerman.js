var things = new Array("non-rotatable disk", "side fumbling CPU", "processor", "with multidimension network security access vulnerabilities", "oc6 level optical line", "microprocessor architecture", "server", "minecraft server", "webserver running Linux 0.01", "Linux system", "shell access terminals", "vulnerable networking firewall", "multiphase process memorizer", "x86 IBM level architecture", "network firewall daemon", "network routing device", "insecure Windows server", "Windows server 1985", "transdimensional phasing device");

var actions = new Array("I've hacked into your ", "I'm breaking into the ", "I've hacked the ", "I've gained effective root access to your ", "I'm gaining root access to ", "I've hacked the ", "I broke into the ");

var jargon = actions[(Math.ceil(Math.random() * actions.length) - 1)]
var length = 5;

for (var i = 0; i <= length; i++) {
	if (i <= 1) {
		jargon = jargon + "with ";
	};
	jargon = jargon + things[(Math.ceil(Math.random() * things.length) - 1)] + " ";
};

document.write("<p style=\"display: inline;\">" + jargon + "</p>")