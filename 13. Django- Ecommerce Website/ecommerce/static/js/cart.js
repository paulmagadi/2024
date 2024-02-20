
addCart = document.getElementsByClassName('add-cart')

$(document).on('click', 'addCart', function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url : '{% url "cart_add" %}',
        data: {
            product_id : $('addCart').val(),
            csrfmiddlewaretoken: '{{ csrf_token }}',
            action: 'post'
        },

        success: function(json){
            document.getElementsByClassName('cart-quantity').textcontent = json.qty
        },

        error: function(xhr, errmsg, err){
            
        }

    });
})