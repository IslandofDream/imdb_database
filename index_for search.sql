use imdb; 

CREATE INDEX movie_name_index ON movie(primary_title(255), original_title(255));

CREATE INDEX person_name_index ON person(name);

CREATE INDEX principal_job_category_index ON principals(job_category);

CREATE INDEX movie_title_type_index ON movie(title_type);

CREATE INDEX movie_genres_genre_index ON movie_genres(genre);

CREATE INDEX akas_region_index ON akas(region);

ALTER TABLE movie DROP INDEX movie_name_index;

ALTER TABLE person DROP INDEX person_name_index;

ALTER TABLE principals DROP INDEX  principal_job_category_index;

ALTER TABLE movie DROP INDEX  movie_title_type_index;

ALTER TABLE movie DROP INDEX movie_title_index;

ALTER TABLE movie_genres DROP INDEX movie_genres_genre_index;

ALTER TABLE akas DROP INDEX akas_region_index;

