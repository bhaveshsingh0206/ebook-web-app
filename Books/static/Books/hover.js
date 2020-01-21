$('.hover').mousemove(function(e) {
	var hovertext = $(this).attr('hovertext');

	$('#hoverdiv').text(hovertext).show();
	$('#hoverdiv').css('top', e.clientY+10).css('left', e.clientX+10);
}).mouseout(function() {
	$('#hoverdiv').hide();

});