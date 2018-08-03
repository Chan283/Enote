$(document).ready(function(){
	$(".shrbtn").hover(function(){
		$(this).css("filter","invert(100%)");
	},function(){
		$(this).css("filter", "invert(0%)");
	});

});

