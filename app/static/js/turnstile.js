function javascriptCallback(token) {
    fetch('/challenge', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'turnstile-response': token })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // The captcha was valid, continue processing the form
            
        } else {
            // The captcha was invalid, show an error message
        }
    });
}