<?php
    $conexion = mysqli_connect("localhost", "root", "", "facemask", 3307);
    $query = "SELECT COUNT(*) AS numero FROM clientes WHERE LOCAL = 1 AND entrada = '2021-07-03'";
    $result = mysqli_query($conexion, $query);
    mysqli_close($conexion);
    $numeroActual = 0;
    do {
        $renglon = mysqli_fetch_array($result);
        if ($renglon != null) {
            $numeroActual = $renglon['numero'];
        }
    } while ($renglon != null);

    $conexion = mysqli_connect("localhost", "root", "", "facemask", 3307);
    $query = "SELECT AVG(temperatura) AS temperaturaPromedio FROM clientes WHERE LOCAL = 1";
    $result = mysqli_query($conexion, $query);
    mysqli_close($conexion);
    $temperaturaPromedio = 0;
    do {
        $renglon = mysqli_fetch_array($result);
        if ($renglon != null) {
            $temperaturaPromedio = $renglon['temperaturaPromedio'];
        }
    } while ($renglon != null);

    $conexion = mysqli_connect("localhost", "root", "", "facemask", 3307);
    $query = "SELECT COUNT(*) AS numero, entrada AS fecha  FROM clientes WHERE LOCAL = 1 GROUP BY entrada";
    $result = mysqli_query($conexion, $query);
    mysqli_close($conexion);
    $dias=[];
    do {
        $renglon = mysqli_fetch_array($result);
        if ($renglon != null) {
            $dias[] = [
                'fecha' => $renglon['fecha'],
                'numero' => $renglon['numero']
            ];
        }
    } while ($renglon != null);

    $data = [
        'numeroClientes' => $numeroActual,
        'temperaturaPromedio' => $temperaturaPromedio,
        'historial' => $dias
    ];
    
    echo json_encode($data);
?>