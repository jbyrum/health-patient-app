$(document).ready(function() {
	$.each($('td'), function () {
	  var text = $(this).html();
	  if(text == 'low') {
	    $(this).css('background-color', 'green');
	  } else if (text == 'medium') {
		$(this).css('background-color', 'yellow');
	  } else if (text == 'high') {
	  	$(this).css('background-color', 'red');
	  }
	});
});