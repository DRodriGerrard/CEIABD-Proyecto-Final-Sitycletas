// Autocompletar con la fecha actual del navegador (mínimo 1 mayo 2025)
const inputFecha = document.getElementById('fecha');
const ahora = new Date();
ahora.setMinutes(ahora.getMinutes() - ahora.getTimezoneOffset());

const fechaMin = new Date("2025-05-01T00:00");
const fechaFinal = (ahora > fechaMin ? ahora : fechaMin).toISOString().slice(0,16);
inputFecha.value = fechaFinal;