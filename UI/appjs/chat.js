angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope', //dependency injections
//something about name being the name of the main (?)
    function($http, $log, $scope) {
        var thisCtrl = this; //this = object that thhtp service implements
           //makes ref to controller (?)

        this.messageList = []; //array that has messages list
        this.counter  = 2;
        this.newText = "";

        this.loadMessages = function(){
            // Get the messages from the server through the rest api o_o
            //var url = "http://localhost:5000/blahblahblah/messages chatt app;
            //there's a way to do this as a singleton tho @_@

            thisCtrl.messageList.push({"id": 1, "text": "Hola Mi Amigo", "author" : "Bob",
            "like" : 4, "nolike" : 1});
            thisCtrl.messageList.push({"id": 2, "text": "Hello World", "author": "Joe",
                "like" : 11, "nolike" : 12});

            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };
        //check partsapp ui for more stuff
        //callback de exito y callback de error


        this.postMsg = function(){
            var msg = thisCtrl.newText;
            // Need to figure out who I am
            var author = "Me";
            var nextId = thisCtrl.counter++;
            thisCtrl.messageList.unshift({"id": nextId, "text" : msg, "author" : author, "like" : 0, "nolike" : 0});
            thisCtrl.newText = "";
        };

        this.loadMessages();
}]);
