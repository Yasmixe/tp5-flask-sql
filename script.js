var numero = 1;
var point = 0;

const etudiant = [
    {
     nom:'john',
     prenom: 'doe',
     note:14           }, 
    {
     nom:'bob',
     prenom: 'carlton',
     note:7           }, 
    {
     nom:'rayane',
     prenom: 'smith',
     note:13           }];

    
// ajouter une ligne a chaque fois qu'on veut ajouter une ligne
function addline(table, numero, nom, prenom, points){
    const newRow = table.insertRow(-1); // -1: on insere la ligne f la fin ta3 le tableau 
    // 0 : f debut
    const Numberr = newRow.insertCell(0);
    Numberr.innerHTML = numero;
    const Name = newRow.insertCell(1);
    Name.innerHTML = nom;
    const secondname = newRow.insertCell(2);
    secondname.innerHTML = prenom;
    const Points = newRow.insertCell(3);
    Points.innerHTML = points;
    const Select = newRow.insertCell(4);
    Select.innerHTML = '<input type="checkbox" name="check" id="">';

}
//ajouter lobjet etudiant
function ajouterstatique(){
    /*const tablee = document.getElementById("table");
    // dabord on ajoute f le tableau les infos ta3 etudiant:
    etudiant.forEach(function(etudiant){
        addline(tablee, numero, etudiant.nom, etudiant.prenom, etudiant.note);
        numero++;
        point += etudiant.note;
        miseajour(numero, point);
   });*/

}

ajouterstatique();
//fnct ajouter on fait lappelle ta3 la fonction addline
function ajouter() {
    const nom = document.getElementById("name").value;
    const prenom = document.getElementById("secondname").value;
    const points = parseFloat(document.getElementById("range").value); // Convertir points en nombre
    const tablee = document.getElementById("table");

    if (nom.trim() === "" || prenom.trim() === "" || isNaN(points)) {
        alert("Veuillez remplir tous les champs correctement.");
    } else {
        addline(tablee, numero, nom, prenom, points);
        point += points;
        numero++;
// maj again ta3 le resume
        miseajour(numero, point);
    }
}

//fnct remove pour supprimer les ligne checked
function supprimer() {
    const table = document.getElementById("table");
    const checkboxes = table.querySelectorAll('input[type="checkbox"]');
    var check = false;
    
    for (let i = checkboxes.length - 1; i >= 0; i--) {
        if (checkboxes[i].checked) {
            table.deleteRow(i + 1); 
            numero--; 
            check = true;
            // hna il faut modifier le num de la derniere ligne
        }
    }
        if (!check) {
        alert("Cochez au moins une case pour pouvoir la supprimer.");
        }   
        
    //maj ta3 resume again 
    miseajour(numero, point);
    // c une boucle pour corriger la case des nombres et les rendre de 1....tab.length
    var cpt =1;
    for (var i = 1; i < table.rows.length; i++) {
        var row = table.rows[i];
        row.cells[0].innerText= cpt;
        cpt++;
        }
}

// on show f la console
function showtable() {
    var tablee = document.getElementById("table");

    for (var i = 1; i < tablee.rows.length; i++) {
        var row = tablee.rows[i];
        var objet_etudiants = {
            num: row.cells[0].innerText,
            nom: row.cells[1].innerText,
            prenom: row.cells[2].innerText,
            points: row.cells[3].innerText,
        };
        console.log(objet_etudiants);
    }
}

//maj a chaque fois quon ajoute ou on supprime une ligne.

function miseajour() {
    const table = document.getElementById("table");
    const lines = document.getElementById("ligne");
    const totale = document.getElementById("total");

    const numRows = table.rows.length - 1; // On soustrait 1 pour exclure la ligne d'en-tête
    let totalPoints = 0;

    for (let i = 1; i <= numRows; i++) {
        const row = table.rows[i];
        totalPoints += parseFloat(row.cells[3].innerText);
    }

    lines.innerHTML = '<p>' + numRows + ' lignes</p>';
    totale.innerHTML = '<p> totale : ' + totalPoints + '</p>';
}

