function dialog(title, msg){
	//$( "#dialog:ui-dialog" ).dialog( "destroy" );
		$( '<div title="'+ title +'"><p>'+msg+'</p></div>' ).dialog({
			modal: true,
			buttons: {
				Ok: function() {
					$( this ).dialog( "close" );
				}
			}
		});
}
function tooltip(msg, notfade){
	var tip = $('<div class="tip">'+msg+'</div>')
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
			if(!notfade){
				setTimeout( function() {
					tip.fadeOut('slow', function() {
						$(this).remove();
					});
				}, 500);
			}
		});
	//.animate({opacity: 1.0}, 3000);
	if(notfade)
		return tip[0];
	//$('<div>'+msg+'</div>').fadeIn('slow');
}
function tooltip_fadeout(obj, time)
{
	time = time || 0;
	setTimeout( function() {
		$(obj).fadeOut('slow', function() {
			$(this).remove();
		});
	}, time);
}
function html_table_from_dict(dict)
{
	table_str = '<div title="">'
	table_str += '<table class="table table-bordered table-striped"><tbody>';
	table_str += '<tr><th>Key</th><th>value</th></tr>'
	_.each(dict, function(value, key){
		table_str += '<tr><td>'+key+'</td><td>'+value+'</td></tr>';
	});
	table_str += '</tbody></table></div>';
	return table_str;
}