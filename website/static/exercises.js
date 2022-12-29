

$("body").on("click", ".delete-config-option-button", function() {
    var count = parseInt( $('.config-option-fields').attr("option-count") );
    $(this).parents(".config-option-row").remove();
    $('.config-option-fields').attr("option-count", count - 1);
})

$(".add-config-option-button").click(function(){
    console.log("party time")
    var count = parseInt( $('.config-option-fields').attr("option-count") );
    newRow =
        '<div class="form-group row config-option-row config-option-field">' +
        '<div class="col">' +
          '<input name="config_types-' + count +
          '" type="text" class="form-control config-type-field" placeholder="Config Type (eg weight)">' +
        '</div>' +
        '<div class="col">' +
          '<input name="config_unit_names-' + count +
          '" type="text" class="form-control config-unit-field" placeholder="Unit Name (eg lbs)">' +
        '</div>' +
        '<div class="col">' +
          '<button type="button" class="btn btn-danger delete-config-option-button">Remove</button>' +
        '</div>' +
      '</div>';
    $('.config-option-fields').append(newRow);
    $('.config-option-fields').attr("option-count", count + 1);
});

function deleteExercise(exerciseId) {
    fetch('/exercises/delete', {
    method: 'POST',
    body: JSON.stringify({ exerciseId: exerciseId })
    }).then((_res) => {
        window.location.href = "/exercises/browse";
    });
}
