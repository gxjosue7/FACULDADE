const itens = document.querySelectorAll("li");

const colors = [
  { name: "AZUL", value: "#3498db" },
  { name: "VERDE", value: "#1abc9c" },
  { name: "ROXO", value: "#9b59b6" },
  { name: "LARANJA", value: "#e67e22" },
  { name: "VERMELHO", value: "#e74c3c" },
  { name: "CINZA", value: "#34495e" },
];

for (let i = 0; i < itens.length; i++) {
  itens[i].addEventListener("click", function () {
    let corSpan = document.querySelector("span").style.color
    if (itens[i].style.background == corSpan) {
        console.log("Acertou")
    }
  });

  itens[i].style.background = colors[i].value;
}

    function sorteiaCor() {
        let indice = parseInt(Math.random() * 6);
        let cor = colors(indice);
        const span = document.querySelector("h2 > span");

        span.textContent = cor.name
        span.style.color = cor.value    
    }

        sorteiaCor()
