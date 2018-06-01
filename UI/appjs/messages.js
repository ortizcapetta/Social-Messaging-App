angular.module('AppChat').controller('MessageController', ['$http', '$log', '$scope', '$location', '$routeParams','loggedUser',
    function($http, $log, $scope, $location, $routeParams,loggedUser) {
        // This variable lets you access this controller
        // from within the callbacks of the $http object

        var thisCtrl = this;
        //this.loggedUser = loggedUser.getUser();
        var uID = loggedUser.getUser()[0].uID;



        var messageList = [];
        var memberList = [];
        var hashtagList = [];

        var like = 1;
        var dislike = -1;

        this.loadMessages = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            var gid = $routeParams.gid;

            // Now create the url with the route to talk with the rest API
             var url = "http://localhost:5000/users/groups/"+gid+"/messages";
            console.log("reqURL: " + url);
            // Now issue the http request to the rest API
            $http.get(url).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));
                    // assing the part details to the variable in the controller
                    thisCtrl.messageList = response.data.Messages;
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
    this.loadGroupMembers = function(){

            var gid = $routeParams.gid;
            var url = "http://localhost:5000/users/groups/"+gid+"/users";

            // Now set up the $http object
            // It has two function call backs, one for success and one for error
            $http.get(url).then(// success call back
                function (response){
                // The is the sucess function!
                // Copy the list of parts in the data variable
                // into the list of parts in the controller.

                    console.log("response: " + JSON.stringify(response));

                    thisCtrl.memberList = response.data.Users;

            }, // error callback
            function (response){
                // This is the error function
                // If we get here, some error occurred.
                // Verify which was the cause and show an alert.
                console.log("Err response: " + JSON.stringify(response));

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

            $log.error("Users Loaded: ", JSON.stringify(thisCtrl.memberList));
        };

        this.addMessage = function(content){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            var gid = $routeParams.gid;
            var data = {'uid': uID,'gid': gid,'content': content};
            console.log("data:" + JSON.stringify(data));

            // Now create the url with the route to talk with the rest API
             var url = "http://localhost:5000/users/groups/"+gid+"/messages";
            console.log("reqURL: " + url);
            // Now issue the http request to the rest API
            $http.post(url,data).then(
                // Success function
                function (response) {
                     console.log("data: " + JSON.stringify(response.data));
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

        this.reactToMessage = function(mid,likeValue){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            var gid = $routeParams.gid;
            var data = {'uID': uID,'mID': mid,'likeValue': likeValue};
            console.log("data:" + JSON.stringify(data));

            // Now create the url with the route to talk with the rest API
             var url = "http://localhost:5000/users/messages/"+mid+"/reactions";
            console.log("reqURL: " + url);
            // Now issue the http request to the rest API
            $http.post(url,data).then(
                // Success function
                function (response) {
                     console.log("data: " + JSON.stringify(response.data));

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
            this.replyToMessage = function(mid,content,original){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            var gid = $routeParams.gid;
            var reply = '"Re: " ' + original + '" ' + content;
            var data = {'originID':mid,'uid':uID,'gid':gid,'content':reply};
            console.log("data:" + JSON.stringify(data));

            // Now create the url with the route to talk with the rest API
             var url = "http://localhost:5000/users/messages/"+mid+"/replies";
            console.log("reqURL: " + url);
            // Now issue the http request to the rest API
            $http.post(url,data).then(
                // Success function
                function (response) {
                     console.log("data: " + JSON.stringify(response.data));
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
             this.viewHashtags = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            var gid = $routeParams.gid;

            // Now create the url with the route to talk with the rest API
             var url = "http://localhost:5000/users/groups/"+gid+"/hashtags";
            console.log("reqURL: " + url);
            // Now issue the http request to the rest API
            $http.get(url).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));
                    // assing the part details to the variable in the controller
                    thisCtrl.hashtagList = response.data.Hashtags;
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


         this.viewDetails = function (mid) {
            $location.url('/messages/'+mid);
        };

        this.viewContacts = function () {
           var gid = $routeParams.gid;
            $location.url(gid + "/contacts");
        };

         this.hashtags = function (gid) {
           var gid = $routeParams.gid;

            $location.url("/groups/"+gid+"/hashtags");
        };

        this.loadGroupMembers();
        this.loadMessages();

}]);