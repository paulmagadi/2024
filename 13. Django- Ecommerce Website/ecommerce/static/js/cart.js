$(document).ready(function() {
    $(document).on('click', '.add-cart', function(e){
        e.preventDefault();
        var product_id = $(this).val(); 
        var product_qty;
        if ($('.quantity input').length) {
            
            product_qty = $('.quantity input').val();
        } else {
            product_qty = 1;
        }

        $.ajax({
            type: 'POST',
            url : cartAddUrl,
            data: {
                product_id : product_id,
                product_qty: product_qty,
                csrfmiddlewaretoken: csrfToken,
                action: 'post'
            },

            success: function(json){
                $('.cart-quantity').text(json.qty);
            },

            error: function(xhr, errmsg, err){
                // Handle error
            }
        });
    });
});
