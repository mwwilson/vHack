function submit_app(){
    
    $.ajax({
        url: "../submit/Germantown",
	dataType: 'json',
	success: function(data){
	    alert("Successfully submitted!")
	    window.location.href = "http://0.0.0.0:6543/";
        },
    });
    
}

$(document).ready(function(){ 
    document.getElementById("germantown_submit").onclick = submit_app
})
