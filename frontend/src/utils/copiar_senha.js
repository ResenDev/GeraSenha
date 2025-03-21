const senha = document.querySelector(".senha").innerText;
const botaoCopia = document.querySelector(".btn-copy");

botaoCopia.addEventListener("click", () => {
    navigator.clipboard.writeText(senha);
    alert("Copiado para a área de transferência!");
});
