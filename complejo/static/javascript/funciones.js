// let hora_inicial = document.getElementById('hora_inicio');
// let hora_final = document.getElementById('hora_final');
// const costo = document.getElementById('pago').value;



// hora_inicial.addEventListener('click', () =>{
//     let e = document.getElementById("hora_inicio");
//     let value = e.options[e.selectedIndex].value;
//     hora_final.selectedIndex = parseInt(value)

//     let option= hora_final.options[0];
//     option.disabled = false;
//     let option1= hora_final.options[1];
//     option1.disabled = false;
//     let option2= hora_final.options[2];
//     option2.disabled = false;
//     let option3= hora_final.options[3];
//     option3.disabled = false;
//     let option4= hora_final.options[4];
//     option4.disabled = false;
//     let option5= hora_final.options[5];
//     option5.disabled = false;
//     let option6= hora_final.options[6];
//     option6.disabled = false;
//     let option7= hora_final.options[7];
//     option7.disabled = false;
//     let option8= hora_final.options[8];
//     option8.disabled = false;
//     let option9= hora_final.options[9];
//     option9.disabled = false;
//     let option10= hora_final.options[10];
//     option10.disabled = false;
//     let option11= hora_final.options[11];
//     option11.disabled = false;
//     let option12= hora_final.options[12];
//     option12.disabled = false;
//     let option13= hora_final.options[13];
//     option13.disabled = false;




// });

// hora_final.addEventListener('click', () =>{
//     let e = document.getElementById("hora_final");
//     let value = e.options[e.selectedIndex].value;

//     let e1 = document.getElementById("hora_inicio");
//     let value1 = e1.options[e1.selectedIndex].value;
//     let hora =((parseInt(value)-parseInt(value1))+1);

//     let pago = document.getElementById('pago')

//     let total = costo*hora
//     pago.value = total



//     let option1 = hora_final.options[value1-1];
//     option1.disabled = true;
//     let option2 = hora_final.options[value1-2];
//     option2.disabled = true;
//     let option3 = hora_final.options[value1-3];
//     option3.disabled = true;
//     let option4 = hora_final.options[value1-4];
//     option4.disabled = true;
//     let option5 = hora_final.options[value1-5];
//     option5.disabled = true;
//     let option6 = hora_final.options[value1-6];
//     option6.disabled = true;
//     let option7 = hora_final.options[value1-7];
//     option7.disabled = true;
//     let option8 = hora_final.options[value1-8];
//     option8.disabled = true;
//     let option9 = hora_final.options[value1-9];
//     option9.disabled = true;
//     let option10 = hora_final.options[value1-10];
//     option10.disabled = true;
//     let option11 = hora_final.options[value1-11];
//     option11.disabled = true;
//     let option12 = hora_final.options[value1-12];
//     option12.disabled = true;
//     let option13 = hora_final.options[value1-13];
//     option13.disabled = true;

// });


// // Validación de los horarios
// $(function(){
//     $("#fecha_reserva").change(function () {
//       var fecha = $(this).val();

//       $.ajax({
//         url: '/validarFecha/',
//         data: {
//           'fecha': fecha
//         },
//         dataType: 'json',
//         success: function (data) {
//           if (data.is_taken) {
//             // alert("La fecha ya existe");
//             document.getElementById("respuesta").innerHTML = " ";
//           }
//           else {
//             document.getElementById("respuesta").innerHTML = " ";
//           }
//         }
//       });

//     });
//   });