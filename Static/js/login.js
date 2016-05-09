window.onload=function(){
	main()
}
function main(){
'use strict';
	
	var count = 0;
	var totalLen = 0;
	$('input[type="radio"]').click(function(){
		var element = $(this)
		var qid = $(element).attr("name")
		var ansid = $(this).val()
		
		$.ajax({
			url: "/submitAnswer",
			type: "GET",
			data: {
				"qid": qid,
				"ansid": ansid
			}, 
			success: function(data){
				console.log(data)
				count += data['status'];
				totalLen = data['length'];
			} 
		})
	})

	$("#submitTest").click(function(){
		alert("Your result is : " + count + " / " + totalLen);
	})
	// var d= document.getElementById("dialogBox");
	// console.log(d);
	// if(d.innerText === '')
	// 	d.style.display = 'none'
	// validateOption()
}
