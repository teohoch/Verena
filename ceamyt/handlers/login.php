<?php
include_once ("../include/database.php");

$db = database();

# Se hacen distintas cosas dependiendo del valor del parámetro "action" #
session_start();
if( $_GET['action'] == 'login' )
{
    $query = $db->prepare("SELECT * FROM users WHERE username= ? AND password = ?");
    $query->execute([$_POST["user"], $_POST["pass"]]);
    $user = $query->fetch();
    if ($user){

        $_SESSION['user'] = $user;
        $_SESSION['success'] = "¡Inicio de sesion exitoso!";
        if ($user["isTeacher"]==1)
        {
            header('Location: ../perfil.php');
        }else{
            header('Location: ../horarios.php');
        }

    }else{
        $_SESSION['error'] = "Usuario/Contraseña erronea";
        header('Location:'. $_SERVER['HTTP_REFERER']);
    }


    
} else if( $_GET['action'] == 'logout' )
{
    session_destroy(); # Borra las variables de sessión
    session_start();
    $_SESSION['info'] = "Sesion cerrada correctamente";
    header('Location: ../horarios.php');
}else{
    header('Location: ../horarios.php');
}

?>
