<!DOCTYPE html>
<html lang="en">
<div id="contenido">
    <STYLE> 
BODY { background: url(https://fbcdn-sphotos-e-a.akamaihd.net/hphotos-ak-xtf1/t31.0-8/13392062_10209407230076069_6872026260508240158_o.jpg) center } 
</STYLE> 
<title>Ceamyt</title>
<meta charset="utf-8">
 <img src="https://fbcdn-sphotos-c-a.akamaihd.net/hphotos-ak-xat1/v/t1.0-9/13342993_10209407228076019_5305967543272292761_n.jpg?oh=95afdcbb4d88c435c7d7b0319ba2a423&oe=5808CCFF&__gda__=1473179197_21a2616a14ec57a3a4b69d5731ebcd3a">
</head>
<body id="page1">
  <body leftmargin="430" topmargin="0" marginwidth="430" marginheight="0" >
<div class="wrap">
  <header>
    <div class="container">
      <p align="left">
      <nav>
        <ul>
          <li><a href="index.php" class="m1">Home Page</a></li>
          <li><a href="about-us.php" class="m2">Nuestros Profesores</a></li>
          <li><a href="articles.php" class="m3">Artículos</a></li>
          <li class="current"><a href="contact-us.php" class="m4">Contáctenos</a></li>
          <li><a href="horarios.php" class="m5">Horarios</a></li>
          <li class="last"><a href="information.php" class="m6">Quienes somos</a></li>
        </ul>
      </nav>
    </div>
  </header>
    <center>
  <div class="container">
    <section id="content">
       <div class="inside">
        <h2>Nuestros <span>Contactos</span></h2>
        <div class="address">
          <address>
          <strong>Zip Code:</strong> 50122<br>
          <strong>Country:</strong> Chile<br>
          <strong>Telephone:</strong> +56 9 71370799 (WhatsApp)<br>
		  <strong>Dirección:</strong> Los Abedules 1199, Bosques de Montemar, Concón.<br>
          </address>
          <div class="extra-wrap">
            <h4>¡INSCRÍBASE YA!</h4>
            <p>Pida información y simplifíquese la vida.</p>
          </div>
        </div>
		
	 <?php
		if(isset($_POST['email'])) {

$email_to = "contacto@ceamyt.cl";
$email_subject = "Contacto desde el sitio web";

if(!isset($_POST['first_name']) ||
!isset($_POST['email']) ||
!isset($_POST['telephone']) ||
!isset($_POST['comments'])) {

echo "<h2>Ocurrió un error y el formulario no ha sido enviado</h2></br>";
echo "<h2><span>Por favor, vuelva atrás y verifique la información ingresada</span></h2>";
die();
}

$email_message = "Detalles del formulario de contacto:\n\n";
$email_message .= "Nombre: " . $_POST['first_name'] . "\n";
$email_message .= "E-mail: " . $_POST['email'] . "\n";
$email_message .= "Teléfono: " . $_POST['telephone'] . "\n";
$email_message .= "Comentarios: " . $_POST['comments'] . "\n\n";


$headers = 'From: '.$email_from."\r\n".
'Reply-To: '.$email_from."\r\n" .
'X-Mailer: PHP/' . phpversion();
@mail($email_to, $email_subject, $email_message, $headers);

echo "<h2>El formulario <span>se ha enviado con éxito!</span></h2>";
}?>
        <h2>Formulario de <span>Contacto</span></h2>
        <form id="contacts-form" name="frmContacto" method="post" action="?">
            <div class="field">
              <label for="first_name">Nombre: *</label>
              <input type="text" name="first_name" maxlength="80" size="25">
            </div>
            <div class="field">
              <label for="email">Dirección de E-mail: *</label>
             <input type="text" name="email" maxlength="80" size="35">
            </div>
            <div class="field">
              <label for="telephone">Telefono: *</label>
             <input type="text" name="telephone" maxlength="80" size="35">
            </div>
            <div class="field extra">
              <label for="comments">Mensaje: *</label>
              <textarea name="comments" maxlength="500" cols="30" rows="5"></textarea>
            </div>
            <input type="submit" value="Enviar">
        </form>
      </div>
    </section>
  </div>
</div>
</div>
</center>
<footer>
  <div class="footerlink">
    <p class="lf">Copyright &copy;<a href="www.ceamyt.cl">ceaMYT</a> -Todos los derechos reservados</p>
    <div style="clear:both;"></div>
  </div>
</footer>
</body>
</html>
