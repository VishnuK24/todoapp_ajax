$(document).ready(function(){

    var csrfToken = $("input[name=csrfmiddlewaretoken]").val()

    $("#createButton").click(function(){
        var data = $("#idCreate").serialize();
        $.ajax({
            url: '/todo/todo-list',
            data: data,
            type: 'post',
            success: function(response) {
                $("#todoTaskList").append('<div class="card mb-1" id="taskCard" data-id="'+ response.task.id + '"><div class="card-body">' 
                + response.task.title + 
                '<button type="button" class="close float-right" data-id="'+ response.task.id + '"><span aria-hidden="true">&times;</span></button></div></div>')
            }
        });
        $("#idCreate")[0].reset();
    });

    $("#todoTaskList").on('click', '.card', function() {
        var dataId = $(this).data('id');

        $.ajax({
            url: '/todo/' + dataId + '/completed/',
            data: {
                csrfmiddlewaretoken: csrfToken,
                id: dataId
            },
            type: 'post',
            success: function() {
                var cardItem = $("#taskCard[data-id='" + dataId + "']");
                cardItem.css('text-decoration', 'line-through').hide().slideDown();
                $("#todoTaskList").append(cardItem);
            }
        });
    }).on('click', 'button.close', function(event) {
        event.stopPropagation();

        var dataId = $(this).data('id');

        $.ajax({
            url: '/todo/' + dataId + '/deleted/',
            data: {
                csrfmiddlewaretoken: csrfToken,
                id: dataId
            },
            type: 'post',
            dataType: 'json',
            success: function() {
                $("#taskCard[data-id='" + dataId + "']").remove();
            }
        })

    });
});