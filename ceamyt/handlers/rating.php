<?php
include_once("../include/database.php");
$db = database();
session_start();
if (isset($_SESSION["user"]))
{
    $user =$_SESSION["user"];




    if ($user["isTeacher"]==0)
    {
        if( $_GET['action'] == 'create' )
        {
            $id_teacher = $_POST["id_teacher"];
            $id_user = $_POST["id_user"];
            $rating = $_POST["rating"];
            if ($id_user==$user["id"] ){
                $insert_query = $db->prepare("INSERT INTO rating (userIDTeacher, userIDStudent, value) VALUE (? , ? , ?);");
                $insert_query->execute([$id_teacher, $id_user, $rating]);

                $_SESSION['success'] = "Su evaluacion ha sido guardada con exito.";
                header('Location: /horarios.php');

            }else{
                $_SESSION['error'] = "Solamente el usuario asociado a la valoracion puede crear la valoracion";
                header('Location: /horarios.php');
            }
        }elseif ($_GET['action'] == 'update'){
            $id_rating = $_POST["id_rating"];
            $rating = $_POST["rating"];
            $check_query = $db->prepare("SELECT * FROM rating WHERE id = ? ;");
            $check_query->execute([$id_rating]);
            $check = $check_query->fetch();
            if($check["userIDStudent"]==$user["id"])
            {
                $insert_query = $db->prepare("UPDATE rating SET value = ? WHERE id= ? ;");
                $insert_query->execute([$rating, $id_rating]);

                $_SESSION['success'] = "Su valoracion ha sido actualizada con exito";
                header('Location: /horarios.php');
            }else{
                $_SESSION['error'] = "Solamente el usuario asociado a una valoracion puede modificar dicha valoracion.";
                var_dump($check);
                var_dump($user);
            }
        }
    }
}else{
    $_SESSION['error'] = "Debe haber iniciado sesion para evaluar profesores";
    header('Location: /horarios.php');

}