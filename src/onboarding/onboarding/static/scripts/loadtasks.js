var dictionary
var allTasks

function loadCards(){
     $.ajax({
        url: "../get_tasks",
	dataType: 'text',
	 cache: false,
	success: function(data){
	    initializeData(data);
        },
    });
}

function initializeData(data1){
    dictionary = JSON.parse(data1);

    $.ajax({
        url: "static/tasks.json",
	dataType: 'text',
	cache: false,
	success: function(data){
	    continueData(data)
        },
    });

 }

function continueData(data){
    allTasks = JSON.parse(data);


    processData(0)
}

function processData(count){
    var task;

    if(count >= Object.keys(allTasks).length){
	return;
    }

    task = Object.keys(allTasks)[count];

    addData(task, count)
    
}

function addData(task, count){
    
    if(Object.keys(dictionary).contains(task))
	{
	    section = document.getElementById("tasklist");
	    html = "<task-card task_name = '" + task + "' task_description='" + 
		dictionary[task]['description'] + "' task_link = '" +
		dictionary[task]['link'] + "'></task-card>"
	    section.innerHTML = section.innerHTML += html
	}
    processData(count + 1)
     
}

$(document).ready(function(){ 
    loadCards()
})
