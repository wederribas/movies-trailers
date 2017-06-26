// Apply class active in menu link
$(document).ready(function() {
	var path = window.location.pathname;
	if(path == '/')
	{
		$('#home').addClass('active');
	}
	else
	{
		$('#about').addClass('active');
	}
});
