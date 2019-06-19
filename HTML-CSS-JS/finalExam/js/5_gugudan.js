function create() {
    var f = Math.floor(Math.random() * 9 + 1);
    var s = Math.floor(Math.random() * 9 + 1);
    document.getElementById("first").innerHTML = f;
    document.getElementById("second").innerHTML = s;
}

function check() {
    var f = document.getElementById("first").innerHTML;
    var s = document.getElementById("second").innerHTML;

    var ans = document.getElementById("answer").value;

    if (f * s == ans) {
        document.getElementById("check").innerHTML = "정답입니다.";
    } else {
        document.getElementById("check").innerHTML = "오답입니다.";
    }
}