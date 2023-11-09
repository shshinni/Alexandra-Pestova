window.addEventListener("DOMContentLoaded", function () {
    document.getElementById('application-form').addEventListener('submit', function (event) {
        event.preventDefault();

        let form = event.target;
        let formData = new FormData(form);

        let url = form.action;

        fetch(url, {
            method: 'POST',
            body: formData
        })
            .then(function (response) {
                if (response.ok) {
                    return response.text();
                } else {
                    throw new Error('Ошибка при отправке формы.');
                }
            })
            .then(function (data) {
                alert('Заявка с номером '+ formData.get('phone') +' отправлена!');
                form.reset();
            })
            .catch(function (error) {
                console.error(error);
                alert(error);
            });
    });
});
