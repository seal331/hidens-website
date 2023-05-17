const things = [
	"non-rotatable disk", 
	"side fumbling CPU", 
	"processor", 
	"with multidimension network security access vulnerabilities", 
	"oc6 level optical line", 
	"microprocessor architecture", 
	"server", 
	"minecraft server", 
	"webserver running Linux 0.01", 
	"Linux system", 
	"shell access terminals", 
	"vulnerable networking firewall", 
	"multiphase process memorizer", 
	"x86 IBM level architecture", 
	"network firewall daemon", 
	"network routing device", 
	"insecure Windows server", 
	"Windows server 1985", 
	"transdimensional phasing device"
  ];
  
const actions = [
	"I've hacked into your ",
	"I'm breaking into the ",
	"I've hacked the ",
	"I've gained effective root access to your ",
	"I'm gaining root access to ",
	"I've hacked the ",
	"I broke into the ",
	"I have inflitrated the "
  ];
  
const getRandomItem = (array) => array[Math.floor(Math.random() * array.length)];
  
const jargon = actions[Math.floor(Math.random() * actions.length)];
  
const length = 5;
  
const items = [];
let withCount = 0;
  
for (let i = 0; i < length; i++) {
	if (i > 0) {
		if (withCount < 1) {
			items.push("with ");
			withCount++;
		}
	}
	items.push(getRandomItem(things));
}
  
const jargonOutput = jargon + items.join(" ") + ".";
  
const jargonElement = document.createElement("p");
jargonElement.textContent = jargonOutput;
  
const container = document.getElementById("jargon-container");
container.appendChild(jargonElement);
