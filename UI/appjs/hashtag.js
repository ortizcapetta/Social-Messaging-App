
angular.module('AppChat').controller('HashtagController', ['$http','$route','$log', '$scope', '$location','$routeParams','loggedUser','$route',
    function($http, $scope,$log, $scope, $location,$routeParams,loggedUser,$route) {
        var thisCtrl = this;



        this.loggedUser = loggedUser.getUser();


 this.viewHashtags = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
             var hashtagList= [];
            var gid = $routeParams.gid;

            // Now create the url with the route to talk with the rest API
            var url = "http://localhost:5000/users/groups/"+gid+"/messages/hashtags";
            console.log("reqURL: " + url);
            // Now issue the http request to the rest API
            $http.get(url).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));
                    // assing the part details to the variable in the controller
                    thisCtrl.hashtagList = response.data.hashtags;
                    console.log("data: " + JSON.stringify(hashtagList))
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

        this.searchHashtag = function(hashtag){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
             var hashtagList= [];
            var gid = $routeParams.gid;

            // Now create the url with the route to talk with the rest API
             var url = 'http://127.0.0.1:5000/users/groups/hashtags?gID='+gid+'&hashtag=!'+hashtag;
            console.log("reqURL: " + url);
            // Now issue the http request to the rest API
            $http.get(url).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));
                    // assing the part details to the variable in the controller
                    thisCtrl.hashtagList = response.data.hashtags;


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




        this.searchHashtag();
        //this.viewHashtags();


}]);
