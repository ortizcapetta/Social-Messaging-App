angular.module('AppChat').controller('LoginController', ['$http', '$log', '$scope', '$location', '$routeParams', 'loggedUser',
    function($http, $log, $scope, $location, $routeParams, loggedUser) {

        var thisCtrl = this;
        this.loggedUser = {};

        this.checkLogin = function(email, password){
            var reqURL = "http://localhost:5000/login";
                console.log("reqURL: " + reqURL);
                var data = {'email': email, 'password': password}
                // Now issue the http request to the rest API
                $http.post(reqURL, data).then(
                    // Success function
                    function (response) {
                        console.log("data: " + JSON.stringify(response.data));
                        thisCtrl.loggedUser = response.data.Users;
                        loggedUser.setUser(thisCtrl.loggedUser);
                        console.log(loggedUser.getUser()[0].uID)
                        $location.path('/home');
                    },
                function (response){
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    if (status == 0){
                        alert("No hay conexion a Internet");
                    }
                    else if (status == 401){
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403){
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404){
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                });


        };

          this.registerUser = function () {
            $location.url('/register');
        };


        this.register = function(email,password,fname,lname,phone){
            var reqURL = "http://localhost:5000/register";
                console.log("reqURL: " + reqURL);
                var data = {'uFirstName': fname, 'uLastName': lname, 'password':password,
                            'phoneNum': phone , 'email':email}
                // Now issue the http request to the rest API
                $http.post(reqURL, data).then(
                    // Success function
                    function (response) {
                        console.log("data: " + JSON.stringify(response.data));
                        thisCtrl.loggedUser = response.data.Users;
                        loggedUser.setUser(thisCtrl.loggedUser);
                        $location.path('/home')
                    },
                    function (response){
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    if (status == 0){
                        alert("No hay conexion a Internet");
                    }
                    else if (status == 401){
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403){
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404){
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                });


        };
}]);