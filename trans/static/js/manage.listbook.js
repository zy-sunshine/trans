g_elem = undefined;
g_elem_btn = undefined;
$('#id_showtoc').bind('click', function(){
	function get_slug(url){
		slug = url.substr(url.indexOf('#')+1);
		return slug;
	}
	if(g_elem != undefined){
		g_elem.remove();
	}
	if(g_elem_btn == this){
		g_elem_btn = undefined;
	}else{
		_slug = slug = get_slug(this.href);
		data = {'slug': slug}
		table_str = '<div title="Show tocs of '+slug+'">'
		table_str += '<a class="btn" href="/manage/addtoc/book/'+slug+'/">Add Toc</a>'
		table_str += '<table class="table table-bordered table-striped"><tbody>';
		table_str += '<tr><th>Name</th><th>Slug</th><th>Operate</th></tr>'
		$.ajax({
  			url: '/manage/ajax/get_toclist/',
  			dataType: 'json',
  			async: false,
  			data: data,
  			success: function(data) {
  				console.log(data);
    			_.each(data, function(e){
					table_str += '<tr><td>'+e.name+'</td><td>'+e.slug+'</td><td><a class="btn" href="/manage/edittoc/book/'+_slug+'/toc/'+e.slug+'/">Edit</a><a class="btn" href="/manage/deltoc/book/'+_slug+'/toc/'+e.slug+'/">Delete</a></td></tr>';
				});
  			}
		});
		/*$.getJSON('/manage/ajax/get_toclist/',data, function(data){
			_.each(data, function(e){
				table_str += '<tr><td>'+e.name+'</td><td>'+e.slug+'</td></tr>';
			});
		});*/
		//table_str += '<tr><td>c1</td><td>c2</td></tr>';
		table_str += '</tbody></table></div>';
		g_elem = $(table_str);
		g_elem.dialog({
			autoOpen: false,
			// height: 300,
			// width: 350,
			modal: true,
			buttons: {
				"Close": function() {
					$( this ).dialog( "close" );
				}
			},
			close: function() {
				
			}
		});
		//g_elem_btn = this;
		//g_elem.insertAfter($(this).parent());
		console.log(table_str);
		g_elem.dialog("open");
	}
});