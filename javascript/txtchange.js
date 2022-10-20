var txt = ['WHAT H', 'Foo', 'Bar', 'h', 'H', 'Test-Text-For-A-Test-Thing', 'gentoo balls'];
var i = 0;

setTimeout(function() {
    if (txt.length < i) {
        document.getElementById("sequence").innerHTML = txt[i];
        i++;
    } else {
        i = 0;
    }
}, 1000);
