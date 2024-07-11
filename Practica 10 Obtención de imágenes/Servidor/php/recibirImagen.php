<?php
    include('conexionSQL.php');
    if (querySQL("INSERT INTO fotos (url) values ('".$_REQUEST['urlImagen']."')")) {
        echo 'Registro exito en el servidor';
    }