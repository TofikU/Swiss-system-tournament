-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- Deleting databse if already exists
DROP DATABASE IF EXISTS tournamnet;


-- Creating database
CREATE DATABASE tournamnet;


-- Connect to database tournament
\c tournament


-- Creating players table and assigning unique id to new players
CREATE TABLE players (id SERIAL primary key,
					  name TEXT);


-- Creating matches table, each match has unique id
-- but winners and losers id are inhereted from players table
CREATE TABLE matches (id SERIAL primary key,
					  winner INTEGER REFERENCES players (id),
					  loser INTEGER REFERENCES players (id));


-- Creating VIEW standings which will present four columns
-- player id and name, win count, total matches played, 
-- and displaying players in DESC order by number of wins.
CREATE OR REPLACE VIEW standings AS
					SELECT players.id, players.name,
					SUM(CASE WHEN players.id = matches.winner THEN 1 ELSE 0 END)
					AS wins, SUM(CASE WHEN players.id = matches.winner
					OR players.id = matches.loser THEN 1 ELSE 0 END)
					AS match_count FROM players LEFT JOIN matches ON
					players.id = matches.winner OR players.id = matches.loser
					GROUP BY players.id
					ORDER BY wins DESC,
					match_count ASC;
