$(function () {

  var canvas = document.getElementById("canvas");
  var classify = document.getElementById("classify");
  var reset = document.getElementById("reset");

  var ctx = canvas.getContext('2d');
  ctx.lineCap = 'round';


  var mouseIsDown = false;

  function draw(x, y) {
    ctx.lineTo(x, y);
    ctx.stroke();
    ctx.beginPath();
    ctx.fill();
    ctx.beginPath();
    ctx.moveTo(x, y);
  }

  canvas.onmousedown = function (e) {
    mouseIsDown = true;
  }

  canvas.onmouseup = function (e) {
    if (mouseIsDown) mouseClick(e);
    mouseIsDown = false;
  }

  canvas.onmousemove = function (e) {
    if (!mouseIsDown) return;
    var rect = canvas.getBoundingClientRect();
    var x = (e.pageX - window.pageXOffset - rect.x) / 20;
    var y = (e.pageY - window.pageYOffset - rect.y) / 20;
    draw(x, y);
    return false;
  }

  function mouseClick(e) {
    // click action
  }

  function clear(ctx) {
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = 'white';
  }


  reset.onclick = function () { clear(ctx) };
  classify.onclick = function () {
    var data = canvas.toDataURL("image/jpeg");
    $.post('/predict', data)
      .done(res => {
        alert(`You drew a ${res.prediction}?`)
      });
  };

  clear(ctx);
})
