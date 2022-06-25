const element = document.getElementById("click-history");
var newEntry, validEntry, entryCount = 0;

document.addEventListener('keydown', function (e) {
    validEntry = false;
    newEntry = document.createElement("li");
    if(e.key === 'a') {
        newEntry.innerText = 'A';
        validEntry = true;
    } else if(e.key === 'l') {
        newEntry.innerText = 'L';
        validEntry = true;
    }

    if(validEntry) {
        element.prepend(newEntry);
        entryCount++;
        document.getElementById('entry-counter').innerText = 'Entries: ' + entryCount;
    }
})

document.getElementById('a-button-press').addEventListener('click', function () {
    newEntry = document.createElement("li");
    newEntry.innerText = 'A';
    element.prepend(newEntry);
    entryCount++;
    document.getElementById('entry-counter').innerText = 'Entries: ' + entryCount;
})

document.getElementById('l-button-press').addEventListener('click', function () {
    newEntry = document.createElement("li");
    newEntry.innerText = 'L';
    element.prepend(newEntry);
    entryCount++;
    document.getElementById('entry-counter').innerText = 'Entries: ' + entryCount;
})

document.getElementById('reset-history').addEventListener('click', function() {
    element.innerHTML = '';
    entryCount = 0;
    document.getElementById('entry-counter').innerText = 'Entries: ' + entryCount;;
})