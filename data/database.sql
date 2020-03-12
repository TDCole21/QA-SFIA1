CREATE DATABASE IF NOT EXISTS SFIA1;

USE SFIA1;

CREATE TABLE Actors (Actor_ID INT(3) AUTO_INCREMENT NOT NULL PRIMARY KEY, Actor_Name VARCHAR(50) NOT NULL);
CREATE TABLE Films (Film_ID INT(3) AUTO_INCREMENT NOT NULL PRIMARY KEY, Film_Name VARCHAR(50) NOT NULL);
CREATE TABLE Film_Actor (FilmID INT(3), ActorID INT(3), FOREIGN KEY(FilmID) REFERENCES Films (Film_ID), FOREIGN KEY(ActorID) REFERENCES Actors(Actor_ID));

INSERT INTO Actors (Actor_Name) VALUES ("Harrison Ford"),("Samuel L. Jackson"),("Morgan Freeman"),("Tom Hanks"),("Robert Downey"),("Eddie Murphy"),("Tom Cruise"),("Johnny Depp"),("Michael Caine"),("Scarlett Johansson"),("Gary Oldman"),("Robin Williams"),("Bruce Willis"),("Stellan Skarsgard"),("Anthony Daniels"),("Ian McKellen"),("Will Smith"),("Stanley Tucci"),("Matt Damon"),("Robert DeNiro"),("Cameron Diaz"),("Liam Neeson"),("Andy Serkis"),("Don Cheadle"),("Ben Stiller"),("Helena Bonham Carter"),("Orlando Bloom"),("Woody Harrelson"),("Cate Blanchett"),("Julia Roberts"),("Elizabeth Banks"),("Ralph Fiennes"),("Emma Watson"),("Tommy Lee Jones"),("Brad Pitt"),("Adam Sandler"),("Daniel Radcliffe"),("Jonah Hill"),("Owen Wilson"),("Idris Elba"),("Bradley Cooper"),("Mark Wahlberg"),("Jim Carrey"),("Dustin Hoffman"),("Leonardo DiCaprio"),("Jeremy Renner"),("Philip Seymour Hoffman"),("Sandra Bullock"),("Chris Evans"),("Anne Hathaway");
INSERT INTO Films (Film_Name) VALUES ("Star Wars: The Force Awakens"),("The Avengers"),("The Dark Knight"),("Toy Story 3"),("Shrek 2"),("War of the Worlds"),("Dead Man's Chest"),("Night at the Museum"),("Sixth Sense"),("Return of the King"),("Independence Day"),("Catching Fire"),("The Martian"),("Meet the Fockers"),("The Phantom Menace"),("Avengers: Age of Ultron"),("Harry Potter and the Deathly Hallows Part 2"),("Ocean's Eleven"),("Men in Black"),("World War Z"),("Hotel Transylvania 2"),("The LEGO Movie"),("American Sniper"),("Transformers 4"),("The Grinch"),("Titanic"),("Minions"),("The Dark Knight Rises");

INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Star Wars: The Force Awakens'), (SELECT Actor_ID from Actors WHERE Actor_Name='Harrison Ford'));


-- Deletes from two tables
DELETE Actors, Film_Actor
FROM Actors
INNER JOIN Film_Actor ON Actors.Actor_ID = Film_Actor.ActorID
WHERE Actors.Actor_Name='Harrison Ford';

-- Select from two independent tables
SELECT *
FROM Actors
INNER JOIN Film_Actor ON Actors.Actor_ID = Film_Actor.ActorID
WHERE Actors.Actor_Name='Harrison Ford';


select * from Films where Film_ID in (select FilmID from Film_Actor)
select Film_Name from Films where Film_ID in (select FilmID from Film_Actor where ActorID=(SELECT Actor_ID from Actors WHERE Actor_Name='Harrison Ford'));

-- Update two independent tables
cur.execute("UPDATE Actors SET Actor_Name=(%s) WHERE Actor_Name=(%s)", [toname, fromname])
cur.execute("INSERT INTO Film_Actor VALUES((SELECT Film_ID from Films WHERE Film_Name=(%s), (SELECT Actor_ID from Actors WHERE Actor_Name=(%s))))", [actorname, filmname])

INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Star Wars: The Force Awakens'), (SELECT Actor_ID from Actors WHERE Actor_Name='Harrison Ford'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name="Shrek 2"), (SELECT Actor_ID from Actors WHERE Actor_Name="Eddie Murphy"));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name=(%s)), (SELECT Actor_ID from Actors WHERE Actor_Name=(%s)));