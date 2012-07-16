/*$(function() {
		$( "#sortable" ).sortable({
			placeholder: "ui-state-highlight"
		});
		$( "#sortable" ).disableSelection();
	});*/
function dialog(msg){
	//$( "#dialog:ui-dialog" ).dialog( "destroy" );
		$( '<div title="test title"><p>'+msg+'</p></div>' ).dialog({
			modal: true,
			buttons: {
				Ok: function() {
					$( this ).dialog( "close" );
				}
			}
		});
}
function tooltip(msg){
	var tip = $('<div class="quick-alert">'+msg+'</div>')
        .css({
        "position": "fixed",
        "right": "0px",
        "top": "100px",
        "padding": "0.5em",
        "background": "#FFA",
        "border": "1px solid #A00",
        "color": "#A00",
        "font-weight": "bold",
        })
    tip.insertAfter( $("body") )
		.fadeIn('slow', function(){
			setTimeout( function() {
				tip.fadeOut('slow', function() {
					$(this).remove();
				});
			}, 500);
		});
	//.animate({opacity: 1.0}, 3000);

	//$('<div>'+msg+'</div>').fadeIn('slow');
}
function del_paragraph(that, para_id){
	var _item = $(that).closest('.portlet');
	$.ajax({
		url: "/manage/ajax/del_paragraph/"+para_id+"/",
		dataType: 'json',
		async: false,
		success: function(data) {
			tooltip('success');
			_item.fadeOut('slow', function() {
				$(this).remove();
			});
		},
		error: function(data){
			tooltip('error');
		}
	});
}

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
				//console.dir(ui);
				//console.log('start: '+ui.item.data('start_pos')+' to: ' + ui.item.index());
				
			},
			stop: function (event, ui) {
				
			}
		});

		$( ".para-content" ).addClass( "ui-widget ui-widget-content ui-helper-clearfix ui-corner-all" );

/*		$( ".portlet-header .ui-icon" ).click(function() {
			$( this ).toggleClass( "ui-icon-minusthick" ).toggleClass( "ui-icon-plusthick" );
			$( this ).parents( ".portlet:first" ).find( ".portlet-content" ).toggle();
		});*/
		$(".para-content").bind("mouseover", function(obj){
			$('.para-opt').css('visibility','hidden');
			$(this).siblings(".para-opt:first").css('visibility','visible');
		})
		$( ".column" ).disableSelection();
		//$("a[name='para_del']").bind('click', function(obj){
	});
