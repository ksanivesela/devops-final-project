const API="/api";

async function cargarUsuarios(){

    const respuesta=await fetch(API+"/users");

    const usuarios=await respuesta.json();

    const tabla=document.getElementById("tablaUsuarios");

    tabla.innerHTML="";

    usuarios.forEach(usuario=>{

        tabla.innerHTML+=`

        <tr>

            <td>${usuario.id}</td>

            <td>${usuario.nombre}</td>

            <td>${usuario.correo}</td>

            <td>

                <button
                    class="eliminar"
                    onclick="eliminar(${usuario.id})">

                    Eliminar

                </button>

            </td>

        </tr>

        `;

    });

}

async function guardarUsuario(){

    const nombre=document.getElementById("nombre").value;

    const correo=document.getElementById("correo").value;

    if(nombre=="" || correo==""){

        alert("Complete todos los campos");

        return;

    }

    await fetch(API+"/users",{

        method:"POST",

        headers:{

            "Content-Type":"application/json"

        },

        body:JSON.stringify({

            nombre:nombre,

            correo:correo

        })

    });

    document.getElementById("nombre").value="";

    document.getElementById("correo").value="";

    cargarUsuarios();

}

async function eliminar(id){

    await fetch(API+"/users/"+id,{

        method:"DELETE"

    });

    cargarUsuarios();

}

cargarUsuarios();