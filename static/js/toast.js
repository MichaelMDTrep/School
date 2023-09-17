$('.toast').show();

$('.btn-close').click(function() {
    $(this).closest('.toast').hide();
});