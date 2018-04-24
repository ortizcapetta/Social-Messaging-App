CREATE TABLE Users (
	uID		    bigserial			    primary key,
	uFirstName	varchar(21)			    NOT NULL,
	uLastName	varchar(21)		    	NOT NULL,
    password	varchar(42)		    	NOT NULL,	--encrypted password
	phoneNum	int				        NOT NULL,
	email		varchar(100)			NOT NULL
	
)

CREATE TABLE Messages (
	mID		    bigserial		    	primary key,
	sentBy		foreign key references	User(uID),
	gID		    foreign key references	Group(gID),	--Group chat msg is in
	timeStamp	datetime		    	NOT NULL,
	content	    varchar(300)			NOT NULL
)

CREATE TABLE Reactions (
	uID		foreign key references	User(uID),
    mID	    foreign key references	Message(mID),
    likeValue	int				        NOT NULL,
    Primary key (user,message)
)

CREATE TABLE Groups (
    gID		    bigserial			    primary key,
    gName		varchar(21)			    NOT NULL,
    gOwner	    foreign key references  User(uID)
)

CREATE TABLE Replies (
	originID	foreign key references	Message(mID),
	replyID		foreign key references	Message(mID),
	Primary key (originID, replyID)
)

CREATE TABLE GUsers (
	gID		    foreign key references	    Group(gID),
	uID		    foreign key references	    User(uID),
	Primary key(gID, uID)
)

CREATE TABLE Contacts (
	uID		    foreign key references	    User(uID),	--person
	friend	    foreign key references	    User(uID),	--friends
	Primary key(uID,friend)
)
