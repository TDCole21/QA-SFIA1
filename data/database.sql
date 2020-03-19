-- Database setup
BEGIN;

CREATE DATABASE IF NOT EXISTS SFIA1;

USE SFIA1;

DROP TABLE IF EXISTS Film_Actor;
DROP TABLE IF EXISTS Actors;
DROP TABLE IF EXISTS Films;

CREATE TABLE Actors (Actor_ID INT(3) AUTO_INCREMENT NOT NULL PRIMARY KEY, Actor_Name VARCHAR(50) UNIQUE NOT NULL);
CREATE TABLE Films (Film_ID INT(3) AUTO_INCREMENT NOT NULL PRIMARY KEY, Film_Name VARCHAR(50) UNIQUE NOT NULL);
CREATE TABLE Film_Actor (FilmID INT(3), ActorID INT(3), FOREIGN KEY(FilmID) REFERENCES Films (Film_ID) ON DELETE CASCADE, FOREIGN KEY(ActorID) REFERENCES Actors(Actor_ID) ON DELETE CASCADE);

INSERT INTO Actors (Actor_Name) VALUES ("Harrison Ford"),("Samuel L. Jackson"),("Morgan Freeman"),("Tom Hanks"),("Robert Downey"),("Eddie Murphy"),("Tom Cruise"),("Johnny Depp"),("Michael Caine"),("Scarlett Johansson"),("Gary Oldman"),("Robin Williams"),("Bruce Willis"),("Stellan Skarsgard"),("Anthony Daniels"),("Ian McKellen"),("Will Smith"),("Stanley Tucci"),("Matt Damon"),("Robert DeNiro"),("Cameron Diaz"),("Liam Neeson"),("Andy Serkis"),("Don Cheadle"),("Ben Stiller"),("Helena Bonham Carter"),("Orlando Bloom"),("Woody Harrelson"),("Cate Blanchett"),("Julia Roberts"),("Elizabeth Banks"),("Ralph Fiennes"),("Emma Watson"),("Tommy Lee Jones"),("Brad Pitt"),("Adam Sandler"),("Daniel Radcliffe"),("Jonah Hill"),("Owen Wilson"),("Idris Elba"),("Bradley Cooper"),("Mark Wahlberg"),("Jim Carrey"),("Dustin Hoffman"),("Leonardo DiCaprio"),("Jeremy Renner"),("Philip Seymour Hoffman"),("Sandra Bullock"),("Chris Evans"),("Anne Hathaway");
INSERT INTO Films (Film_Name) VALUES ("Star Wars: The Force Awakens"),("The Avengers"),("The Dark Knight"),("Toy Story 3"),("Shrek 2"),("War of the Worlds"),("Dead Man's Chest"),("Night at the Museum"),("Sixth Sense"),("Return of the King"),("Independence Day"),("Catching Fire"),("The Martian"),("Meet the Fockers"),("The Phantom Menace"),("Avengers: Age of Ultron"),("Harry Potter and the Deathly Hallows Part 2"),("Ocean's Eleven"),("Men in Black"),("World War Z"),("Hotel Transylvania 2"),("The LEGO Movie"),("American Sniper"),("Transformers 4"),("The Grinch"),("Titanic"),("Minions"),("The Dark Knight Rises");

INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Star Wars: The Force Awakens'), (SELECT Actor_ID from Actors WHERE Actor_Name='Harrison Ford'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='The Avengers'), (SELECT Actor_ID from Actors WHERE Actor_Name='Samuel L. Jackson'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='The Dark Knight'), (SELECT Actor_ID from Actors WHERE Actor_Name='Morgan Freeman'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Toy Story 3'), (SELECT Actor_ID from Actors WHERE Actor_Name='Tom Hanks'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='The Avengers'), (SELECT Actor_ID from Actors WHERE Actor_Name='Robert Downey, Jr.'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Shrek 2'), (SELECT Actor_ID from Actors WHERE Actor_Name='Eddie Murphy'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='War of the Worlds'), (SELECT Actor_ID from Actors WHERE Actor_Name='Tom Cruise'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Dead Man\'s Chest'), (SELECT Actor_ID from Actors WHERE Actor_Name='Johnny Depp'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='The Dark Knight'), (SELECT Actor_ID from Actors WHERE Actor_Name='Michael Caine'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='The Avengers'), (SELECT Actor_ID from Actors WHERE Actor_Name='Scarlett Johansson'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='The Dark Knight'), (SELECT Actor_ID from Actors WHERE Actor_Name='Gary Oldman'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Night at the Museum'), (SELECT Actor_ID from Actors WHERE Actor_Name='Robin Williams'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Sixth Sense'), (SELECT Actor_ID from Actors WHERE Actor_Name='Bruce Willis'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='The Avengers'), (SELECT Actor_ID from Actors WHERE Actor_Name='Stellan Skarsgard'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Star Wars: The Force Awakens'), (SELECT Actor_ID from Actors WHERE Actor_Name='Anthony Daniels'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Return of the King'), (SELECT Actor_ID from Actors WHERE Actor_Name='Ian McKellen'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Independence Day'), (SELECT Actor_ID from Actors WHERE Actor_Name='Will Smith'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Catching Fire'), (SELECT Actor_ID from Actors WHERE Actor_Name='Stanley Tucci'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='The Martian'), (SELECT Actor_ID from Actors WHERE Actor_Name='Matt Damon'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Meet the Fockers'), (SELECT Actor_ID from Actors WHERE Actor_Name='Robert DeNiro'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Shrek 2'), (SELECT Actor_ID from Actors WHERE Actor_Name='Cameron Diaz'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='The Phantom Menace'), (SELECT Actor_ID from Actors WHERE Actor_Name='Liam Neeson'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Star Wars: The Force Awakens'), (SELECT Actor_ID from Actors WHERE Actor_Name='Andy Serkis'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Avengers: Age of Ultron'), (SELECT Actor_ID from Actors WHERE Actor_Name='Don Cheadle'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Meet the Fockers'), (SELECT Actor_ID from Actors WHERE Actor_Name='Ben Stiller'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Harry Potter and the Deathly Hallows Part 2'), (SELECT Actor_ID from Actors WHERE Actor_Name='Helena Bonham Carter'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Dead Man\'s Chest'), (SELECT Actor_ID from Actors WHERE Actor_Name='Orlando Bloom'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Catching Fire'), (SELECT Actor_ID from Actors WHERE Actor_Name='Woody Harrelson'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Return of the King'), (SELECT Actor_ID from Actors WHERE Actor_Name='Cate Blanchett'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Ocean\'s Eleven'), (SELECT Actor_ID from Actors WHERE Actor_Name='Julia Roberts'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Catching Fire'), (SELECT Actor_ID from Actors WHERE Actor_Name='Elizabeth Banks'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Harry Potter and the Deathly Hallows Part 2'), (SELECT Actor_ID from Actors WHERE Actor_Name='Ralph Fiennes'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Harry Potter and the Deathly Hallows Part 2'), (SELECT Actor_ID from Actors WHERE Actor_Name='Emma Watson'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Men in Black'), (SELECT Actor_ID from Actors WHERE Actor_Name='Tommy Lee Jones'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='World War Z'), (SELECT Actor_ID from Actors WHERE Actor_Name='Brad Pitt'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Hotel Transylvania 2'), (SELECT Actor_ID from Actors WHERE Actor_Name='Adam Sandler'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Harry Potter and the Deathly Hallows Part 2'), (SELECT Actor_ID from Actors WHERE Actor_Name='Daniel Radcliffe'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='The LEGO Movie'), (SELECT Actor_ID from Actors WHERE Actor_Name='Jonah Hill'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Night at the Museum'), (SELECT Actor_ID from Actors WHERE Actor_Name='Owen Wilson'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Avengers: Age of Ultron'), (SELECT Actor_ID from Actors WHERE Actor_Name='Idris Elba'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='American Sniper'), (SELECT Actor_ID from Actors WHERE Actor_Name='Bradley Cooper'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Transformers 4'), (SELECT Actor_ID from Actors WHERE Actor_Name='Mark Wahlberg'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='The Grinch'), (SELECT Actor_ID from Actors WHERE Actor_Name='Jim Carrey'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Meet the Fockers'), (SELECT Actor_ID from Actors WHERE Actor_Name='Dustin Hoffman'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Titanic'), (SELECT Actor_ID from Actors WHERE Actor_Name='Leonardo DiCaprio'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='The Avengers'), (SELECT Actor_ID from Actors WHERE Actor_Name='Jeremy Renner'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Catching Fire'), (SELECT Actor_ID from Actors WHERE Actor_Name='Philip Seymour Hoffman'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='Minions'), (SELECT Actor_ID from Actors WHERE Actor_Name='Sandra Bullock'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='The Avengers'), (SELECT Actor_ID from Actors WHERE Actor_Name='Chris Evans'));
INSERT INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name='The Dark Knight Rises'), (SELECT Actor_ID from Actors WHERE Actor_Name='Anne Hathaway'));

COMMIT;