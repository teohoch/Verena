<?php
include_once("../include/database.php");
$db = database();
session_start();
if (isset($_SESSION["user"]))
{
    $user =$_SESSION["user"];
    $id_bloque = $_GET["id_bloque_horario"];

    $query= $db->prepare("SELECT * FROM bloque_horario WHERE id = ? ;");
    $query->execute([$id_bloque]);
    $bloque_en_db = $query->fetch();

    if ($user["isTeacher"]==0)
    {
        if( $_GET['action'] == 'reservar' )
        {
            if ($bloque_en_db["disponible"] == 1 and $bloque_en_db["userIDStudent"]==null ){
                $update_query = $db->prepare("UPDATE bloque_horario SET userIDStudent= ? WHERE id= ?;");
                $update_query->execute([$user["id"], $bloque_en_db["id"]]);

                $_SESSION['success'] = "EL bloque seleccionado a sido reservado con exito";
                header('Location: /horarios.php');

            }else{
                $_SESSION['error'] = "EL bloque seleccionado no esta disponible, seleccione otro";
                header('Location: /horarios.php');
            }
        }elseif ($_GET['action'] == 'cancelar'){
            if($bloque_en_db["userIDStudent"]==$user["id"])
            {
                $update_query = $db->prepare("UPDATE bloque_horario SET userIDStudent= NULL WHERE id= ?;");
                $update_query->execute([$bloque_en_db["id"]]);
                $_SESSION['success'] = "La reserva ha sido cancelada con exito";
                header('Location: /horarios.php');
            }else{
                $_SESSION['error'] = "Solo el estudiante que realizo la reserva puede cancelarla.";
                header('Location: /horarios.php');
            }
        }
    }else{
        if( $_GET['action'] == 'habilitar' )
        {
            if($bloque_en_db["userIDTeacher"]==$user["id"])
            {
                $update_query = $db->prepare("UPDATE bloque_horario SET disponible= TRUE WHERE id= ?;");
                $update_query->execute([$bloque_en_db["id"]]);
                $_SESSION['success'] = "Bloque habilitado con exito";
                header('Location: /perfil.php');
            }else{
                $_SESSION['error'] = "Solo el profesor que realiza este bloque puede habilitarlo.";
                header('Location: /perfil.php');
            }


        }elseif ($_GET['action'] == 'inhabilitar')
        {
            if($bloque_en_db["userIDTeacher"]==$user["id"])
            {
                $update_query = $db->prepare("UPDATE bloque_horario SET disponible= FALSE WHERE id= ?;");
                $update_query->execute([$bloque_en_db["id"]]);
                $_SESSION['success'] = "Bloque inhabilitado con exito";
                header('Location: /perfil.php');
            }else{
                $_SESSION['error'] = "Solo el profesor que realiza este bloque puede inhabilitarlo.";
                header('Location: /perfil.php');
            }

        }

    }
}else{
    $_SESSION['error'] = "Debe haber iniciado sesion para reservar horas";
    header('Location: /horarios.php');

}






