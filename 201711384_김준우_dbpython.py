import pymysql
import sys

        
def fun1(): 
    
    title = input('검색할 영화 제목을 적어주세요.\n')
    # 검색할 영화제목을 입력받습니다. 
    title = "\'" + title + "\'" #문자열 이므로 ''가 sql문에 있어야 합니다. 그렇기 위해서 입력받은 과목번호에 ''을 붙여줍니다.
    sql = 'select * from movie where movie.original_title = %s and movie.primary_title = %s;' %(title, title)
    curs.execute(sql)
    row = curs.fetchone()
    while row:
        print("title_id: %s, titletype : %s primary_title: %s original_title : %s is_adult : %s start_year : %s end_year : %s runtime_minutes : %s" 
              %(row['title_id'],row['title_type'],row['primary_title'],row['original_title'],
                row['is_adult'],row['start_year'],row['end_year'],row['runtime_minutes']))
        row = curs.fetchone()
    # 검색결과를 출력합니다.
    conn.commit()
    # sql 구문 실행 후 적용을 위해 커밋 해줍니다. 
    
def fun2():
    actor = input('배우를 입력해주세요.\n')
    actor = "\'" + actor + "\'"
    sql = 'select person.name_ , movie.title_type ,  movie.primary_title, review.average_rating '\
            +'from  person, movie , principals, review '\
            +'where principals.name_id = person.name_id '\
            +'and principals.title_id = movie.title_id '\
            +'and review.title_id = movie.title_id '\
            +'and movie.title_type = \'movie\' '\
            +'and person.name_ like %s and principals.job_category = \'actor\' order by review.average_rating DESC;' %(actor)
    # principal, movie, person테이블들을 조인 시키고 입력받은 배우가 출연한 영화들을 검색하고 review테이블을 통해서 
    # 평점이 높은 순으로 정렬합니다.
    curs.execute(sql)
    row = curs.fetchone()
    while row:
        print("name: %s, titletype : %s primary_title: %s average_rating : %.1f" 
              %(row['name_'],row['title_type'],row['primary_title'],row['average_rating']))
        row = curs.fetchone()
    # 검색결과를 출력합니다. 요소가 너무 많기 때문에 이름, 타입, 제목, 별점 만 출력합니다. 
    conn.commit()

    
def fun3():
    director = input('영화감독을 입력해주세요.\n')
    director = "\'" + director + "\'"
    sql = 'select person.name_ , movie.title_type ,  movie.primary_title, movie.start_year '\
        +'from  person, movie , principals '\
        +'where principals.name_id = person.name_id '\
        +'and principals.title_id = movie.title_id '\
        +'and movie.title_type = \'movie\' '\
        +'and person.name_ like %s and principals.job_category = \'director\' order by movie.start_year;' %(director)
    # principal, movie, person테이블들을 조인 시키고 입력받은 배우가 출연한 영화들을 검색하고 review테이블을 통해서 
    # 개봉년도 순으로 정렬합니다.
    curs.execute(sql)
    row = curs.fetchone()
    while row:
        print("name: %s, titletype : %s primary_title: %s start_year : %d" 
              %(row['name_'],row['title_type'],row['primary_title'],row['start_year']))
        row = curs.fetchone()
    # 검색결과를 출력합니다. 요소가 너무 많기 때문에 이름, 타입, 제목, 개봉년도 만 출력합니다. 
    conn.commit()
            
