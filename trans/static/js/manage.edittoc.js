/*$(function() {
		$( "#sortable" ).sortable({
			placeholder: "ui-state-highlight"
		});
		$( "#sortable" ).disableSelection();
	});*/

/*
function del_paragraph(that, para_id){
	var _item = $(that).closest('.portlet');
	$.ajax({
		url: "/manage/ajax/del_para/"+para_id+"/",
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
}*/
var _del_paras = []
function del_paragraph(that, para_id){
	var _item = $(that).closest('.portlet');
	if(_item){
		_item.fadeOut('slow', function() {
				$(this).remove();
		});
		//setTimeout(function(){
			tooltip("success");
		//}, 0);
	}else{
		//setTimeout(function(){
			tooltip("failed");
		//}, 0);
	}
	_del_paras.push(para_id);
}

function edit_paragraph(that, para_id){
	id = "#para_" + para_id;
	var content_elem = $(id).find(".para-content");
	content = content_elem.text();
	$( '<div title="modify Paragraph '+ para_id +'"><textarea rows="7" cols="80" id="m_content" >'+content+'</textarea></div>' ).dialog({
		modal: true,
		buttons: {
			Ok: function() {
				content_elem.text($(this).find("#m_content")[0].value);
				$( this ).dialog( "close" );
			}
		}
	});
}

function info_paragraph(that, para_id){
	$.get('/manage/ajax/info_para/',{'para_id': para_id}, function(data){
		if(data['ret']){
			tab = $(html_table_from_dict(data['data']));
			tab.dialog({
				autoOpen: false,
				modal: true,
				buttons: {
					"Close": function() {
						$( this ).dialog( "close" );
					}
				},
				close: function() {
					
				}
			});
			tab.dialog("open");
		}else{
			dialog('Error', data['msg']);
		}
	}, 'json');
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

		$("#submit_all").bind("click", function(obj){
			var _dict = {'del': _del_paras, 'data': []};
			_.each($(".portlet"), function(elem, idx){
				id = $(elem).find(".label").text();
				content = $(elem).find(".para-content").text();
				_dict['data'].push({"id": id, "idx": idx, "content": content});
			});
			_tip = tooltip("operating...", true);
			$.ajax({
		        url: '/manage/ajax/save_paras/',
		        type: 'POST',
		        contentType: 'application/json; charset=utf-8',
		        data: $.toJSON(_dict),
		        dataType: 'json',
		        success: function(result) {
		        	if(result.ret){
			        	_tip.innerText = 'success';
		        	}else{
		        		_tip.innerText = 'failed';
		        	}
		        	tooltip_fadeout(_tip, 500);
		        },
		        error: function(){
		        	_tip.innerText = 'error';
		        	tooltip_fadeout(this, 500);

		        }
		    });
		});
	});
