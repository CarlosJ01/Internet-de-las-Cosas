let actions = {
    /* Optener ultima imagen */
    getImagen: function () {  
        $.ajax({
            type: "GET",
            url: "php/getUltimaImagen.php",
            data: {},
            dataType: "json",
            success: function (json) {
                console.log(json);
                if (json.success) {
                    $('#imagen').attr('src', json.success.url);
                    $('#mensaje').text('');
                } else {
                    $('#imagen').attr('src', "");
                    $('#mensaje').text(json.error);
                }
            }
        });
    }
}
$(document).ready(function () {
    actions.getImagen();
    /* Recarga cada 2 segundos */
    setInterval(() => {
        actions.getImagen();
    }, 2000);
});