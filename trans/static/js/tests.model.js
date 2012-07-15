	jQuery( function($) { 
		// find all tr's with a data-href attribute
		$('tbody tr[data-href]').click( function() {
			// copy the data-href value to the modal for later use
			$('#modal-editUser').attr('data-href',$(this).attr('data-href'));
			// show the modal window
			$('#modal-editUser').modal({show: true , backdrop : true , keyboard: true});
		}).find('a').hover( function() { 
			// unbind it in case I put some a tags in the table row eventually
			$(this).parents('tr').unbind('click'); 
		}, function() { 
			$(this).parents('tr').click( function() { 
				// rebind it
				$('#modal-editUser').attr('data-href',$(this).attr('data-href'));
				$('#modal-editUser').modal({show: true , backdrop : true , keyboard: true});
			}); 
		});
		
		// when the modal show event fires, load the url that was copied to the data-href attribute
		$('#modal-editUser').bind('show', function() {
			$(this).load($(this).attr('data-href'));
		});
	});