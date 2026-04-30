function pegarDados() {
    return {
        renda: Number(document.getElementById("renda").value),
        valor: Number(document.getElementById("valor").value),
        prazo: Number(document.getElementById("prazo").value)
    };
}

// 2. Calcular empréstimo
function calcularEmprestimo(renda, valor, prazo) {
    let anos = prazo / 12;
    let taxa = 0.02 * anos;
    let total = valor + (valor * taxa);
    let parcela = total / prazo;
    let limite = renda * 0.3;

    return {
        parcela: parcela,
        aprovado: parcela <= limite
    };
}

function mostrarResultado(parcela, aprovado) {
    let mensagem = `Parcela mensal: R$ ${parcela.toFixed(2)} <br>`;

    if (aprovado) {
        mensagem += "Empréstimo dentro do limite";
    } else {
        mensagem += "Risco de comprometimento da renda";
    }

    document.getElementById("resultado").innerHTML = mensagem;
}

document.getElementById("formEmprestimo").addEventListener("submit", function (e) {
    e.preventDefault();

    let dados = pegarDados();
    let resultado = calcularEmprestimo(dados.renda, dados.valor, dados.prazo);
    mostrarResultado(resultado.parcela, resultado.aprovado);
});