const imgDisplay = document.getElementById("ImgDisplay");

const miniaturas = document.querySelectorAll(".imgMini img");

miniaturas.forEach(function (img) {
  img.addEventListener("click", function () {
    imgDisplay.src = img.src;
    document.getElementById('legenda').textContent = img.alt;
  });
});

imgDisplay.src = miniaturas[0].src;
document.getElementById('legenda').textContent = miniaturas[0].alt;