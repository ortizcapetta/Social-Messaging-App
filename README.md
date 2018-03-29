# Social-Messaging-App

This is phase 1 of a social messaging app database project.
Below you can find an overview of the ER database system and its components.
A visual representation of this can be seen in "ER-Diagram.png".

------------

Entities:
    User - Application user. Has 7 attributes.
    uID : bigserial - Unique ID belonging to an application user.
    Name : varchar(42) - User’s full name.
        uName : varchar(21) - User’s first name.
        uLastName : varchar(21) - User’s last name.
    e-mail : varchar() - User’s email. 
    password : varchar(42) - Stored password will be one-way encrypted beforehand.
    online : boolean - Assuming updates whenever user opens application, returns true when the user has the application open and false when the user has it closed.
    {group chats} - Composite attribute consisting of list of group chats (gID) the user belongs to.
    phone number : phoneNum - User’s phone number.

Messages - Has 6 attributes. Weak entity because a message can’t exist without a user that sends it.
    mID : bigserial - Unique ID for each message sent.
    message : text - String holding the contents of the message.
    sentBy : foreign key - Reference to User(uID). User that sent the message
    timestamp : datetime - Date and time information for when message was sent.
    {likes} - Composite attribute with users (uID) and their reaction to the message.

Chat Group - Has 5 attributes. Weak entity because a group can’t exist without users in it.
    gID : bigserial - Unique ID belonging to chat group.
    gName : varchar(21)  - Name of the group.
    {users} - Composite attribute consisting of users (uID) that belong to the group.
    {messages} - Composite attribute consisting of messages (mID) sent to the group.
    gOwner : foreign key - Reference to User(uID). Owner of the group chat.

Relationships:
    Sends - One user can send multiple messages.
    Belongs To - One user can send to multiple chat groups.
    Are Sent To - Many messages can be sent to multiple groups and one group can have multiple messages.
    Replies - More than one message can be a reply to one other message.
    Friends With - Composite attribute consisting of list of users (uID) belonging to other users.
