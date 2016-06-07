
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
    var nNotas = GetURLParameter("nNotas");
    var forma = $("#formNotas");
    var linea = '<row>        <div class="form-group col-sm-6 vcenter">        <label class="col-sm-2" for="nombreAsignatura{2}">Nota {1}</label>    <div class="col-sm-8">        <input type="number" class="form-control" id="nombreAsignatura{2}" placeholder="55" max="100" min="0" data-native-error="Por favor rellene este campo correctamente"  required>    <div class="help-block with-errors"></div>        </div>        </div>        <div class="form-group col-sm-6 vcenter">        <label  class="col-sm-2" for="nTotalNotas{2}">Ponderacion Nota</label>    <div class="col-sm-8">        <input type="number" class="form-control" id="nTotalNotas{2}" placeholder=30 max="100" min="0" data-native-error="Por favor rellene este campo correctamente"  required>    <div class="help-block with-errors"></div>        </div>        </div>        </row>';

    for (i=0; i<nNotas; i++)
    {
        var linea2 = linea.replace("{1}",i+1).replace("{2}",i);
        forma.append(linea2);
    }
    forma.append('<button type="submit" class="btn btn-default">Enviar</button>');

});