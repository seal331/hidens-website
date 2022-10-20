var txt = ['WHAT H', 'Foo', 'Bar', 'h', 'H', 'Test-Text-For-A-Test-Thing', 'gentoo balls'];
var i = 0;

document.getElementById("sequence").innerHTML = txt[i];
        
setInterval(function() {
    if (i < txt.length - 1) {
        i++;
    } else {
        i = 0;
    }
    
    document.getElementById("sequence").innerHTML = txt[i];
}, 1000);
