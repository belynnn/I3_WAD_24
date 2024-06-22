// FUNCTIONS
function generateRandomNumber() {
    return Math.floor(Math.random() * 3) + 1;
}



//! 1)  Stockez dans une variable, le résultat d'une saisie au clavier et affichez-la.
const STRING_RESULT = 'Ceci est une saisie au clavier, appellée "string" en programmation.';
const EXO_01_SUBMIT = document.querySelector('#exo_01_submit');

EXO_01_SUBMIT.addEventListener('click', function() {
    const RESPONSE_EXO_01 = document.createElement('p');

    RESPONSE_EXO_01.innerText = `🟢 ${STRING_RESULT}`;
    EXO_01_SUBMIT.parentElement.append(RESPONSE_EXO_01);

    EXO_01_SUBMIT.setAttribute("disabled", false);
});



//! 2)  À la place d'afficher simplement la variable, affichez son contenu précédé de la chaîne de caractères "Saisie clavier: ".
const EXO_02_SUBMIT = document.querySelector('#exo_02_submit');

EXO_02_SUBMIT.addEventListener('click', function() {
    const RESPONSE_EXO_02 = document.createElement('p');

    RESPONSE_EXO_02.innerText = `🟢 Saisie clavier : ${STRING_RESULT}`;
    EXO_02_SUBMIT.parentElement.append(RESPONSE_EXO_02);

    EXO_02_SUBMIT.setAttribute("disabled", false);
});



//! 3)  Récupérez au clavier un nombre et stockez-le dans une variable.
const EXO_03_SUBMIT = document.querySelector('#exo_03_submit');
const EXO_04_SUBMIT = document.querySelector('#exo_04_submit');
const EXO_05_SUBMIT = document.querySelector('#exo_05_submit');

EXO_03_SUBMIT.addEventListener('click', function() {
    const RESPONSE_EXO_03 = document.createElement('p');

    let exo03UserInput = parseInt(prompt("Veuillez entrer un nombre"));
    RESPONSE_EXO_03.innerText = `Vous avez entré ${exo03UserInput}, essayez le bouton des exercices 04 et 05. Pas de résultat ? Vous avez peut-être utilisé toutes vos chances.`;

    EXO_03_SUBMIT.parentElement.append(RESPONSE_EXO_03);
    
    //! 4)  Si le nombre qui se trouve dans la variable number est plus grand que 10, affichez la chaîne de caractères “Ce nombre est plus grand que 10”.
    if (exo03UserInput > 10) {
        EXO_04_SUBMIT.addEventListener('click', function() {
            const RESPONSE_EXO_04 = document.createElement('p');

            RESPONSE_EXO_04.innerText = `🟢 Ce nombre est plus grand que 10.`;
            EXO_03_SUBMIT.parentElement.append(RESPONSE_EXO_04);

            EXO_04_SUBMIT.setAttribute("disabled", false);
        })

    //! 5)  À la suite de la condition, si celle-ci n'est pas remplie, affichez le message suivant: “Le nombre est plus petit ou égal à 10.”
    } else {
        EXO_05_SUBMIT.addEventListener('click', function() {
            const RESPONSE_EXO_05 = document.createElement('p');

            RESPONSE_EXO_05.innerText = `🟢 Le nombre est plus petit ou égal à 10.`;
            EXO_03_SUBMIT.parentElement.append(RESPONSE_EXO_05);

            EXO_05_SUBMIT.setAttribute("disabled", false);
        })
    }
})



//! 6)  Récupérez un nombre au clavier et stockez-le dans une variable.
//  Si le nombre récupéré est plus grand ou égale à 10 affichez “Bravo!”.
//  Sinon, si il est plus grand que 8 affichez “Pas mal.”
//  Sinon, si le nombre est plus grand que 5 affichez “Mouais, bof”
//  Et sinon dans les autres cas affichez “Pas terrible”
const EXO_06_SUBMIT = document.querySelector('#exo_06_submit');

EXO_06_SUBMIT.addEventListener('click', function() {
    let exo06UserInput = parseInt(prompt("Veuillez entrer un nombre."));
    
    while (isNaN(exo06UserInput)) {
        exo06UserInput = parseInt(prompt("Veuillez entrer un nombre."));
    }

    const RESPONSE_EXO_06 = document.createElement('p');

    if (!isNaN(exo06UserInput) && exo06UserInput >= 10) {
        RESPONSE_EXO_06.innerText = `🟢 Bravo!`;
        EXO_06_SUBMIT.parentElement.append(RESPONSE_EXO_06);

    } else if (!isNaN(exo06UserInput) && exo06UserInput > 8) {
        RESPONSE_EXO_06.innerText = `🟣 Pas mal.`;
        EXO_06_SUBMIT.parentElement.append(RESPONSE_EXO_06);

    } else if (!isNaN(exo06UserInput) && exo06UserInput > 5) {
        RESPONSE_EXO_06.innerText = `🟠 Mouais, bof`;
        EXO_06_SUBMIT.parentElement.append(RESPONSE_EXO_06);

    } else {
        RESPONSE_EXO_06.innerText = `🔴 Pas terrible`;
        EXO_06_SUBMIT.parentElement.append(RESPONSE_EXO_06);
    }
})



