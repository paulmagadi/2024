$(document).ready(function() {
    $(document).on('click', '.add-cart', function(e){
        e.preventDefault();
        var product_id = $(this).val(); // Retrieve product ID from the button's value attribute
        var product_qty;

        // Check if the quantity input field exists
        if ($('.quantity input').length) {
            // If quantity input exists, use its value
            product_qty = $('.quantity input').val();
        } else {
            // Otherwise, default quantity to one
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
