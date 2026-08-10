const itens = document.querySelectorAll("li");
let corAtual = null;
let cronometro = "00:00";
let intervalo;

const colors = [
  { name: "AZUL", value: "#3498db" },
  { name: "VERDE", value: "#1abc9c" },
  { name: "ROXO", value: "#9b59b6" },
  { name: "LARANJA", value: "#e67e22" },
  { name: "VERMELHO", value: "#e74c3c" },
  { name: "CINZA", value: "#34495e" },
];

function embaralhaColors() {
  return [...colors].sort(() => Math.random() - 0.5);
}

function atualizaCronometro() {
  const inicio = Date.now();
  intervalo = setInterval(() => {
    let agora = Date.now();
    let ms = agora - inicio;
    cronometro = new Date(ms).toString().substr(15, 8);
    document.querySelector("section div p").textContent = cronometro;
  }, 1000);
}

function pintaQuadrados() {
  const coresEmbaralhadas = embaralhaColors();

  for (let i = 0; i < itens.length; i++) {
    itens[i].style.backgroundColor = coresEmbaralhadas[i].value;
    itens[i].onclick = null;

    itens[i].addEventListener("click", function () {
      if (coresEmbaralhadas[i].name === corAtual.name) {
        console.log(" Acertou!");
        setTimeout(() => sorteiaCor(), 500);
      } else {
        console.log(" Errou!");
      }
    });
  }
}

function sorteiaCor() {
  let indice = parseInt(Math.random() * colors.length);
  let cor = colors[indice];

  corAtual = cor;

  const span = document.querySelector("h2 > span");
  span.textContent = cor.name;
  span.style.backgroundColor = cor.value;

  pintaQuadrados();
}

sorteiaCor();
atualizaCronometro();