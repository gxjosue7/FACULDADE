function abrir(titulo) {

  let conteudo = titulo.nextElementSibling;

  let icone = titulo.querySelector("i");

  conteudo.style.maxHeight = "200px";

  conteudo.style.padding = "20px";

  icone.classList.remove("fa-plus");

  icone.classList.add("fa-minus");
}

function fechar(titulo) {

  let conteudo = titulo.nextElementSibling;

  let icone = titulo.querySelector("i");

  conteudo.style.maxHeight = "0";

  conteudo.style.padding = "0 20px";

  icone.classList.remove("fa-minus");

  icone.classList.add("fa-plus");
}