function checkSlugUnique(event)
{
	/*$.ajax()*/
	console.log('check: ' + $("#id_slug").val());
	data = {slug: $("#id_slug").val()}
	$.getJSON('/admin/check/book_slug_unique/', data, function(data){
		var help = $("#id_slug").siblings(".help-inline");
		var group = $("#id_slug").parents('.control-group');
		if(data.ret == false){
			help[0].innerText = 'not unique';
			group.attr('class', 'control-group error');
		}else{
			help[0].innerText = 'valid';
			group.attr('class', 'control-group success');
		}
	} );
	
}
$("#id_name").bind("blur", checkSlugUnique);
$("#id_slug").bind("blur", checkSlugUnique);

$("#id_name").bind("keyup",function(){
	$("#id_name").slugify($("#id_slug"));
});