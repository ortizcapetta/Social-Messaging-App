CREATE TABLE Users (
	uID		    bigserial			    primary key,
	uFirstName	varchar(21)			    NOT NULL,
	uLastName	varchar(21)		    	NOT NULL,
    password	varchar(42)		    	NOT NULL,	--encrypted password
	phoneNum	varchar(10)			    NOT NULL,
	email		varchar(100)			NOT NULL UNIQUE
	
);

CREATE TABLE Messages (
	mID		    bigserial		    	primary key,
	uID			integer references		Users(uID),
	gID		    integer references		Groups(gID),	--Group chat msg is in
	timeStamp	timestamp		    	NOT NULL,
	content	    varchar(300)			NOT NULL
);

CREATE TABLE Reactions (
	rID			bigserial				primary key,
	uID			integer  references		Users(uID),
    mID	    	integer references		Messages(mID),
    likeValue	int				        NOT NULL
);

CREATE TABLE Groups (
    gID		    bigserial  				primary key,
    gName		varchar(21)			    NOT NULL,
    gOwner	    integer references  	Users(uID)
);

CREATE TABLE Replies (
	originID	integer references		Messages(mID),
	replyID		integer references		Messages(mID),
	Primary key (originID, replyID)
);

CREATE TABLE GUsers (
	gID		    integer references	    Groups(gID),
	uID		    integer references	    Users(uID),
	Primary key(gID, uID)
);

CREATE TABLE Contacts (
	uID		    integer references	    Users(uID),	--person
	friend	    integer references	    Users(uID),	--friends
	Primary key(uID,friend)
);

CREATE TABLE Hashtags(
	htID		bigserial				primary key,
	hashtag		varchar(21)				NOT NULL,
	mID			integer references		Messages(mID)
);