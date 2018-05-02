# Social-Messaging-App

This is phase 1 of a social messaging app database project.
Below you can find an overview of the ER database system and its components.
A visual representation of this can be seen in "ER-Diagram.png".

------------

Entities:
    Users

    uID : bigserial - Unique ID belonging to an application user.

    Name : varchar(42) - User’s full name.

        uName : varchar(21) - User’s first name.

        uLastName : varchar(21) - User’s last name.

    e-mail : varchar() - User’s email. 

    password : varchar(42) - Stored password will be one-way encrypted beforehand.

    phone number : phoneNum - User’s phone number.


Messages

    mID : bigserial - Unique ID for each message sent.

    message : text - String holding the contents of the message.

    sentBy : foreign key - Reference to User(uID). User that sent the message

    timestamp : datetime - Date and time information for when message was sent.


Chat Groups

    gID : bigserial - Unique ID belonging to chat group.

    gName : varchar(21)  - Name of the group.


Reactions

    rID : bigserial - Unique ID belonging to a specific reaction.
    
    uID : foreign key - Reference to Users(uID). User that reacted to a message.
    
    mID : bigserial - Reference to Messages(mID). Message that was reacted to.
    
    likeValue : int - Integer that represents a positive (+1) or negative (-1) reaction.


Hashtags

    htID : bigserial - Unique ID belonging to a tag phrase.
    
    hashtag : varchar(21) - Text of the tag phrase.
    
    mID : foreign key - Reference to Messages(mID). Message that contained hashtag.


Relationships:

    Sends - One user can send multiple messages.
    
    Belongs To - One user can send to multiple chat groups.
   
    gOwner : foreign key - Reference to User(uID). Owner of the group chat.
    
    Are Sent To - Many messages can be sent to multiple groups and one group can have multiple messages.
    
    Replies - More than one message can be a reply to one other message.
    
    Friends With - List of users (uID) belonging to other users that are in a user’s contact list.
    
    Contains - A message can contain various hashtags and a hashtag can be associated with many messages.
