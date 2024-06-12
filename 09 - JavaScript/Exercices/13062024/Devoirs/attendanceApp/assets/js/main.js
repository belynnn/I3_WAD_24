console.log('Coucou');
const btnPresent = document.querySelectorAll('td.btnPresent');
const btnAbsent = document.querySelectorAll('td.btnAbsent');

for (let i = 0 ; i < btnPresent.length ; i++) {
    btnPresent[i].addEventListener('click', function() {
        btnPresent[i].textContent = '🟢';
        btnAbsent[i].textContent = '🟦';
    })
    btnAbsent[i].addEventListener('click', function() {
        btnAbsent[i].textContent = '🔴';
        btnPresent[i].textContent = '🟦';
    })
}

console.log(btnPresent, btnAbsent)

