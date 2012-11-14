  $(document).ready(function() {
  $("input:submit").click(function (event) {
	$(event.target).addClass("hidden");
	var form = event.target.parentNode;
	var msg = document.createElement();   
	$(msg).addClass("process");
	msg.innerHTML = "&nbsp;&nbsp;&nbsp;Trwa archiwizacja...";
	form.insertBefore(msg, event.target.nextSibling);
  });         
});
