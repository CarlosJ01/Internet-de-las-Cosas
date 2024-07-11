<?php
    /* Extraer los datos */
    extract($_REQUEST, EXTR_PREFIX_ALL|EXTR_REFS, 'request');

    /* Guardar en la Base de Datos */
    try {
        $pdo = new PDO(
            "mysql:dbname=datos_servidor;host=localhost;port=3307",
            "root",
            "",
            array(PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8")
        );
    } catch (PDOException $e) {
        echo "Error en el servidor";
    }

    $query = $pdo->prepare("INSERT INTO clima (id_sensor, certificado, latitud, longitud, utc, fecha, hora, variable, valor)
                                VALUES (:id_sensor, :certificado, :latitud, :longitud, :utc, :fecha, :hora, :variable, :valor)");
    
    $query->bindParam(':id_sensor', $request_id_sensor);
    $query->bindParam(':certificado', $request_certificado);
    $query->bindParam(':latitud', $request_latitud);
    $query->bindParam(':longitud', $request_longitud);
    $query->bindParam(':utc', $request_utc);
    $query->bindParam(':fecha', $request_fecha);
    $query->bindParam(':hora', $request_hora);
    $query->bindParam(':variable', $request_variable);
    $query->bindParam(':valor', $request_valor);
    $query->execute();
    
    /* Mensaje devuelta */
    if($query){
        echo 'Guardado en la nube satisfactorio';
    }
    else{
        echo "Error al subir a la BD del Servidor";
    }
?>