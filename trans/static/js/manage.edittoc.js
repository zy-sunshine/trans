/*$(function() {
		$( "#sortable" ).sortable({
			placeholder: "ui-state-highlight"
		});
		$( "#sortable" ).disableSelection();
	});*/



$(function() {
		$( ".column" ).sortable({
			connectWith: ".column",
			cancel: 'button',
			opacity: 0.6,
			tolerance: 'intersect',
			//revert: true,
/*			start: function(event, ui) { 
				console.log('start event: ' + event);
			},
			update: function(event, ui) { 
				console.log('update event: ' + event);
			},
			change: function(event, ui) { 
				console.log('change event: ' + event);
			},
			stop: function(event, ui) { 
				console.log('stop event: ' + event);
			},*/
			start: function(event, ui) {
	            var start_pos = ui.item.index();
	            ui.item.data('start_pos', start_pos);
        	},
			update: function(event, ui) { 
				console.dir(ui);
				console.log('start: '+ui.item.data('start_pos')+' to: ' + ui.item.index());
				
			},
			stop: function (event, ui) {
				
			}
		});

		$( ".para-content" ).addClass( "ui-widget ui-widget-content ui-helper-clearfix ui-corner-all" );

/*		$( ".portlet-header .ui-icon" ).click(function() {
			$( this ).toggleClass( "ui-icon-minusthick" ).toggleClass( "ui-icon-plusthick" );
			$( this ).parents( ".portlet:first" ).find( ".portlet-content" ).toggle();
		});*/
		$(".para-content").bind("mouseover", function(event){
			$('.para-opt').css('visibility','hidden');
			$(this).siblings(".para-opt:first").css('visibility','visible');
		})
		$( ".column" ).disableSelection();
	});
