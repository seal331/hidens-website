//Originally from the NickNet IRC website 
//Author:  Nicholas Higgins
//Contact: spybob888@aol.com

function randInt(size) {
    return Math.ceil(Math.random()*size);
  }
      function getHackerman(jNum)
      {
          var mtTagline = new Array();
          mtTagline[1] = "I'm breaking into the shell access terminals with a server transdimensional phasing device";
          mtTagline[2] = "I've hacked the oc6 level optical line with a Linux 0.01 non-rotatable disk";
          mtTagline[3] = "I've hacked into your transdimensional phasing device network";
          mtTagline[4] = "I broke into the vulnerable networking firewall with network routing device multiphase processors";
          mtTagline[5] = "I've hacked the server with a side fumbling CPU processor";
          mtTagline[6] = "I'm gaining root access to vulnerable networking firewall with a non-rotatable network switch";
          mtTagline[7] = "I've gained effective root access to your x86 IBM level architecture";
          mtTagline[8] = "I'm breaking into the network routing device with non-rotatable disk microprocessors";
          mtTagline[9] = "I've gained effective root access to your network routing device with x86 IBM tremmy pipes";
          mtTagline[10] = "I've hacked the with multidimension network security access vulnerabilities with a network routing device";
          mtTagline[11]= "I'm gaining root access to multiphase process memorizer with network routing device x86 IBM level architecture microprocessor architecture side fumbling CPU";
          mtTagline[12]= "I'm gaining root access to oc6 level optical line with oc6 level optical line Linux system minecraft server processor";
                  
          return mtTagline[jNum];
      }
      document.write(getHackerman(randInt(12)));