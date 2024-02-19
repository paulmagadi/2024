const updateButtons = document.getElementsByClassName('add-cart');


for(let i = 0; i < updateButtons.length; i++) {
    updateButtons[i].addEventListener('click', function(){
        let productId = this.dataset.product
        let action = this.dataset.action

        console.log('USER:', user)
        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log('user is logged in, sending data...')

    let url = '/update_cart/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })
    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
}