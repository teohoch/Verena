
$(document).ready(function(){

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
    $("#asignatura").val(GetURLParameter("asignatura"));
    $("#notaAprobatoria").val(GetURLParameter("notaAprobatoria"));
    $("#notaReprobatoria").val(GetURLParameter("notaReprobatoria"));

    var nNotas = GetURLParameter("nNotas");

    $("#nNotas").val(nNotas);

    var forma = $("#formNotas");
    var linea = '<row>        <div class="form-group col-sm-6 vcenter">        <label class="col-sm-2" for="valorNota{2}">Nota {1}</label>    <div class="col-sm-8">        <input type="number" class="form-control" name="valorNota{2}" id="valorNota{2}" placeholder="4" max="7" min="1" step="0.1" data-native-error="Por favor rellene este campo correctamente"  required>    <div class="help-block with-errors"></div>        </div>        </div>        <div class="form-group col-sm-6 vcenter">        <label  class="col-sm-2" for="ponderacionNota{2}">Ponderacion Nota</label>    <div class="col-sm-8">        <input type="number" class="form-control" name="ponderacionNota{2}" id="ponderacionNota{2}" placeholder=30 max="100" min="0" data-native-error="Por favor rellene este campo correctamente"  required>    <div class="help-block with-errors"></div>        </div>        </div>        </row>';

    for (i=0; i<nNotas; i++)
    {
        var linea2 = linea.replace(/\{1\}/gi,i+1);
        var linea3 = linea2.replace(/\{2\}/gi,i)
        forma.append(linea3);
    }
    forma.append('<button type="submit" class="btn btn-default">Enviar</button>');

});