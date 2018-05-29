

angular.module('AppChat').controller('MessageDetailsController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        // This variable lets you access this controller
        // from within the callbacks of the $http object

        var thisCtrl = this;

        // This variable hold the information on the part
        // as read from the REST API
        var messageDetails = []
        var messageLikes = []
        var messageDislikes =[]

        this.loadMessageDetails = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            var mid = $routeParams.mid;

            // Now create the url with the route to talk with the rest API
             var url = "http://localhost:5000/users/messages/"+mid;
            console.log("reqURL: " + url);
            // Now issue the http request to the rest API
            $http.get(url).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));
                    // assing the part details to the variable in the controller
                    thisCtrl.messageDetails = response.data.Messages;
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;

                    if (status == 0) {
                        alert("No hay conexion a Internet");
                    }
                    else if (status == 401) {
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403) {
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404) {
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            );
        };

        this.loadMessageLikes = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            var mid = $routeParams.mid;

            // Now create the url with the route to talk with the rest API
             var url = "http://localhost:5000/users/messages/"+mid+"/reactions/likedby";
            console.log("reqURL: " + url);
            // Now issue the http request to the rest API
            $http.get(url).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));
                    // assing the part details to the variable in the controller
                    thisCtrl.messageLikes = response.data.Reactions;
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;

                    if (status == 0) {
                        alert("No hay conexion a Internet");
                    }
                    else if (status == 401) {
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403) {
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404) {
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            );
        };

        this.loadMessageDislikes = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            var mid = $routeParams.mid;

            // Now create the url with the route to talk with the rest API
             var url = "http://localhost:5000/users/messages/"+mid+"/reactions/dislikedby";
            console.log("reqURL: " + url);
            // Now issue the http request to the rest API
            $http.get(url).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));
                    // assing the part details to the variable in the controller
                    thisCtrl.messageDislikes = response.data.Reactions;
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;

                    if (status == 0) {
                        alert("No hay conexion a Internet");
                    }
                    else if (status == 401) {
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403) {
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404) {
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            );
        };

        this.loadMessageDetails();
        this.loadMessageLikes();
        this.loadMessageDislikes();
}]);