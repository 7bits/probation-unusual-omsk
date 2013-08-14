$(document).ready(function() {
    $('#subscription-form').submit(function(e) {
        e.preventDefault();
        $.ajax({
            url: "/subscribe/",
            type: "POST",
            dataType: "json",
            data: $(this).serialize(), 
            success: function(data) {
                // Удаляем ошибки если были
                //$form.find('.error').remove();
                if (data['result'] == 'success') {
                    // Делаем что-то полезное
                    $(id_email).val("");
                    alert("Спасибо за подписку!");
                }
                else if (data['result'] == 'error') {
                    // Показываем ошибки
                    //$form.replaceWith(data['response']);
                    alert("не правильный e-mail!");
                }
            },
        });
    });
});
