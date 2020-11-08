$(function (){

    let createForm = function(action){
        let newForm = document.createElement('form');
        newForm.action = action
        newForm.method = 'post';
        var csrfInput = document.createElement('input');
        csrfInput.name = 'csrfmiddlewaretoken';
        csrfInput.value = $("[name='csrfmiddlewaretoken']").val();
        newForm.appendChild(csrfInput);
        newForm.style.display = 'none';
        document.body.append(newForm);
        newForm.submit();
        return newForm;
    }

    $(".remote-card").click(function (){
        let contentId = $(this).attr('content-id')
        let action = `/del_evaluation_content/${contentId}/`
        createForm(action)
    })

    $(".del-section").click(function (){
        let sectionId = $(this).attr('section-id')
        let action = `/del_section/${sectionId}/`
        createForm(action)
    })
})