def fun4():
    choice = int(input('리뷰순으로 검색하려면 1번 별점 높은 순으로 검색하려면 2번을 입력하세요\n'))
    # 별점순 리뷰순으로 검색할지 결정합니다. 
    if choice == 1:
        sql = 'select movie.title_type, movie.primary_title, movie_genres.genre, review.num_votes '\
            +'from movie, movie_genres, review '\
            +'where movie.title_id = movie_genres.title_id '\
            +'and movie.title_id = review.title_id '\
            +'and movie_genres.title_id = review.title_id '\
            +'and movie.title_type = \'movie\' '\
            +'and movie_genres.genre like \'Drama%\' '\
            +'order by review.num_votes DESC;'
        # 리뷰가 많은 순으로 검색하는 경우입니다. 
        #movie, movie_genre, review 테이블을 각각 조인 시킨후 drama 장르에 해당하는 타이틀 타입이 영화인 
        #영화만 리뷰순으로 정렬합니다. 
        curs.execute(sql)
        row = curs.fetchone()
        while row:
            print("num_votes : %d  primary_title : %s  title_type: %s genre : %s " 
                  %(row['num_votes'],row['primary_title'],row['title_type'],row['genre']))
            row = curs.fetchone()
        # 검색결과를 출력합니다. 요소가 너무 많기 때문에 타이틀타입, 제목, 장르, 리뷰갯수 만 출력합니다. 
        conn.commit()
    elif choice == 2:
        sql = 'select movie.title_type, movie.primary_title, movie_genres.genre, review.average_rating '\
            +'from movie, movie_genres, review '\
            +'where movie.title_id = movie_genres.title_id '\
            +'and movie.title_id = review.title_id '\
            +'and movie_genres.title_id = review.title_id '\
            +'and movie.title_type = \'movie\' '\
            +'and movie_genres.genre like \'Drama%\' '\
            +'order by review.average_rating DESC;'
        # 별점이 높은 순으로 검색하는 경우입니다. 
        #movie, movie_genre, review 테이블을 각각 조인 시킨후 drama 장르에 해당하는 타이틀 타입이 영화인 
        #영화만 리뷰순으로 정렬합니다. 
        curs.execute(sql)
        row = curs.fetchone()
        while row:
            print("average_rating : %.1f title: %s title_type: %s genre : %s " 
                  %(row['average_rating'],row['primary_title'],row['title_type'],row['genre']))
            row = curs.fetchone()
        # 검색결과를 출력합니다. 요소가 너무 많기 때문에 타이틀타입, 제목, 장르, 리뷰갯수 만 출력합니다. 
        conn.commit()        
    else:
        print("잘못된 입력입니다.")

def fun5():

    sql = 'select movie.primary_title ,episode.season_number, review.num_votes '\
        +'from movie, episode, review '\
        +'where movie.title_id = episode.episode_title_id '\
        +'and movie.title_id = review.title_id '\
        +'and episode.season_number > 5 '\
        +'order by review.num_votes ASC;'
    # movie, episode, review 테이블을 조인시키고 시즌넘버가 5이상인 
    # 데이터에 대해서 리뷰가 적은순으로 정렬시킵다.
    curs.execute(sql)
    row = curs.fetchone()
    while row:
        print("primary_title : %s season_number: %d num_votes : %d" 
              %(row['primary_title'],row['season_number'],row['num_votes']))
        row = curs.fetchone()
    # 검색결과를 출력합니다. 제목과 시즌 넘버, 리뷰 만 출력합니다.
    conn.commit()
    
    
def fun6():

    sql = 'select distinct(movie.primary_title) , akas.region, review.num_votes, review.average_rating ' \
        +'from movie, akas, review '\
        +'where movie.title_id = akas.title_id '\
        +'and movie.title_id = review.title_id '\
        +'and movie.title_type = \'movie\' '\
        +'and akas.region = \'KR\' '\
        +'and review.num_votes > 10000 '\
        +'order by review.average_rating DESC;'
    # movie, akas, review 테이블을 조인시키고 한국 영화이면서 리뷰가 10000이 넘는 영화를
    # 별점 높은순으로 정렬시킵니다.
    curs.execute(sql)
    row = curs.fetchone()
    while row:
        print("primary_title : %s region: %s num_votes : %d average_rating : %d" 
              %(row['primary_title'],row['region'],row['num_votes'], row['average_rating']))
        row = curs.fetchone()
    # 검색결과를 출력합니다. 제목과 지역, 리뷰 수, 별점 만 출력합니다.
    conn.commit()
    
            
conn = pymysql.connect(host  = 'localhost', user = 'root', password = '690501', db = 'imdb')
curs  = conn.cursor(pymysql.cursors.DictCursor)

while True: # 각각의 입력을 받을 입력 메뉴입니다. 
    
    print(' 1. 영화제목 기반 검색 ')
    print(' 2. 특정 배우 검색 ')
    print(' 3. 특정 감독 검색 ')
    print(' 4. Drama 장르 영화 검색 ')
    print(' 5. 5시즌 이상 방영한 프로그램 검색 ')
    print(' 6. 리뷰 만개 이상 한국 영화 검색 ')
    print(' 0. 종료 ')
    num = int(input('선택 : '))

    if num == 0: # 시스템 종료
        print(' 프로그램 종료 ')
        curs.close()
        conn.close()
        sys.exit()
        # 시스템 종료전 커서와 커넥션을 close 해줍니다. 
    elif num == 1: # 영화제목 검색
        fun1()
    elif num == 2: # 특정 배우 출연작 검색
        fun2()
    elif num == 3: # 특정 감독 검색
        fun3()
    elif num == 4: # Drama 장르 영화 검색z`
        fun4()
    elif num == 5: # 5시즌 이상 방영한 프로그램 검색
        fun5()
    elif num == 6: # 리뷰 만개 이상 한국상영 영화 검색
        fun6() 
    else: # 0~9 이외 선택인 경우 예외 처리를 합니다. 
        print('{}는 없는 번호'.format(num))

