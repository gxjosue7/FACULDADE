const imgDisplay = document.getElementById("ImgDisplay");

const miniaturas = document.querySelectorAll(".imgMini img");

miniaturas.forEach(function (img) {
  img.addEventListener("click", function () {
    imgDisplay.src = img.src;
  });
});

