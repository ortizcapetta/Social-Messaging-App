INSERT INTO Users (uID, uFirstName, uLastName, password, phoneNum, email) 
VALUES (1, 'Gustavo', 'Reyes', 'password', 7875555555, 'gustavo.heroku@upr.edu'),
(2, 'Antonio', 'Lugo', 'password', 7875555555, 'antonio.heroku@upr.edu'),
(3, 'Alejandra', 'Ortiz', 'password', 7875555555, 'alejandra.heroku@upr.edu');

INSERT INTO Groups (gID, gName, gOwner) 
VALUES (1, 'group1', 1),
(2, 'group2', 2),
(3, 'group3', 3);

INSERT INTO Messages (mID, uID, gID, timeStamp, content) 
VALUES (1, 1, 1, 'January 8 04:05:06 1999 PST','hey there'),
(2, 2, 2, 'January 8 04:05:06 1999 PST', 'hey there'),
(3, 3, 3, 'January 8 04:05:06 1999 PST', 'hey there');

INSERT INTO Reactions (rID, uID, mID, likeValue) 
VALUES (1, 1, 1, 1),
(2, 2, 2, 1),
(3, 3, 3, 1);

INSERT INTO Replies (originID, replyID) 
VALUES (1, 2),
(2, 3),
(3, 1);

INSERT INTO GUsers (gID, uID) 
VALUES (1, 1),
(2, 2),
(3, 3);

INSERT INTO Contacts (uID, friend) 
VALUES (1, 2),
(2, 3),
(3, 1);

INSERT INTO Hashtags (htID, hashtag, mID) 
VALUES (1, 'huelga', 2),
(2, 'finals',3),
(3, 'noHuelga',1);