$(function () {
    $("audio").on("ended", function () {
        $("#shuffle").click();
    });

    $("#folder").click(() => {
        var promesaJQuery = $.get("/folder");

        promesaJQuery.done(function (json) {
            console.log(json.respuesta);
        });

        promesaJQuery.fail(function (respuesta) {
            alert("¡Error en promesaJQuery!");
            console.log(respuesta);
        });
    });
});
