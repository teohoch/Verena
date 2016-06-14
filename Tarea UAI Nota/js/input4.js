

function GetURLParameter(sParam)
{
    var sPageURL = window.location.search.substring(1);
    var sURLVariables = sPageURL.split('&');
    for (var i = 0; i < sURLVariables.length; i++)
    {
        var sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] == sParam)
        {
            return decodeURIComponent(sParameterName[1]);
        }
    }
}
function capitalize(s)
{
    return s && s[0].toUpperCase() + s.slice(1);
}



$(document).ready(function(){

    var nNotas = GetURLParameter("nNotas");
    var aprobatoria = GetURLParameter("notaAprobatoria")
    var reprobatoria = GetURLParameter("notaReprobatoria")
    var promedioActual = 0;
    var porcentajeActual = 0;

    for (i=0; i<nNotas; i++)
    {
        var tempA = parseInt(GetURLParameter("valorNota"+i))
        var tempB = parseInt(GetURLParameter("ponderacionNota"+i))
        promedioActual = promedioActual + (tempA * (tempB/100))
        porcentajeActual = porcentajeActual + (tempB/100)
    }

    var nota = $("#nota")
    var estado = $("#estado")
    var notas_nesesarias = $("#lista")
    nota.append(promedioActual.toFixed(2))

    if (promedioActual<reprobatoria)
    {
        nota.css("color","red")
        estado.css("color","red")
        estado.append("Reprobando")

        var nesesaria = reprobatoria-promedioActual
        var nesesaria2 = aprobatoria-promedioActual
        var a = (nesesaria/(1-porcentajeActual)).toFixed(2)
        var b = (nesesaria2/(1-porcentajeActual)).toFixed(2)

        if(a>7.0)
        {
            var ap = '<row>                   <div class="col-sm-12">        <li>        <p>Lamentamos informarte que no hay forma de no reprobar este ramo con las pruebas restantes. </p>    </li>    </div>    </div>    </row>'
        }else
        {
            var ap = '<row>                   <div class="col-sm-12">        <li>        <p>Nesesitas <span style="color: red">{1}</span> de promedio en el resto de tus notas para no reprobar </p>    </li>    </div>    </div>    </row>'
            var ap = ap.replace("{1}", a)
        }

        if(b>7.0)
        {
            var ap2 = '<row>                 <div class="col-sm-12">        <li>        <p>No existe forma de aprobar con las notas que tienes sin el examen. </p>    </li>    </div>    </div>    </row>'

        }else
        {
            var ap2 = '<row>                 <div class="col-sm-12">        <li>        <p>Nesesitas <span style="color: blue">{1}</span> de promedio en el resto de tus notas para aprobar sin examen </p>    </li>    </div>    </div>    </row>'
            var ap2 = ap2.replace("{1}", b)
        }



        notas_nesesarias.append(ap)
        notas_nesesarias.append(ap2)
    }else{
        if (promedioActual>aprobatoria)
        {
            nota.css("color","blue")
            estado.css("color","blue")
            estado.append("Aprobando")
        }else {
            $("#wrap_estado").empty()
            $("#wrap_estado").append("Debera rendir examen para pasar, pero tiene promedio mayor a la nota reprobatoria")


            var nesesaria2 = aprobatoria-promedioActual

            var b = (nesesaria2/(1-porcentajeActual)).toFixed(2)

            var ap2 = '<row>                    <div class="col-sm-12">        <li>        <p>Nesesitas <span style="color: red">{1}</span> de promedio en el resto de tus notas para aprobar sin examen </p>    </li>    </div>    </div>    </row>'
            var ap2 = ap2.replace("{1}", b)

            notas_nesesarias.append(ap2)

        }
    }



    

    var asignatura = GetURLParameter("asignatura");
    var linea = '<row>        <div class="col-sm-4 col-sm-offset-4">        <h1>Asignatura {0}</h1>        </div>        </row>        '.replace("{0}",capitalize(asignatura))
    $("#container").prepend(linea)
    


});