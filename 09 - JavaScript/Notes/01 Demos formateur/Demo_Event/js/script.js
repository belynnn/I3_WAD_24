const inputNom = document.querySelector("#inputNom");
const inputPrenom = document.querySelector("#inputPrenom");
const inputAge = document.querySelector("#inputAge");
const bouton = document.querySelector("#bouton");

bouton.addEventListener('click', function(){
    const nomComplet = inputNom.value + " " + inputPrenom.value;
    const age = inputAge.valueAsNumber;
    const ageDansCinqAns = age + 5;
    alert("Bonjour " +nomComplet+ ", vous avez " +age+ " ans et dans 5 ans, vous aurez " +ageDansCinqAns+ " ans.");
})