
use imdb;

select *
from movie
where movie.original_title = 'Doom' and movie.primary_title = 'Doom';

select person.name_ , movie.title_type ,  movie.primary_title, review.average_rating
from  person, movie , principals, review
where principals.name_id = person.name_id
and principals.title_id = movie.title_id
and review.title_id = movie.title_id
and movie.title_type = 'movie'
and person.name_ like 'Russell Crowe' 
and principals.job_category = 'actor'
order by review.average_rating DESC;

select person.name_ , movie.title_type ,  movie.primary_title, movie.start_year
from  person, movie , principals
where principals.name_id = person.name_id
and principals.title_id = movie.title_id
and movie.title_type = 'movie'
and person.name_ like 'Alfred Hitchcock' 
and principals.job_category = 'director'
order by movie.start_year;


select movie.title_type, movie.primary_title, movie_genres.genre, review.num_votes
from movie, movie_genres, review
where movie.title_id = movie_genres.title_id
and movie.title_id = review.title_id
and movie_genres.title_id = review.title_id
and movie.title_type = 'movie'
and movie_genres.genre like 'Drama%'
order by review.num_votes ASC;

select movie.title_type, movie.primary_title, movie_genres.genre, review.average_rating
from movie, movie_genres, review
where movie.title_id = movie_genres.title_id
and movie.title_id = review.title_id
and movie_genres.title_id = review.title_id
and movie.title_type = 'movie'
and movie_genres.genre like 'Drama%' 
order by review.average_rating DESC;

select  movie.primary_title ,episode.season_number, review.num_votes
from movie, episode, review
where movie.title_id = episode.episode_title_id
and movie.title_id = review.title_id
and episode.season_number > 5
order by review.num_votes ASC;

select distinct(movie.primary_title) , akas.region, review.num_votes, review.average_rating
from movie, akas, review
where movie.title_id = akas.title_id
and movie.title_id = review.title_id
and movie.title_type = 'movie'
and akas.region = 'KR'
and review.num_votes > 10000
order by review.average_rating DESC;
