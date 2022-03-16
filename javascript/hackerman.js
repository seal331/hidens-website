//Originally from the NickNet IRC website 
//Author:  Nicholas Higgins
//Contact: spybob888@aol.com

function randInt(size) {
    return Math.ceil(Math.random()*size);
  }
    function getHackerman(jNum) {
        var mtHaxor = new Array();

        mtHaxor[1] = "I'm breaking into the shell access terminals with a server transdimensional phasing device";
        mtHaxor[2] = "I've hacked the oc6 level optical line with a Linux 0.01 non-rotatable disk";
        mtHaxor[3] = "I've hacked into your transdimensional phasing device network";
        mtHaxor[4] = "I broke into the vulnerable networking firewall with network routing device multiphase processors";
        mtHaxor[5] = "I've hacked the server with a side fumbling CPU processor";
        mtHaxor[6] = "I'm gaining root access to vulnerable networking firewall with a non-rotatable network switch";
        mtHaxor[7] = "I've gained effective root access to your x86 IBM level architecture";
        mtHaxor[8] = "I'm breaking into the network routing device with non-rotatable disk microprocessors";
        mtHaxor[9] = "I've gained effective root access to your network routing device with x86 IBM tremmy pipes";
        mtHaxor[10] = "I've hacked the with multidimension network security access vulnerabilities with a network routing device";
        mtHaxor[11]= "I'm gaining root access to multiphase process memorizer with network routing device x86 IBM level architecture microprocessor architecture side fumbling CPU";
        mtHaxor[12]= "I'm gaining root access to oc6 level optical line with oc6 level optical line Linux system minecraft server processor";
        mtHaxor[13] = "I've hacked the processor with network routing device insecure Windows server Windows server 1985 Windows server 1985"
        mtHaxor[14] = "I've hacked the network routing device with Windows server 1985 network firewall daemon shell access terminals vulnerable networking firewall"
        
        return mtHaxor[jNum];

    }

document.write(getHackerman(randInt(14)));