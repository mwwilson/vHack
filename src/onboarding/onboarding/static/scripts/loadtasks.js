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
    dictionary = dictionary['response'];

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
    if(Object.keys(dictionary).indexOf(task) != -1)
	{
	    var card = document.createElement("task-card")
	    card.setAttribute("id", task)
	    card.setAttribute("task_description", allTasks[task]['description'])
	    card.setAttribute("task_link", allTasks[task]['link'])
	    card.setAttribute("task_name", task)
	    
	    if(dictionary[task] == 'complete'){
		//card.goLink()
		
	    }

	    document.getElementById("tasklist").appendChild(card)

	   
	}
    processData(count + 1)
     
}

$(document).ready(function(){ 
    loadCards()
})
