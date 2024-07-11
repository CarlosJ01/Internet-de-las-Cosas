<?php
    function querySQL($query) {
        $conexion = mysqli_connect("localhost", "root", "", "camara", 3307);
        if (!$conexion){
            echo "Error con la conexion con mySQL";
            return false;
        }
        mysqli_query ($conexion, $query);
        mysqli_close($conexion);
        return true;
    }

    function selectSQL($query) {
        $conexion = mysqli_connect("localhost", "root", "", "camara", 3307);
        if (!$conexion){
            echo "Error con la conexion con mySQL";
            return [];
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