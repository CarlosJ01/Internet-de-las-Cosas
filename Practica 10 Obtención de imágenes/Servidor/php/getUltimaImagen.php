<?php
    include('conexionSQL.php');
    $foto = selectSQL('SELECT * FROM fotos WHERE mostrado = 0 LIMIT 1');
    if (count($foto) == 1) {
        if (querySQL("UPDATE fotos SET mostrado = 1 WHERE id = ".$foto[0]['id'])) {
            echo json_encode(['success' => $foto[0]]);
        } else {
            echo json_encode(['error' => 'No puede actualizar la imagen']);
        }
    } else {
        echo json_encode(['error' => 'Sin imagenes disponibles']);
    }