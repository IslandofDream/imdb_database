
select *
from movie
use index(movie_name_index)
where movie.original_title = 'Doom' and movie.primary_title = 'Doom';


select *
from movie
where movie.original_title = 'matrix';