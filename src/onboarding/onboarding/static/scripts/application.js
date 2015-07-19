function submit_app(){
    
    $.ajax({
        url: "../submit/Application",
	dataType: 'json',
	success: function(data){
	    alert("Successfully submitted!")
	    window.location.href = "http://0.0.0.0:6543/";
        },
    });
    
}

$(document).ready(function(){ 
    document.getElementById("application_submit").onclick = submit_app
})
