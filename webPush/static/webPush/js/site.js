const pushForm = document.getElementById('send_push_form');
const errorMsg = document.querySelector('.error');

pushForm.addEventListener('submit', async function (e) {
    e.preventDefault();
    const input = this[0];
    const textarea = this[1];
    const button = this[2];
    errorMsg.innerText = '';

    const head = $('#push_head').val();
    const body = $('#push_body').val();
    const meta = document.querySelector('meta[name="user_id"]');
    const id = meta ? meta.content : null;

    if (head && body && id) {
        button.innerText = 'Sending...';
        button.disabled = true;
        $.ajax({
            type:'POST',
            url:"send_push",
            data: {'push_head':head,'push_body':body,'id':id},
            success:function(res){
                if (res.status === 200) {
                    button.innerText = 'Send another 😃!';
                    button.disabled = false;
                    input.value = '';
                    textarea.value = '';
                } else {
                    errorMsg.innerText = res.message;
                    button.innerText = 'Something broke 😢..  Try again?';
                    button.disabled = false;
                }
            },
            error:function(res){
                alert("Something went wrong. Try again !! : ",res)
            }
        });    
    }
    else {
        let error;
        if (!head || !body){
            error = 'Please ensure you complete the form 🙏🏾'
        }
        else if (!id){
            error = "Are you sure you're logged in? 🤔. Make sure! 👍🏼"
        }
        errorMsg.innerText = error;
    }
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});