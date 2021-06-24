
-- Alias_attributes
CREATE INDEX akas_attributes_index ON akas_attributes(title_id);

-- Alias_types
CREATE INDEX akas_types_index ON akas_types(title_id);

-- Aliases
CREATE INDEX akas_index ON akas(title_id);

-- Directors
CREATE INDEX Directors_title_id_index ON Directors(title_id);
CREATE INDEX Directors_name_id_index ON Directors(name_id);

-- Episode_belongs_to
CREATE INDEX Episode_title_id_index ON Episode(episode_title_id);
CREATE INDEX Episode_show_title_id_index ON Episode(parent_tv_show_title_id);

-- Had_role
CREATE INDEX information_title_id_index ON information_role(title_id);
CREATE INDEX information_name_id_index ON information_role(name_id);

-- Known_for
CREATE INDEX starring_index ON starring(name_id);

-- Name_worked_as
CREATE INDEX information_profession_index ON information_profession(profession);

-- Names_
CREATE INDEX information_index ON information(name_id);

-- Principals
CREATE INDEX Principals_index ON Principals(title_id);

-- Title_genres
CREATE INDEX movie_genres_title_id_index ON movie_genres(title_id);
CREATE INDEX movie_genres_genre_index ON movie_genres(genre);

-- Title_ratings
CREATE INDEX movie_ratings_index ON movie_ratings(title_id);

-- Titles
CREATE INDEX movie_index ON movie(title_id);

CREATE INDEX movie_name_index ON movie(primary_title(255), original_title(255));

-- Writers
CREATE INDEX Writers_title_id_index ON Writers(title_id);
CREATE INDEX Writers_name_id_index ON Writers(name_id);