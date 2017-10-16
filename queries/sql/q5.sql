DROP VIEW IF EXISTS year7079 ;
DROP VIEW IF EXISTS year8089 ;
DROP VIEW IF EXISTS year9099 ;
DROP VIEW IF EXISTS year0009 ;
DROP VIEW IF EXISTS year1019 ;

CREATE VIEW year7079 AS(
    SELECT  count(pub_key) as cnt
    FROM    publication
    WHERE   year >=1970 and 
            year <=1979 and 
            pub_class = 'inproceedings'
);

CREATE VIEW year8089 AS(
    SELECT  count(pub_key) as cnt
    FROM    publication
    WHERE   year >=1980 and 
            year <=1989 and 
            pub_class = 'inproceedings'
);

CREATE VIEW year9099 AS(
    SELECT  count(pub_key) as cnt
    FROM    publication
    WHERE   year >=1990 and 
            year <=1999 and 
            pub_class = 'inproceedings'
);

CREATE VIEW year0009 AS(
    SELECT  count(pub_key) as cnt
    FROM    publication
    WHERE   year >=2000 and 
            year <=2009 and 
            pub_class = 'inproceedings'
);

CREATE VIEW year1019 AS(
    SELECT  count(pub_key) as cnt
    FROM    publication
    WHERE   year >=2010 and 
            year <=2019 and 
            pub_class = 'inproceedings'
);

SELECT  
    year7079.cnt as yr7079, 
    year8089.cnt as yr8089, 
    year9099.cnt as yr9099, 
    year0009.cnt as yr0009, 
    year1019.cnt as yr1019
FROM    year7079, year8089, year9099, year0009, year1019;
