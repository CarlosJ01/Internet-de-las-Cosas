<?php
    include('conectorSQL.php');
    $resultado = consultaBD('SELECT * FROM movimientos ORDER BY FechaYHora DESC LIMIT 1');
    
    echo json_encode($resultado[0]);
?>