/*
------------------------------------------------------------------------------
				PLACES MANAGER ANGULAR JS SCRIPT
------------------------------------------------------------------------------
*/

// creating the module
var myApp = 
angular
.module("chatModule", [])
.controller("chatController", function($scope, $http) {	

	$scope.message = "Chatzila Dashboard";

	// some chat objects
	$scope.users = [];

        //----------------------------------------------------
        // function to get all logged in users
        //----------------------------------------------------
        $scope.GetAllLoggedInUsers = function () {
             $http.get("/get_logged_users/")
                 .then(function(response){ 
                     $scope.users = response.data; 
                 });
        };

	// function to add new place
	$scope.addTask = function() {
		//$scope.places.push({ title: $scope.new_place, completed: false});
	}

        // show users on start
        $scope.GetAllLoggedInUsers();
});

myApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});
