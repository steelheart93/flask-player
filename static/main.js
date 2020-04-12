$(function () {
    $("audio").on("ended", function () {
        $("#shuffle").click();
    });
});
