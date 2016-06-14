<html>

<?php
global $title;
$title= "Horarios";
include ("include/header.php");
include_once ("include/database.php");
$db = database();


if (isset($_SESSION["user"])) {
    $user = $_SESSION["user"];
    if ($user["isTeacher"]==1)
    {
        ?>
        <row>
            <div class="col-sm-12">
                <h1>Perfil de <?php echo $user["name"]?></h1>
            </div>
        </row>
        <row>
            <div class="col-sm-6">
                <p>Aqui puede habilitar e inhabilitar los horarios en los que desea hacer clases.</p>
            </div>
        </row>
        <row>
            <div class="col-sm-12">
                <div class="table-responsive table-bordered table-condensed">
                    <table class="table">
                        <thead>
                        <tr>
                            <th>Horario</th>
                            <th>Lunes</th>
                            <th>Martes</th>
                            <th>Miercoles</th>
                            <th>Jueves</th>
                            <th>Viernes</th>
                            <th>Sabado</th>
                            <th>Domingo</th>
                        </tr>
                        </thead>
                        <tbody>
                        <?php
                        for ($i = 1; $i<=12;$i++) {
                            ?>
                            <tr>
                                <td> <?php $hora_inicio = implode(":", [($i + 7), "00"]);
                                    $hora_termino = implode(":", [($i + 8), "00"]);
                                    echo implode("-", [$hora_inicio, $hora_termino]) ?> </td>
                                <?php

                                $query = $db->prepare("SELECT * FROM bloque_horario WHERE bloque = ? AND userIDTeacher= ? ;");
                                $query->execute([$i,$user["id"]]);
                                $bloques = $query->fetchAll();
                                foreach ($bloques as $bloque)
                                {
                                    if ($bloque["disponible"]==1)
                                    {
                                        ?>
                                        <td>
                                            <a href="handlers/reservation.php?action=inhabilitar&id_bloque_horario=<?php echo $bloque["id"]; ?>">
                                                <button class="btn btn-warning btn-sm"> Inhabilitar Horario </button>
                                            </a>
                                        </td>

                                        <?php
                                    }else{
                                        ?>
                                        <td>
                                            <a href="handlers/reservation.php?action=habilitar&id_bloque_horario=<?php echo $bloque["id"]; ?>">
                                                <button class="btn btn-sm"> Habilitar Horario </button>
                                            </a>
                                        </td>

                                        <?php

                                    }
                                }
                                ?>
                            </tr>
                            <?php
                        }
                        ?>

                        </tbody>
                    </table>
                </div>
                <?php


                ?>
            </div>
        </row>

        <?php


    }else{

        $_SESSION["error"] = "Debe ser profesor para ingresar al perfil de profesor";
        header('Location: /horarios.php');
    }
}else{
    $_SESSION["error"] = "Debe haber iniciado sesion para ingresar al perfil";
    header('Location: /horarios.php');
}
?>