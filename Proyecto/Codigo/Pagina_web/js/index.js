let graficas = {
    llenarCapacidad: function (clientes, faltantes) {
        google.charts.load("current", {packages:["corechart"]});
        google.charts.setOnLoadCallback(drawChart);
        function drawChart() {
            var data = google.visualization.arrayToDataTable([
                ['Task', 'Capacidad'],
                ['Personas dentro', clientes],
                ['Lugares Disponibles', faltantes]
            ]);
            var options = {
                title: 'Capacidad del Negocio',
                pieHole: 0.4,
            };

            var chart = new google.visualization.PieChart(document.getElementById('capacidadLocal'));
            chart.draw(data, options);
        }
    },
    llenarTermometro: function (temperatura) {  
        $('#temperaturaPromedio').html(`
            ${temperatura}<sup>°C</sup>
        `);
    },
    historialDias: function (historial) { 
        google.charts.load('current', {'packages':['corechart']});
        google.charts.setOnLoadCallback(drawChart);
            function drawChart() {

                let datos = [
                    ['Día', 'Clientes']
                ];
                historial.forEach(dia => {
                    datos.push([
                        dia.fecha, 
                        parseInt(dia.numero)
                    ]);
                });
                console.log(datos);
                var data = google.visualization.arrayToDataTable(datos);
                
                var options = {
                    title: 'Historial de clientes por dia',
                    curveType: 'function',
                    legend: { position: 'bottom' },
                    series: {
                        0: { color: '#D00A0A' },
                    }
                };

                var chart = new google.visualization.LineChart(document.getElementById('historialClientes'));
                chart.draw(data, options);
            }
    }
};  

let getDatos = function () {
    console.log('Peticion de datos');
    $('#cargar').removeClass('d-none');
    $('#graficas').addClass('d-none');
    $.ajax({
        type: "get",
        url: "getDatos.php",
        data: {},
        dataType: "json",
        success: function (response) {
            let capacidadMaxima = 200;
            graficas.llenarCapacidad(parseInt(response.numeroClientes), capacidadMaxima-response.numeroClientes);
            graficas.llenarTermometro(parseFloat(response.temperaturaPromedio).toFixed(2));
            graficas.historialDias(response.historial);
            $('#graficas').removeClass('d-none');
            $('#cargar').addClass('d-none');
        }
    });
}
$(document).ready(function () {
    getDatos();
    setInterval(() => {
        getDatos();
    }, 60000);
});