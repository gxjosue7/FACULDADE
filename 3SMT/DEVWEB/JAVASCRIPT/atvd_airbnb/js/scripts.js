let PRECO_BASE = 620;
let TAXA_LIMPEZA = 120;
let TAXA_SERVICO_PERC = 0.15;
let INCREMENTO_HOSPEDE = 0.20;

let checkinInput = document.getElementById('checkin');
let checkoutInput = document.getElementById('checkout');
let hospedesSelect = document.getElementById('hospedes');

let form = document.querySelector('form');
let btnReservar = form.querySelector('button');

let labelCupom = document.createElement('label');
labelCupom.setAttribute('for', 'cupom');
labelCupom.textContent = 'Cupom de desconto';

let inputCupom = document.createElement('input');
inputCupom.type = 'text';
inputCupom.id = 'cupom';
inputCupom.name = 'cupom';
inputCupom.placeholder = 'Ex: OFF15, OFF40...';
inputCupom.style.textTransform = 'uppercase';

form.insertBefore(labelCupom, btnReservar);
form.insertBefore(inputCupom, btnReservar);

let spanPrecoHeader = document.querySelector('header p span');
let divs = document.querySelectorAll('.card main > div');
let spanPrecoCalc = divs[0].querySelector('p span:first-child');
let spanQtdNoites = divs[0].querySelector('.qtd-hosp');
let spanTaxaServico = divs[2].querySelector('p span');
let spanTotal = document.querySelector('.card footer p span');
let msgNaoSeraCobrado = document.querySelector('.card main > p');

function precoNoitePorHospede(hospedes) {
    let adicionais = hospedes - 1;
    return PRECO_BASE * (1 + adicionais * INCREMENTO_HOSPEDE);
}

function calcularNoites(checkin, checkout) {
    if (!checkin || !checkout) return 0;
    let diff = new Date(checkout) - new Date(checkin);
    return diff > 0 ? Math.floor(diff / 86400000) : 0;
}

function aplicarCupom(total, cupom) {
    let match = cupom.toUpperCase().match(/^OFF(\d+)$/);
    if (!match) return { totalFinal: total, desconto: 0 };
    let percentual = parseInt(match[1]) / 100;
    let desconto = total * percentual;
    return { totalFinal: total - desconto, desconto };
}

function formatarBRL(valor) {
    return valor.toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

function atualizar() {
    let hospedes = parseInt(hospedesSelect.value);
    let noites = calcularNoites(checkinInput.value, checkoutInput.value);
    let precoNoite = precoNoitePorHospede(hospedes);

    let subtotal = precoNoite * noites;
    let taxaServico = subtotal * TAXA_SERVICO_PERC;
    let totalBruto = subtotal + TAXA_LIMPEZA + taxaServico;

    let cupom = inputCupom.value.trim();
    let { totalFinal } = aplicarCupom(totalBruto, cupom);

    spanPrecoHeader.textContent = formatarBRL(precoNoite);
    spanPrecoCalc.textContent = formatarBRL(precoNoite);

    if (noites > 0) {
        spanQtdNoites.textContent = `x ${noites} ${noites === 1 ? 'noite' : 'noites'}`;
    } else {
        spanQtdNoites.textContent = 'noites';
    }

    spanTaxaServico.textContent = formatarBRL(taxaServico);
    spanTotal.textContent = formatarBRL(totalFinal);
}

checkoutInput.addEventListener('change', atualizar);
hospedesSelect.addEventListener('change', atualizar);
inputCupom.addEventListener('input', atualizar);

form.addEventListener('submit', (e) => e.preventDefault());

atualizar();