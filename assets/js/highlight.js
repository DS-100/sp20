const startOfSp20InMilli = new Date(2020, 0, 20, 0, 0, 0, 0).getTime();
const oneWeekInMilli = 604800000;

function highlighWeek() {
    const currentMilli = (new Date()).getTime();
    const currWeekIndex = Math.floor((currentMilli - startOfSp20InMilli) / oneWeekInMilli);
    var currentWeekTab = document.getElementsByClassName("module")[currWeekIndex];
    currentWeekTab.style.background = "linear-gradient(90deg, #2869e6 1.5%, white 1.5%)";
    var header = currentWeekTab.children[0];
    header.style.borderStyle = "none";
    var body = currentWeekTab.children[1];
    body.style.borderStyle = "none";
    var children = body.children;
    for (var i = 0; i < children.length; i++) {
        var currChild = children[i];
        if (!currChild.className.startsWith("module-event")) {
        currChild.style.border = "none";
        }
    }
}

document.addEventListener("DOMContentLoaded", function(event) {
    highlighWeek();
});
