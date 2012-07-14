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
		console.log(this.href);
		slug = get_slug(this.href);
		data = {'slug': slug}
		table_str = '<table class="table"><tbody>';
		table_str += '<tr><th></th><th><a class="btn" href="/admin/addtoc/book/'+slug+'/">Add Toc</a></th></tr>'
		$.ajax({
  			url: '/admin/ajax/get_toclist/',
  			dataType: 'json',
  			async: false,
  			data: data,
  			success: function(data) {
    			_.each(data, function(e){
					table_str += '<tr><td>'+e.name+'</td><td>'+e.slug+'</td></tr>';
				});
  			}
		});
		/*$.getJSON('/admin/ajax/get_toclist/',data, function(data){
			_.each(data, function(e){
				table_str += '<tr><td>'+e.name+'</td><td>'+e.slug+'</td></tr>';
			});
		});*/
		//table_str += '<tr><td>c1</td><td>c2</td></tr>';
		table_str += '</tbody></table>';
		g_elem = $(table_str);
		g_elem_btn = this;
		g_elem.insertAfter(this);
	}
});