<?php
    function consultaBD($query) {
        $conexion = mysqli_connect("localhost", "root", "", "localizacion", 3307);
        if (mysqli_connect_errno()) {
            echo "Error al conectarse a MySQL: " . mysqli_connect_error();
        }
        $resultado = mysqli_query($conexion, $query);
        mysqli_close($conexion);
        
        $arreglo = [];
        do {
            $renglon = mysqli_fetch_array($resultado,MYSQLI_ASSOC);
            if ($renglon != null) {
                $arreglo[] = $renglon;
            }
        } while ($renglon != null);

        return $arreglo;
    }
?>