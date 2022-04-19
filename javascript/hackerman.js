//Originally from the NickNet IRC website 
//Author:  Nicholas Higgins
//Contact: spybob888@aol.com

function randInt(size) {
    return Math.ceil(Math.random()*size);
}

    function getHackerman(jNum) {
        var Haxor = new Array();

        Haxor[1] = "I'm breaking into the shell access terminals with a server transdimensional phasing device";
        Haxor[2] = "I've hacked the oc6 level optical line with a Linux 0.01 non-rotatable disk";
        Haxor[3] = "I've hacked into your transdimensional phasing device network";
        Haxor[4] = "I broke into the vulnerable networking firewall with network routing device multiphase processors";
        Haxor[5] = "I've hacked the server with a side fumbling CPU processor";
        Haxor[6] = "I'm gaining root access to vulnerable networking firewall with a non-rotatable network switch";
        Haxor[7] = "I've gained effective root access to your x86 IBM level architecture";
        Haxor[8] = "I'm breaking into the network routing device with non-rotatable disk microprocessors";
        Haxor[9] = "I've gained effective root access to your network routing device with x86 IBM tremmy pipes";
        Haxor[10] = "I've hacked the with multidimension network security access vulnerabilities with a network routing device";
        Haxor[11]= "I'm gaining root access to multiphase process memorizer with network routing device x86 IBM level architecture microprocessor architecture side fumbling CPU";
        Haxor[12]= "I'm gaining root access to oc6 level optical line with oc6 level optical line Linux system minecraft server processor";
        Haxor[13] = "I've hacked the processor with network routing device insecure Windows server Windows server 1985 Windows server 1985";
        Haxor[14] = "I've hacked the network routing device with Windows server 1985 network firewall daemon shell access terminals vulnerable networking firewall";
        Haxor[15] = "I've gained effective root access to your transdimensional phasing device with shell access terminals side fumbling CPU server Windows server 1985";
        
        return Haxor[jNum];

    }

document.write(getHackerman(randInt(15)));