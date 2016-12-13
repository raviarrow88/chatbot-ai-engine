	// create the module and name it scotchApp
	var chatBotApp = angular.module('chatBotApp', ['ngRoute']);

	// configure our routes
	chatBotApp.config(function($routeProvider) {
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
	chatBotApp.controller('baseController', function($scope) {
		// create a message to display in our view
		$scope.message = 'Everyone come and see how good I look!';
	});

	chatBotApp.controller('talkController', function($scope) {
		$scope.message = 'Look! I am an about page.';
	});
