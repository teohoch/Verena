<html>
<?php
global $title;
$title= "Horarios";
include ("include/header.php");
include_once ("include/database.php");
$db = database();
$profesores = $db->query("SELECT * FROM users WHERE isTeacher =1;");

if (isset($_SESSION["user"])) {
    $user = $_SESSION["user"];
}
?>
<h1>Horarios de Cada profesor</h1>
<row>
    <div class="col-sm-4">
       <span style="color: red"> Rojo</span>=> Horario reservado
    </div>
    <div class="col-sm-4">
        <span style="color: blue"> Azul </span>=> Horario Disponible para reservar
    </div>
    <div class="col-sm-4">
        <button class="btn btn-primary">Cancelar Reserva</button> => Cancelar Reserva existente
    </div>
</row>
<br>
<?php


foreach ($profesores as $row)
{
   ?>
    <row>
        <div class="col-sm-12 ">
            <h3>Horario Profesor <?php echo $row["name"] ?></h3>
        </div>
    </row>
    <row>
        <div class="col-sm-12">
            <?php
            if (isset($user) && $user["isTeacher"]==0)
            {
                $check_query = $db->prepare("SELECT * FROM rating WHERE userIDTeacher = ? AND userIDStudent = ? ;");
                $check_query->execute([$row["id"],$user["id"]]);
                $check = $check_query->fetch();
                if ($check)
                {
                    ?>
                    <form class="form-inline" method="post" action="handlers/rating.php?action=update" role="form">
                        <div class="form-group">
                            <input type="number" name="rating" step="0.5" class="form-control rating" value="<?php echo $check["value"] ?>" data-size="xs" data-show-caption="false">
                        </div>
                        <input type="hidden" name="id_rating" value="<?php echo $check["id"] ?>">
                        <button type="submit" class="btn btn-default">Evaluar</button>
                    </form>
                    <?php

                }else{
                    $average_query = $db->prepare("SELECT avg(value) as val FROM rating WHERE userIDTeacher = ? ;");
                    $average_query->execute([$row["id"]]);
                    $average = $average_query->fetch();
                    $average=$average["val"];
                    ?>
                    <form class="form-inline" method="post" action="handlers/rating.php?action=create" role="form">
                        <div class="form-group">
                            <input type="number" name="rating" step="0.5" class="form-control rating" value="<?php echo $average ?>" data-size="xs" data-show-caption="false">
                        </div>
                        <input type="hidden" name="id_teacher" value="<?php echo $row["id"] ?>">
                        <input type="hidden" name="id_user" value="<?php echo $user["id"] ?>">

                        <button type="submit" class="btn btn-default">Evaluar</button>
                    </form>
                    <?php

                }
                


            }else{
                $average_query = $db->prepare("SELECT avg(value) as val FROM rating WHERE userIDTeacher = ? ;");
                $average_query->execute([$row["id"]]);
                $average = $average_query->fetch();
                $average=$average["val"];
                ?>
                <form class="form-inline" role="form">
                    <div class="form-group">
                        <input type="number" step="0.5" class="form-control rating" data-disabled="true" value="<?php echo $average ?>" data-show-caption="false" data-size="xs">
                    </div>
                </form>
                <?php
            }
            ?>

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
                for ($i = 1; $i<=12;$i++)
                {
                ?>
                <tr>
                    <td> <?php $hora_inicio = implode(":",[($i+7),"00"]); $hora_termino= implode(":",[($i+8),"00"]); echo implode("-",[$hora_inicio,$hora_termino])?> </td>
                    <?php
                    $query = $db->prepare("SELECT * FROM bloque_horario WHERE bloque = ? AND userIDTeacher= ? ;");
                    $query->execute([$i,$row["id"]]);
                    $bloques = $query->fetchAll();
                    foreach ($bloques as $bloque)
                    {
                        if ($bloque["disponible"]==1){
                            if ($bloque["userIDStudent"]==null)
                            {
                                if (isset($user) && $user["isTeacher"]==0){
                                    ?>
                                    <td><a href="/handlers/reservation.php?action=reservar&id_bloque_horario=<?php echo $bloque["id"] ?> ">Disponible</a></td>
                                    <?php
                                }else{
                                    ?>
                                    <td style="color: blue">Disponible</td>
                                    <?php
                                }

                            }else{
                                if ($bloque["userIDStudent"]==$user["id"]){
                                    # Si el que reservo el horario es el mismo usuario, puede cancelar la reserva
                                    ?>
                                    <td >
                                        <a href="/handlers/reservation.php?action=cancelar&id_bloque_horario=<?php echo $bloque["id"] ?> ">
                                            <button class="btn btn-primary btn-sm">Cancelar Reserva</button>
                                        </a>
                                    </td>
                                    <?php
                                }else{
                                    ?>
                                    <td style="color: red">Reservado</td>
                                    <?php
                                }
                            }
                        }else{
                            ?>
                            <td>-</td>
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
    }

    ?>
            </div>
    </row>
    </div>
</body>
</html>

