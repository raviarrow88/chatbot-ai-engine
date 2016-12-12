	// create the module and name it scotchApp
	var scotchApp = angular.module('scotchApp', ['ngRoute']);

	// configure our routes
	scotchApp.config(function($routeProvider) {
		$routeProvider

			// route for the home page
			.when('/', {
				templateUrl : 'views/home.html',
				controller  : 'baseController'
			})

			// route for the talk page
			.when('/talk', {
				templateUrl : 'views/talk.html',
				controller  : 'talkController'
			})


	});

	// create the controller and inject Angular's $scope
	scotchApp.controller('baseController', function($scope) {
		// create a message to display in our view
		$scope.message = 'Everyone come and see how good I look!';
	});

	scotchApp.controller('talkController', function($scope) {
		$scope.message = 'Look! I am an about page.';
	});
