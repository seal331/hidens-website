document.addEventListener('DOMContentLoaded', function() {
    var screenWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
    var screenHeight = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
    var minScreenWidth = 1366;
    var minScreenHeight = 768;
  
    if (screenWidth < minScreenWidth || screenHeight < minScreenHeight) {
      var warningMessage = "Warning: Your screen resolution is below 1366x768. You will encounter usability issues.";
      var warningElement = document.createElement("div");
      warningElement.innerHTML = warningMessage;
      warningElement.style.textAlign = "center";
      warningElement.style.backgroundColor = "red";
      warningElement.style.color = "white";
      warningElement.style.padding = "10px";
      warningElement.style.paddingLeft= "115px";
      warningElement.style.position = "fixed";
      warningElement.style.top = "0";
      warningElement.style.left = "0";
      warningElement.style.width = "100%";
      warningElement.style.textAlign = "center";
      warningElement.style.zIndex = "2";
      document.body.insertBefore(warningElement, document.body.firstChild);
      
      var footerElement = document.querySelector("footer");
      if (footerElement) {
        footerElement.style.display = "none";
      }
    }
  });