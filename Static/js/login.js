window.onload=function(){
	main()
}
function main(){
'use strict';

	$('#loginButton').click(function(){
		
		var email = $('#loginEmail').val();
		var pwd = $('#loginPwd').val();
		
		$.ajax({
			
			url : '/loginCredentials',
			data : {'email':email, 'pwd':pwd},
			type : 'GET',
			success : function(data){
				

				if(data['status']==0){
					alert("user doesnot exists! please signup");
					
				}
				else{
					alert("user exists");
				}	
			},
			error : function(error){
			
				alert(error);
			},
		})
	})

}
