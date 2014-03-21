window.onload=onLoad;

function onLoad() {
    $(".btn-guess-year").click(checkForCorrectYear);
}

function checkForCorrectYear() {
    var year = $(this).text();
    $.ajax({
        url: "/carquizgame/check_year/",
        data: 'date=' + carOfDayDate + '&guess=' + year,
        crossDomain: true,
    }).done(
        function(data) {
            if(data.success)
            {
                $('#correctModal').modal();
            }
            else
            {
                $('#incorrectModal').modal();
            }
        }
    );
}