//! 7)  Écrivez un script qui demande à l'utilisateur un nombre (entre 1 et 10).
//  Tant qu'il ne rentre pas un chiffre entre 1 et 10, le programme demande à nouveau à l'utilisateur un nombre (entre 1 et 10).
const EXO_07_SUBMIT = document.querySelector('#exo_07_submit');

EXO_07_SUBMIT.addEventListener('click', function() {
    let EXO_07_USER_INPUT = 0;
    const RESPONSE_EXO_07 = document.createElement('p');

    do {
        EXO_07_USER_INPUT = parseInt(prompt("Entrez un nombre entre 1 et 10 inclus"));

    } while (isNaN(EXO_07_USER_INPUT) || EXO_07_USER_INPUT < 1 || EXO_07_USER_INPUT > 10);

    RESPONSE_EXO_07.innerText = `🟢 Vous avez entré un nombre compris entre 1 et 10 inclus.`;
    EXO_07_SUBMIT.parentElement.append(RESPONSE_EXO_07);

    EXO_07_SUBMIT.setAttribute("disabled", false);
})



//! 8)  Écrivez un script qui demande à l'utilisateur un mot de passe.
//  Si le mot de passe entré n'est pas "Pyth0n" le programme demande à nouveau le mot de passe.
//  Quand le mot de passe est bon, le programme affiche "Mot de passe valide."
//  Après 3 tentatives infructueuses, le programme affiche "Mot de passe incorrect."
const EXO_08_SUBMIT = document.querySelector('#exo_08_submit');

EXO_08_SUBMIT.addEventListener('click', function() {
    let EXO_08_USER_INPUT = "";
    let disconnect = true;
    let count = 1;

    while (disconnect) {
        EXO_08_USER_INPUT = prompt("Veuillez entrer le bon mot de passe.")
        const RESPONSE_EXO_08 = document.createElement('p');

        if (EXO_08_USER_INPUT != "Pyth0n") {
            if (count < 3) {
                alert("Mot de passe invalide.");
                count += 1;
            } else if (count === 3) {
                RESPONSE_EXO_08.innerText = `🔴 Vous avez tenté de vous connecter trop de fois, veuillez réessayer.`;
                EXO_08_SUBMIT.parentElement.append(RESPONSE_EXO_08);

                break;
            }
        } else {
            RESPONSE_EXO_08.innerText = `🟢 Mot de passe valide.`;
            EXO_08_SUBMIT.parentElement.append(RESPONSE_EXO_08);

            disconnect = false;
            EXO_08_SUBMIT.setAttribute("disabled", false);
        }
    }
})



//! 9)  Écrivez un programme qui va générer trois nombres aléatoirement (entre 1 et 6).
//      Ensuite le programme va afficher les trois nombres
//      Si les trois nombres ne sont pas identiques, il recommence.
const EXO_09_SUBMIT = document.querySelector('#exo_09_submit');

EXO_09_SUBMIT.addEventListener('click', () => {
    let FIRST_RANDOM_NUMBER = 0;
    let SECOND_RANDOM_NUMBER = 1;
    let THIRD_RANDOM_NUMBER = 2;
    const RESPONSE_EXO_09 = document.createElement('p');

    
    do {
        alert(`❌ ${FIRST_RANDOM_NUMBER} - ${SECOND_RANDOM_NUMBER} - ${THIRD_RANDOM_NUMBER}`);

        FIRST_RANDOM_NUMBER = generateRandomNumber();
        SECOND_RANDOM_NUMBER = generateRandomNumber();
        THIRD_RANDOM_NUMBER = generateRandomNumber();

    } while (FIRST_RANDOM_NUMBER !== SECOND_RANDOM_NUMBER || SECOND_RANDOM_NUMBER !== THIRD_RANDOM_NUMBER);

    RESPONSE_EXO_09.innerText = `🟢 ${FIRST_RANDOM_NUMBER} - ${SECOND_RANDOM_NUMBER} - ${THIRD_RANDOM_NUMBER}`;
    EXO_09_SUBMIT.parentElement.append(RESPONSE_EXO_09);

    EXO_09_SUBMIT.setAttribute("disabled", false);
})



//! 10) Demandez à l'utilisateur d'entrer des nombre jusqu'à ce qu'il donne la valeur 0.
//      Ensuite, affichez le plus grand et le plus petit nombre que l'utilisateur a donné.
const EXO_10_SUBMIT = document.querySelector('#exo_10_submit');

EXO_10_SUBMIT.addEventListener('click', function() {
    
})



//! 11) Générez deux nombres aléatoire (entre 0 et 100)
//      Affichez ces deux nombres en demandant à l'utilisateur d'en donner la somme
//      Continuez à lui demander tant que la réponse est mauvaise.
//      À la fin du programme, affichez à l'utilisateur le nombre d'erreurs qu'il a commises.
const EXO_11_SUBMIT = document.querySelector('#exo_11_submit');

EXO_11_SUBMIT.addEventListener('click', function() {
    
})