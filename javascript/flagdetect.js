window.addEventListener('load', function() {
    var width = document.getElementsByTagName("img")[1].width
    if (width != 0) {
        console.log("flag counter seems to have loaded, removing notice");
        document.getElementsByClassName("flagcounternotice")[0].remove()
    }
}, false);
