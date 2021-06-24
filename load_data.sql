SET GLOBAL local_infile = 1;

drop table aliases;

CREATE TABLE akas (
  title_id          VARCHAR(255) NOT NULL, -- not null bc PK
  ordering          INTEGER NOT NULL, -- not null bc PK
  title             TEXT NOT NULL,
  region				    CHAR(4),
  language          CHAR(4),
  is_original_title	BOOLEAN
);

use imdb;
-- Load Aliases.tsv into Aliases table
LOAD DATA LOCAL INFILE  'C:/Users/junwoo/Desktop/myindb/Aliases.tsv'
INTO TABLE akas
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;


LOAD DATA LOCAL INFILE  'C:/Users/junwoo/Desktop/myindb/Alias_attributes.tsv'
INTO TABLE akas_attributes
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

-- Load Alias_types.tsv into Alias_types table
LOAD DATA LOCAL INFILE  'C:/Users/junwoo/Desktop/myindb/Alias_types.tsv'
INTO TABLE akas_types
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

-- Load Directors.tsv into Directors table
LOAD DATA LOCAL INFILE 'C:/Users/junwoo/Desktop/myindb/Directors.tsv'
INTO TABLE Directors
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

-- Load Writers.tsv into Writers table
LOAD DATA LOCAL INFILE 'C:/Users/junwoo/Desktop/myindb/Writers.tsv'
INTO TABLE Writers
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

-- Load Episode_belongs_to.tsv into Episode_belongs_to table
LOAD DATA LOCAL INFILE 'C:/Users/junwoo/Desktop/myindb/Episode_belongs_to.tsv'
INTO TABLE Episode
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

-- Load Names_.tsv into Names_ table
LOAD DATA LOCAL INFILE 'C:/Users/junwoo/Desktop/myindb/Names_.tsv'
INTO TABLE information
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

-- Load Name_worked_as.tsv into Name_worked_as table
LOAD DATA LOCAL INFILE 'C:/Users/junwoo/Desktop/myindb/Name_worked_as.tsv'
INTO TABLE information_profession
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

-- Load Known_for.tsv into Known_for table
LOAD DATA LOCAL INFILE 'C:/Users/junwoo/Desktop/myindb/Known_for.tsv'
INTO TABLE starring
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

-- Load Principals.tsv into Principals table
LOAD DATA LOCAL INFILE 'C:/Users/junwoo/Desktop/myindb/Principals.tsv'
INTO TABLE Principals
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

-- Load Had_role.tsv into Had_role table
LOAD DATA LOCAL INFILE 'C:/Users/junwoo/Desktop/myindb/Had_role.tsv'
INTO TABLE information_role
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

-- Load Titles.tsv into Titles table
LOAD DATA LOCAL INFILE 'C:/Users/junwoo/Desktop/myindb/Titles.tsv'
INTO TABLE movie
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

-- Load Title_genres.tsv into Title_genres table
LOAD DATA LOCAL INFILE  'C:/Users/junwoo/Desktop/myindb/Title_genres.tsv'
INTO TABLE movie_genres
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

-- Load Title_ratings.tsv into Title_ratings table
LOAD DATA LOCAL INFILE  'C:/Users/junwoo/Desktop/myindb/Title_ratings.tsv'
INTO TABLE movie_ratings
COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;

select * 
from movie_ratings;