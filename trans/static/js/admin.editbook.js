g_val = undefined;
function checkSlugUnique(event)
{
	/*$.ajax()*/
	var _this = this;
	if(g_val === undefined){
		g_val = this.val();
	}
	if(g_val == this.val()){
		var help = this.siblings(".help-inline");
		var group = this.parents('.control-group');
		help[0].innerText = 'keep the same';
		group.attr('class', 'control-group success');
		return;
	}

	data = {slug: this.val()}
	$.getJSON('/admin/check/book_slug_unique/', data, function(data){
		var help = _this.siblings(".help-inline");
		var group = _this.parents('.control-group');
		if(data.ret == false){
			help[0].innerText = 'not unique';
			group.attr('class', 'control-group error');
		}else{
			help[0].innerText = 'valid';
			group.attr('class', 'control-group success');
		}
	} );
	
}
$("#id_name").bind("blur", $.proxy(checkSlugUnique, $("#id_slug")));
$("#id_slug").bind("blur", $.proxy(checkSlugUnique, $("#id_slug")));

$("#id_name").bind("keyup",function(){
	$("#id_name").slugify($("#id_slug"));
});