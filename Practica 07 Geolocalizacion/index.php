<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>IOT Geolocalización</title>

        <link rel="stylesheet" href="css/index.css">
        <script src="js/jquery-3.6.0.min.js"></script>
        <script src="js/index.js"></script>
    </head>
    <body>
        <h1>Práctica 7: Raspberry Pi (geolocalización)</h1>
        <p><strong>Objetivo: </strong>Ubicar la geolocalización de un dispositivo Raspberry.</p>
        <hr>
        <p style="color: red">* Siguiente actualizacion en (<span id="tiempo">5</span>) segundos</p>
        <p style="color: blue" id="cargando"></p>
        <canvas id="mapa" width="820px" height="550px">
			Tu navegador no soporta CANVAS
		</canvas>
        <br>
        <?php
            include('php/conectorSQL.php');
            $resultado = consultaBD('SELECT * FROM mapa');
            echo "<script>dibujarEdificio(".$resultado[0]['latitud'].", ".$resultado[0]['longitud'].", ".$resultado[1]['latitud'].", ".$resultado[1]['longitud'].", ".$resultado[2]['latitud'].", ".$resultado[2]['longitud'].", ".$resultado[3]['latitud'].", ".$resultado[3]['longitud'].");</script>";
        ?>
    </body>
</html>