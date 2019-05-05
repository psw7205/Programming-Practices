const canvas = document.getElementById("jsCanvas");
const colors = document.getElementsByClassName("jsColor");
const range = document.getElementById("jsRange");
const mode = document.getElementById("jsMode");
const save = document.getElementById("jsSave");

let ctx = canvas.getContext("2d");
let painting = false;
let filling = false;

function onMouseMove(event) {
    const x = event.offsetX;
    const y = event.offsetY;

    if (painting && !filling) {
        ctx.lineTo(x, y);
        ctx.stroke();
    }
}

function startPainting(event) {
    painting = true;

    const x = event.offsetX;
    const y = event.offsetY;
    ctx.beginPath();
    ctx.moveTo(x, y);
}

function stopPainting() {
    painting = false;
}

function handleColorClick(event) {
    ctx.strokeStyle = event.target.style.backgroundColor;
    ctx.fillStyle = ctx.strokeStyle;
}

function handleRange(event) {
    ctx.lineWidth = event.target.value;
}

function handleModeClick() {
    if (filling) {
        filling = false;
        mode.innerText = "paint";
    } else {
        filling = true;
        mode.innerText = "fill";
    }
}

function handleCanvasClick() {
    if (filling) {
        ctx.fillRect(0, 0, canvas.width, canvas.height);
    }
}

function handleCtxMenu(event) {
    event.preventDefault();
}

function handleSaveClick(event) {
    const img = canvas.toDataURL();
    const temp = document.createElement("a");
    temp.href = img;
    temp.download = "PaintJS";
    temp.click();
}

function init() {
    canvas.addEventListener("mousemove", onMouseMove);
    canvas.addEventListener("mousedown", startPainting);
    canvas.addEventListener("mouseup", stopPainting);
    canvas.addEventListener("mouseleave", stopPainting);
    canvas.addEventListener("click", handleCanvasClick);
    canvas.addEventListener("contextmenu", handleCtxMenu);
    range.addEventListener("input", handleRange);
    save.addEventListener("click", handleSaveClick);

    Array.from(colors).forEach(color =>
        color.addEventListener("click", handleColorClick)
    );

    mode.addEventListener("click", handleModeClick);

    ctx.fillStyle = "#ffffff";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    canvas.width = 600;
    canvas.height = 600;

    ctx.strokeStyle = "black";
    ctx.lineWidth = 2.5;
}

init();
