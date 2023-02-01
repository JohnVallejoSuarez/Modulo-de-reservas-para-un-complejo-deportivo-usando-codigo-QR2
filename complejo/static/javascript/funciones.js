let opI = document.getElementById('hora_inicio');
let opF = document.getElementById('hora_final');
let pago = document.getElementById('hora_final');


opI.addEventListener('click', () =>{
    let e = document.getElementById("hora_inicio");
    let value = e.options[e.selectedIndex].value;
    console.log(value);
    opF.selectedIndex = parseInt(value)
});

