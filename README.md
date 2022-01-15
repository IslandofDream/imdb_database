# **◎프로젝트 설명**

본 프로젝트는 데이터베이스를 이용한 프로젝트입니다. 인터넷 영화 데이터베이스 (IMDB)에서 제공하는 tsv 형태의 파일들을 자신만의 기준을 통해서 데이터분석을 하고 E-R모델링, 관계형 테이블 분석까지 합니다. 이후 python과 MySql을 통해서 인터넷 영화 데이터베이스 (IMDB)의 데이터베이스를 쿼리들을 통해서 직접 데이터베스 관리하는 프로그램을 구현하였습니다.

# **◎ 인터넷 영화 데이터베이스 (IMDB) 데이터 분석**

IMDB에서 제공하는 tsv파일의 데이터를 다음과 같이 분석하였습니다.

따라서 다음과 같은 형태로 tsv의 파일들의 어트리뷰트를 파악하고 tsv들을 테이블화 할 수 있었습니다.

![episodes](https://user-images.githubusercontent.com/70648111/149606464-b837b38e-cd3c-4167-8d10-c1cf89700117.png)

![ratings](https://user-images.githubusercontent.com/70648111/149606468-8493e8ff-2f41-4ce5-aa9a-a2e6d779340e.png)

![title basic](https://user-images.githubusercontent.com/70648111/149606469-67f90db0-4955-4475-ac11-885542237c16.png)

![akas](https://user-images.githubusercontent.com/70648111/149606473-3e610f16-3d25-4a08-8858-72ec6901aae2.png)

![crew](https://user-images.githubusercontent.com/70648111/149606443-ed671d40-4ca5-4604-8cf7-0b285e09e1eb.png)

![principals](https://user-images.githubusercontent.com/70648111/149606467-4996dfcc-ee93-4deb-af8d-2a816ef4bb26.png)

![crew](https://user-images.githubusercontent.com/70648111/149606443-ed671d40-4ca5-4604-8cf7-0b285e09e1eb.png)

# **◎E-R 모델링**

위에서 한 데이터분석을 바탕으로 다음과 같은 E-R모델링을 실시하였습니다. 기본적으로 tsv파일을 그대로 한 테이블로 사용하는 것이 아닌 원활한 기본키, 외래키 사용을 위해서 다음과 같은 형태로 구성하였습니다.

![E-R모델링](https://user-images.githubusercontent.com/70648111/149606465-0d806e7c-8d67-41a9-a195-25c37af6ff6f.png)

# **◎관계형 데이터베이스 테이블 설계**

E-R 모델링을 기반으로 관계형 테이블을 다음과 같이 설계 하였습니다. Directors, Writers테이블과 같이 원활한 join관계 설정을 위하여 기본키 없이 외래키만 사용하는 테이블들도 일부 사용하였습니다

![관계형테이블](https://user-images.githubusercontent.com/70648111/149606471-81ee9497-7ce9-43d1-8188-1ed749e85d19.png)

# **◎인덱스 적용**

Sql을 통해서 데이터를 검색 및 관리 할 때, 적절한 부분에 인덱스를 적용하면 더 빠른 검색 속도를 보장 할 수 있습니다. 따라서 일부 테이블의 빨간색 글씨의 필드에 인덱스를 적용 하였습니다. 또한 인덱스를 사용하였을 때와 사용하지 않았을 때의 속도차이 또한 정리하였습니다.

![인덱스 적용](https://user-images.githubusercontent.com/70648111/149606472-4a7c56fd-0bff-454b-bf5b-06323d154d41.png)

![인덱스속도](https://user-images.githubusercontent.com/70648111/149606521-da642888-b6e7-4546-ad24-147a9e670f7f.png)

# **◎실행 결과**

## mysql workbench

![db1](https://user-images.githubusercontent.com/70648111/149606444-e09f79f9-1199-4d3e-b2bd-ae0d768f9a7a.gif)

![db2](https://user-images.githubusercontent.com/70648111/149606445-35dffd62-576f-44be-ba5b-a20753d8498d.gif)

## python을 이용한 mysql연결

![db3](https://user-images.githubusercontent.com/70648111/149606450-15f5002c-b1af-4320-92c2-9bc4f8ade9e5.gif)

![db4](https://user-images.githubusercontent.com/70648111/149606453-fba4052c-8012-471d-af46-60102b12fd19.gif)

![db5.gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7b5e1bc3-93b9-4202-982d-05f60a58b5b3/db5.gif)
