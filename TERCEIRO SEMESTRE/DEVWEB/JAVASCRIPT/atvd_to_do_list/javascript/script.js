function adicionar(btn) {
  const input = document.getElementById("texto");
  const texto = input.value.trim();

  if (!texto) {
    input.focus();
    return;
  }

  const ul = document.getElementById("lista");

  const li = document.createElement("li");
  li.innerHTML = `
    <input type="checkbox" onchange="toggleConcluido(this)" />
    <span class="task-text">${escapar(texto)}</span>
    <button class="btn-delete" onclick="remover(this)">Delete</button>
    <button class="btn-edit"   onclick="editar(this)">Edit</button>
  `;

  ul.appendChild(li);
  input.value = "";
  input.focus();
}

function remover(btn) {
  const li = btn.closest("li");
  li.remove();
}

function editar(btn) {
  const li = btn.closest("li");
  const span = li.querySelector(".task-text");
  const novoTexto = prompt("Editar tarefa:", span.textContent);

  if (novoTexto !== null && novoTexto.trim() !== "") {
    span.textContent = novoTexto.trim();
  }
}

function toggleConcluido(checkbox) {
  const span = checkbox.nextElementSibling;
  span.classList.toggle("done", checkbox.checked);
}

function escapar(str) {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}