const $formulario = document.getElementById('Form');
const $Nombre = document.getElementById('Nombre');
const $CH4pmm = document.getElementById('CH4ppm');
const $C2H4ppm = document.getElementById('C2H4ppm');
const $C2H2ppm = document.getElementById('C2H2ppm');


$formulario.addEventListener('submit', function(e){
    let nombre = String($Nombre.value).trim();
    if (nombre.length == 0){
        alert('El nombre no puede estar vacío');
        e.preventDefault()
    }
    if ($CH4pmm.value + $C2H4ppm.value + $C2H2ppm.value == 0){
        alert('CH4ppm, C2H4ppm y C2H2ppm no pueden sumar 0');
        e.preventDefault()
    }
});