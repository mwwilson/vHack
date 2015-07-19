function download_offer(){
            window.location.href = "http://localhost:6543/offer_letter";
}



function submit_app(){

    $.ajax({
        url: "../submit/Offer_Letter",
        dataType: 'json',
        success: function(data){
            alert("Successfully submitted!")
            window.location.href = "http://localhost:6543/";
        },
    });

}

$(document).ready(function(){
    document.getElementById("offer_letter_download").onclick = download_offer;
     document.getElementById("application_submit").onclick = submit_app
})

