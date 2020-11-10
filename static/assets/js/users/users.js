$('a#desativar').click(function(e){
    e.preventDefault();
    var user = $(this).attr("alt");
    var link = $(this).attr("href");
	swal.fire({
  	    title: 'Tem certeza que deseja desativar o(a) usuário(a) ' + user,
  	    text: "Você pode reverter isso no menu de usuários inativos.",
  	    type: 'warning',
  	    showCancelButton: true,
  	    confirmButtonText: 'Sim',
  	    cancelButtonText: 'Cancelar',
	}).then((result) => {
  		if (result.value) {
            window.location.href = link;
  	} else if ( result.dismiss === Swal.DismissReason.cancel ) {
            swal.fire(
                'Cancelado',
                '',
                'error'
                                          )
            }})});


$('a#delete').click(function(e){
    e.preventDefault();
    var user = $(this).attr("alt");
    var link = $(this).attr("href");
	swal.fire({
  	    title: 'Tem certeza que deseja excluir o(a) usuário(a) ' + user,
  	    text: "Você não poderá desfazer isso.",
  	    type: 'warning',
  	    showCancelButton: true,
  	    confirmButtonText: 'Sim',
  	    cancelButtonText: 'Cancelar',
	}).then((result) => {
  		if (result.value) {
            window.location.href = link;
  	} else if ( result.dismiss === Swal.DismissReason.cancel ) {
            swal.fire(
                'Cancelado',
                '',
                'error'
                                          )
            }})});




