<head>
    <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="css/global.css">
    <script src="bootstrap/js/jquery.min.js"></script>
    <script src="bootstrap/js/bootstrap.min.js"></script>

    <link href="stars/css/star-rating.css" media="all" rel="stylesheet" type="text/css" />
    <link href="stars/css/theme-krajee-svg.css" media="all" rel="stylesheet" type="text/css" />
    <script src="stars/js/star-rating.js" type="text/javascript"></script>
    <script src="../stars/js/star-rating_locale_es.js"></script>

    <meta content="text/html; charset=ISO-8859-1" http-equiv="content-type">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title><?php echo $title ?></title>
</head>

<body>
    <nav class="navbar navbar-default navbar-fixed-top">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>

                <p class="navbar-text"> Ceamyt</p>
            </div>
    
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <?php
                session_start();
                if (!isset($_SESSION['user'])) {
                ?>
                    <form action="../handlers/login.php?action=login" method="post" class="navbar-form navbar-right">
                        <div class="form-group">
                            <input name="user" type="text" class="form-control" placeholder="Usuario">
                        </div>
                        <div class="form-group">
                            <input name="pass" type="password" class="form-control" placeholder="Contraseña">
                        </div>
                        <button type="submit" class="btn btn-default">Iniciar sesion</button>
                    </form>
                    <?php
                } else {
                ?>
                    <a href="../handlers/login.php?action=logout">
                        <button type="button bt" style="margin-left: 20px;" class="btn btn-default navbar-right navbar-btn">Cerrar sesion</button>
                    </a>
                <p class="navbar-text navbar-right"> Bienvenido <?php echo $_SESSION['user']['name']; ?> </p>
                    <?php
                }
                ?>

            </div>
        </div>
    </nav>

    <div class="container">
<?php
    if (isset($_SESSION["error"]))
    {
        ?>
        <div class="alert alert-danger alert-dismissible" role="alert">
            <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <strong>¡Error!</strong> <?php echo $_SESSION["error"] ?>
        </div>
        <?php
        unset($_SESSION["error"]);

    }
    if (isset($_SESSION["success"]))
    {
        ?>
        <div class="alert alert-success alert-dismissible" role="alert">
            <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <strong>¡Eureka!</strong> <?php echo $_SESSION["success"] ?>
        </div>
        <?php
        unset($_SESSION["success"]);
    }
    if (isset($_SESSION["info"]))
    {
        ?>
        <div class="alert alert-info alert-dismissible" role="alert">
            <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <?php echo $_SESSION["info"] ?>
        </div>
        <?php
        unset($_SESSION["info"]);
    }



