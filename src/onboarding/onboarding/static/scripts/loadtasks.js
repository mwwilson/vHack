var dictionary

function loadCards(){
     $.ajax({
        url: "static/tasks.json",
	dataType: 'text',
    cache: false,
	success: function(data){
	    initializeData(data);
        },
    });
}

function initializeData(data){
    dictionary = JSON.parse(data);

    processData(0);
 }

function processData(count){
    var task;

    if(count >= Object.keys(dictionary).length){
	return;
    }

    task = Object.keys(dictionary)[count];

    addData(task, count)
    
}

function addData(task, count){
    section = document.getElementById("tasklist");
    html = "<task-card task_name = '" + task + "' task_description='" + dictionary[task]['description'] + "'></task-card>"
    section.innerHTML = section.innerHTML += html
    
    processData(count + 1)
     
}

$(document).ready(function(){ 
    loadCards()
})
