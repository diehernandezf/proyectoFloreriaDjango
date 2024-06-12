$(document).ready(function(){
    
});

$(function(){
    $("#miFormulario").validate({
        rules:{
            txtUsername:{
                required:true
            },
            txtEmail:{
                required:true
            },
            txtPassword:{
                required:true
            }
        },
        messages:{
            txtUsername:{
                required: "Campo obligatorio."
            },
            txtEmail:{
                required: "Campo obligatorio"
            },
            txtPassword:{
                required: "Campo obligatorio"
            }
        }
        
    })
})