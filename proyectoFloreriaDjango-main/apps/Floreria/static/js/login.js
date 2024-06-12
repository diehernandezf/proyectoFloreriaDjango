console.log("Hola lo pibe");
/* ESTAS VALIDACIONES NO FUNCIONAN CON UN FORM-GROUP CON VALIDACIONES DE BOOSTRAP */
document.getElementById("valUsername").style.display = "none"
document.getElementById("valContrasena").style.display = "none"

function validacionDeDatos() {
    let usuario = document.getElementById("txtUsername").value;
    let contrasena = document.getElementById("txtContrasena").value;

    if (usuario.length == 0) {
        document.getElementById("valUsername").style.display = "inline"
        document.getElementById("txtUsername").classList.add("is-invalid")
    } else {
        document.getElementById("valUsername").style.display = "none"
        document.getElementById("txtUsername").classList.remove("is-invalid")
        document.getElementById("txtUsername").classList.add("is-valid")
    }
    if (contrasena.length == 0) {
        document.getElementById("valContrasena").style.display = "inline"
        document.getElementById("txtContrasena").classList.add("is-invalid")
    } else {
        document.getElementById("valContrasena").style.display = "none"
        document.getElementById("txtContrasena").classList.remove("is-invalid")
        document.getElementById("txtContrasena").classList.add("is-valid")
    }
}

document.getElementById("mostrar").style.display = "none";

function password(){
    let input = document.getElementById("txtContrasena");
    if (input.type == "password") {
        input.type = "text";
        document.getElementById("ocultar").style.display = "inline";
        document.getElementById("mostrar").style.display = "none";
    } else{
        input.type = "password"
        document.getElementById("ocultar").style.display = "none";
        document.getElementById("mostrar").style.display = "inline";
    }
}