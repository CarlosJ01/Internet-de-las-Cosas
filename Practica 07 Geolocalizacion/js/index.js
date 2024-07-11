let tiempo = 6;

function convertirCordenadasPixeles(lat, lon) {
    latitud_superior = 19.723673;
    longitud_superior = -101.185338;

    x = (((longitud_superior - lon)*820)/-0.000544);
    y = (((latitud_superior - lat)*550)/0.000352);
    
    return [x,y];
}

function dibujarPunto(ctx, punto, color = "red"){
    ctx.lineWidth = 5;
    ctx.strokeStyle = color;
    ctx.fillStyle = color;

    ctx.beginPath();
    ctx.arc(punto[0], punto[1], 3, 0, 2*Math.PI,true);
    ctx.stroke();
}

function dibujarCuadrado(ctx, punto1, punto2, punto3, punto4, color = "red") {
    ctx.lineWidth = 3;
    ctx.strokeStyle = color;
    ctx.fillStyle = color;
    
    ctx.beginPath();
    ctx.moveTo(punto1[0], punto1[1]);
    ctx.lineTo(punto2[0], punto2[1]);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(punto2[0], punto2[1]);
    ctx.lineTo(punto4[0], punto4[1]);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(punto4[0], punto4[1]);
    ctx.lineTo(punto3[0], punto3[1]);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(punto3[0], punto3[1]);
    ctx.lineTo(punto1[0], punto1[1]);
    ctx.stroke();
}

function dibujarEdificio(lat1, lon1, lat2, lon2, lat3, lon3, lat4, lon4) {
    var canvas=document.getElementById('mapa');
    if(canvas&&canvas.getContext){
        var ctx=canvas.getContext("2d");
		if (ctx) {
            /* Conversion de cordenadas */
            lat1=parseFloat(lat1);
            lon1=parseFloat(lon1);
            lat2=parseFloat(lat2);
            lon2=parseFloat(lon2);
            lat3=parseFloat(lat3);
            lon3=parseFloat(lon3);
            lat4=parseFloat(lat4);
            lon4=parseFloat(lon4);

            document.write("Puntos del mapa: ");
            /* Edificio */
            ctx.font = "3em Verdana";
            ctx.lineWidth = 1.0;
            ctx.fillStyle = "white";
            ctx.strokeStyle = "white";
            ctx.shadowColor = "black";
            ctx.shadowOffsetX = 5;
            ctx.shadowOffsetY = 5;
            ctx.shadowBlur = 10;
            ctx.fillText("Edificio CH",35,50);
            ctx.strokeText("Edificio CH",35,50);

            /* Punto 1 */
            punto1 = convertirCordenadasPixeles(lat1, lon1);
            document.write("<br/>   1) Latitud: "+lat1+", Longitud: "+lon1+" (X: "+punto1[0]+",Y: "+punto1[1]+")");
            dibujarPunto(ctx, punto1);

            /* Punto 2 */
            punto2 = convertirCordenadasPixeles(lat2, lon2);
            document.write("<br/>   2) Latitud: "+lat2+", Longitud: "+lon2+" (X: "+punto2[0]+",Y: "+punto2[1]+")");
            dibujarPunto(ctx, punto2);

            /* Punto 3 */
            punto3 = convertirCordenadasPixeles(lat3, lon3);
            document.write("<br/>   3) Latitud: "+lat3+", Longitud: "+lon3+" (X: "+punto3[0]+",Y: "+punto3[1]+")");
            dibujarPunto(ctx, punto3);

            /* Punto 4 */
            punto4 = convertirCordenadasPixeles(lat4, lon4);
            document.write("<br/>   4) Latitud: "+lat4+", Longitud: "+lon4+" (X: "+punto4[0]+",Y: "+punto4[1]+")");
            dibujarPunto(ctx, punto4);
            
            dibujarCuadrado(ctx, punto1, punto2, punto3, punto4);

            /* Raspberry */
            /* lat = 19.723431;
            lon = -101.184948;
            

            document.getElementById("cargando").innerHTML = " <hr>";
            document.getElementById("cargando").innerHTML = " <hr>"; */

        } else {
            alert("Error Canvas no soportado");
        }
    }
}

$(document).ready(function () {
    /* Cargando */
    $('#cargando').html("<strong>CARGANDO CORDENADAS DE LA RASPBERRY</strong>");
    var ctx=document.getElementById('mapa').getContext("2d");
    /* Peticion */
    $.ajax({
        type: "GET",
        url: "php/ultimaLocalizacion.php",
        data: {},
        dataType: "json",
        success: function (response) {
            /* Mostrar en el mapa */
            console.log(response);
            lat=parseFloat(response.Latitud);
            lon=parseFloat(response.Longitud);
            puntoRB = convertirCordenadasPixeles(lat, lon);
            dibujarPunto(ctx, puntoRB, 'yellow');
            $('#cargando').html("<strong>Raspberry => Latitud: "+lat+", Longitud: "+lon+" (X: "+x+",Y: "+y+")</strong>");
            setTimeout(function(){ dibujarPunto(ctx, puntoRB, 'black'); }, 5500);
        }
    });

    /* Peticion cada 6 segundos */
    window.setInterval(function () {  
        /* Cargando */
        $('#cargando').html("<strong>CARGANDO CORDENADAS DE LA RASPBERRY</strong>");
        var ctx=document.getElementById('mapa').getContext("2d");
        /* Peticion */
        $.ajax({
            type: "GET",
            url: "php/ultimaLocalizacion.php",
            data: {},
            dataType: "json",
            success: function (response) {
                /* Mostrar en el mapa */
                console.log(response);
                lat=parseFloat(response.Latitud);
                lon=parseFloat(response.Longitud);
                puntoRB = convertirCordenadasPixeles(lat, lon);
                dibujarPunto(ctx, puntoRB, 'yellow');
                $('#cargando').html("<strong>Raspberry => Latitud: "+lat+", Longitud: "+lon+" (X: "+x+",Y: "+y+")</strong>");
                setTimeout(function(){ dibujarPunto(ctx, puntoRB, 'black'); }, 5500);
            } 
        });
    }, 6000);

    /* Cuenta regresiva para el contador */
    window.setInterval(function () {
        tiempo -= 1;
        $('#tiempo').text(tiempo);  
        if (tiempo == 0)
            tiempo = 6;
    }, 1000);
});