/*
------------------------------------------------------------------------------
				PLACES MANAGER ANGULAR JS SCRIPT
------------------------------------------------------------------------------
*/

// creating the module
var myApp = 
angular
.module("placeModule", [])
.controller("placeController", function($scope, $http) {	

	$scope.message = "Favorite Places";

	// some place objects
	$scope.places = [];
	$scope.categories = [];

        $scope.GetAllCategories = function () {
             $http.get("/categories/")
                 .then(function(response){ 
                     $scope.categories = response.data; 

                     // get places for first category
                     $scope.GetAllPlaces($scope.categories[0].id);
                 });
        };

        $scope.GetAllPlaces = function (pid) {
             $http.get("/places/" + pid)
                 .then(function(response){ 
                     $scope.places = response.data; 
                 });
        };
            
	// function to add new place
	$scope.addTask = function() {
		//$scope.places.push({ title: $scope.new_place, completed: false});
	}

        // show categories on start
        $scope.GetAllCategories();
});

myApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});
