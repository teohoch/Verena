

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


    

    var asignatura = GetURLParameter("asignatura");
    var linea = '<row>        <div class="col-sm-4 col-sm-offset-4">        <h1>Asignatura {0}</h1>        </div>        </row>        '.replace("{0}",capitalize(asignatura))
    $("#container").prepend(linea)
    


});