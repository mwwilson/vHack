function submit_app(){
    
    $.ajax({
        url: "../submit/Training",
	dataType: 'json',
	success: function(data){
	    alert("Successfully submitted!")
	    window.location.href = "http://0.0.0.0:6543/";
        },
    });
    
}

$(document).ready(function(){ 
    document.getElementById("training_submit").onclick = submit_app
})
