let count = 0;

function plus() {
    count++;
    document.getElementById("counter").innerHTML = count;
    if (count === 5) {
        document.getElementById("stoopid cat").innerHTML = '<img src="silly-cat.png"></img>';
    }
    else {
        document.getElementById("stoopid cat").innerHTML = '';
    }

}

function minus() {
    count--;
    document.getElementById("counter").innerHTML = count;
    if (count === 5) {
        document.getElementById("stoopid cat").innerHTML = '<img src="silly-cat.png"></img>';
    }
    else {
        document.getElementById("stoopid cat").innerHTML = '';
    }
}

