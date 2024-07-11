<?php 
    /* Extraer los datos */
    extract($_REQUEST, EXTR_PREFIX_ALL|EXTR_REFS, 'request');

    /* Guardar en la Base de Datos */
    try {
        $pdo = new PDO(
            "mysql:dbname=facemask;host=localhost;port=3307",
            "root",
            "",
            array(PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8")
        );
    } catch (PDOException $e) {
        echo "Error en el servidor";
    }
    /* Comprobar certificado */
    if ($request_certificado == md5('HNos6pfF2M*$')){
        /* Actulizar la BD */
        $query = $pdo->prepare($request_query);
        $query->execute();
        echo 'Actulizado';
    }
?>