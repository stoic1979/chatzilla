/*
------------------------------------------------------------------------------
    CHAT MANAGER ANGULAR JS SCRIPT
------------------------------------------------------------------------------
*/


//////////////////////////////////////////////////////
//                                                  //
// CREATING AngularJS MODULE & CONTROLLER           //
//                                                  //
//////////////////////////////////////////////////////
var myApp = 
angular
.module("chatModule", [])
.controller("chatController", function($scope, $http, $interval) {	


	$scope.message = "Chatzila Dashboard";

	// some chat objects
	$scope.users = [];
	$scope.messages = [];

        //////////////////////////////////////////////////////
        //                                                  //
        // Function To Get All Logged In Users              //
        //                                                  //
        //////////////////////////////////////////////////////
        $scope.GetAllLoggedInUsers = function () {
             $http.get("/get_logged_users/")
                 .then(function(response){ 
                     $scope.users = response.data; 

                     // if no user is selected, select the first one
                     if(selectedUser == "" && $scope.users.length > 0){
                         selectedUser = $scope.users[0].username;
                         console.log("selected user: " + selectedUser);
                     }
                 });
        };

        //////////////////////////////////////////////////////
        //                                                  //
        // Function To Get All Messages For This User       //
        //                                                  //
        //////////////////////////////////////////////////////
        $scope.GetAllMessages = function () {
            $http({
                method: 'POST',
                url: '/get_user_messages/',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                transformRequest: function(obj) {
                    var str = [];
                    for(var p in obj)
                        str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
                    return str.join("&");
                },
                data: {username: $scope.myUsername, last_msg_id: lastMsgId}
            }).success(function (response) {
                $scope.messages = response; 
                $scope.processMessages($scope.messages);
            });
        };

        //////////////////////////////////////////////////////
        //                                                  //
        // Function Processes All Incoming Messages         //
        //                                                  //
        //////////////////////////////////////////////////////
        $scope.processMessages = function(messages){
            for(var i=0; i<messages.length; i++) {
                var m = messages[i];
                lastMsgId = m.id;
                console.log(m.snd + ": " + m.content);
                console.log("Me: " + $scope.myUsername);
                if(selectedUser == ""){
                    selectedUser = m.snd;
                }
                if(selectedUser == m.snd || selectedUser == m.rcv) {
                    createMessageGUI(m.snd, m.created_at, m.content);			
                }
                var message = m.content;
                var ts = m.created_at;

                var msg = new MessageData(selectedUser, ts, message);
                if(selectedUser in usersMessages) {
                    var msgLst = usersMessages[selectedUser];
                    msgLst.push(msg);		
                } else { // first time
                    var msgLst = [];
                    msgLst.push(msg);
                    usersMessages[selectedUser] = msgLst;
                }
                console.log("lastMsgId: " + lastMsgId);
            }
        };

        //////////////////////////////////////////////////////
        //                                                  //
        // Initialization Function For Passing Data         //
        // Via ng-init From Template                        //
        //                                                  //
        //////////////////////////////////////////////////////
        $scope.init = function (username, id) {
            $scope.myUsername = username;
            $scope.myUserId = id;
            console.log("You are logged in as: " + $scope.myUsername + " with id=" + id);
        };

        //////////////////////////////////////////////////////
        //                                                  //
        // Focus And Select The Current Clicked User        //
        //                                                  //
        //////////////////////////////////////////////////////
        $scope.focusUser = function(username){

            console.log("focusUser: " + username);

            selectedUser = username;

            // clear all messages from right side
            $("#usersMessList tr").remove();

            // show messages for selected user on right side
            var msgLst = usersMessages[selectedUser];
            if (! (selectedUser in usersMessages) ) return;
            for(var i=0; i < msgLst.length; i++) {
                var msg = msgLst[i];
                createMessageGUI(msg.user, msg.ts, msg.msg);
            }
        };

        //////////////////////////////////////////////////////
        //                                                  //
        // Function For Adding Message To Message List      //
        //                                                  //
        //////////////////////////////////////////////////////
        $scope.sendMessage = function(){
            var message = getMessage();
            var ts = getCurDateTime();

            var msg = new MessageData(selectedUser, ts, message);
            if(selectedUser in usersMessages) {
                var msgLst = usersMessages[selectedUser];
                msgLst.push(msg);		
            } else { // first time
                var msgLst = [];
                msgLst.push(msg);
                usersMessages[selectedUser] = msgLst;
            }
            createMessageGUI(selectedUser, ts, message);			

            $scope.PostMessage($scope.myUsername, selectedUser, message);
        };

        //////////////////////////////////////////////////////
        //                                                  //
        // Function POSTS A MESSAGE TO SERVER               //
        //                                                  //
        //////////////////////////////////////////////////////
        $scope.PostMessage = function (sender, receiver, message) {
            $http({
                method: 'POST',
                url: '/send_message/',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                transformRequest: function(obj) {
                    var str = [];
                    for(var p in obj)
                        str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
                    return str.join("&");
                },
                data: {sender: sender, receiver: receiver, content: message}
            }).success(function (response) {
                console.log("post message response: " + response);
            });
        };

        //////////////////////////////////////////////////////
        //                                                  //
        //      Service To Refresh/Fetch Logged In Users    //
        //                                                  //
        //////////////////////////////////////////////////////
        setInterval($scope.GetAllLoggedInUsers, 3000);

        setInterval($scope.GetAllMessages, 5000);

});

myApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});

//////////////////////////////////////////////////////
//                                                  //
//     GLOBAL DATA                                  //
//                                                  //
//////////////////////////////////////////////////////
var scrollOffset = 100;
var scrollInit   = false;		
var selectedUser = "";
var lastMsgId    = 0;


//dictionary for holding the all users messages
var usersMessages={};

$(document).ready(function(){
    $("#user-list li").bind("click", function() {
        $("ul li").removeClass('focus-user');	
        $(this).addClass('focus-user');	
        selectedUser = $(this).text();
        focusUser();
    });
});


function MessageData(user, ts, msg) {
    this.user = user;
    this.ts = ts;
    this.msg = msg;
}


//////////////////////////////////////////////////////
//                                                  //
// get the current date and time	   	    //
//                                                  //
//////////////////////////////////////////////////////
function getCurDateTime(){
    var now = new Date();
    var month =now.getMonth()+1;
    month = month < 10 ? "0"+month : month;
    var date = now.getDate();	
    date = date < 10 ? "0"+date : date;
    var year = now.getYear()+1900;
    var hh = now.getHours();
    hh = hh < 10 ? "0"+hh : hh > 12 ? "0"+(hh-12) : hh;  
    var mm = now.getMinutes();
    mm = mm < 10 ? "0"+mm : mm;  
    var ss = now.getSeconds();
    ss = ss < 10 ? "0"+ss : ss;  

    var dateTime = date+"/"+ month +"/"+year+" :: "+hh+":"+mm+":"+ss;
    return dateTime;
}



//////////////////////////////////////////////////////
//                                                  //
// function for initializing scrollbar		    //
//                                                  //
//////////////////////////////////////////////////////
function initScroll(){
    var div = document.getElementById("msgListDiv");
    if(!scrollInit){
        div.scrollTop += scrollOffset;				
    }	
}


//////////////////////////////////////////////////////
//                                                  //
// function for getting current typed message       //
//                                                  //
//////////////////////////////////////////////////////
function getMessage(){

    var message = document.getElementById("msg");
    var msgTxt = message.value;
    message.value = "";		
    return msgTxt;
}

//////////////////////////////////////////////////////
//                                                  //
// function for creating GUI for currently added    //
// messege				 	    //
//			                            //
//////////////////////////////////////////////////////

function createMessageGUI(user, ts, message){

    initScroll();
    var usersMessList = document.getElementById("usersMessList");
    var newRow = usersMessList.insertRow(-1);
    var usr = newRow.insertCell(0);
    var mess = newRow.insertCell(1);

    if(selectedUser!=""){
        usr.innerHTML = '<p class="user">'+ user + '<span id=""> [ '+ ts +' ] </span> :</p>';
        mess.innerHTML =  '<div class="message" style="float:left;"> <p class="mess-body">'+ message +' </p></div>';
        moveScrollDown();
    }
    else{
        alert("Please select a user");
    }			
}



//////////////////////////////////////////////////////
//                                                  //
// move scroll down on adding new message           //
//                                                  //
//////////////////////////////////////////////////////

function moveScrollDown(){		
    var div = document.getElementById("msgListDiv");
    div.scrollTop +=scrollOffset;
}


