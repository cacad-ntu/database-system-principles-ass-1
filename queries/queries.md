# Queries

## Query 1

```sql
SELECT      publication_type, COUNT(*) AS Total
FROM        publication 
WHERE       pub_year < 2018 AND pub_year > 1999
GROUP BY    publication_type
```

## Query 2

```sql
SELECT      DISTINCT conf_name
FROM        (
            SELECT      conf_name, pub_year
            FROM        publication
            WHERE       publication_type = inproceedings AND 
                        publication_month = 7
            GROUP BY    conf_name, pub_year
            )
WHERE       COUNT(DISTINCT conf_name) > 200
GROUP BY    pub_year
```

## Query 3(a)

```sql
SELECT      *
FROM        (
            SELECT      pid as pid
            FROM        authored, author
            WHERE       author.name = X and 
                        authored.aid = author.id
            ), publication
WHERE       year = 2015 and 
            publication.pub_id == pid
```

## Query 3(b)

```sql
SELECT      *
FROM        (
            SELECT      pid as pid
            FROM        authored, author
            WHERE       author.name = X and 
                        authored.aid = author.id
            ), publication
WHERE       year = Y and 
            name = Z and
            publication.pub_id = pid
```
## Query 3(c)

```sql
SELECT      author.name
FROM        (
            SELECT      pid as pid, author.name
            FROM        authored, author
            WHERE       authored.aid = author.id
            ), publication
WHERE       year = Y and 
            name = Z and 
            COUNT(pid) > 2
GROUP BY    author.name    

```

## Query 4(a)

```sql
DROP VIEW IF EXISTS PVLDB;
DROP VIEW IF EXISTS SIGMOD;
DROP VIEW IF EXISTS PVLDB_SIGMOD;
CREATE VIEW PVLDB AS(
    SELECT      authored.aid
    FROM        authored
    JOIN        publication ON authored.pid = publication.pub_id
    WHERE       publication.name = "PVLDB"
    GROUP BY    aid
    HAVING      COUNT(aid) >= 10
);

CREATE VIEW SIGMOD AS(
    SELECT      authored.aid
    FROM        authored
    JOIN        publication ON authored.pid = publication.pub_id
    WHERE       publication.name = "SIGMOD"
    GROUP BY    aid
    HAVING      COUNT(aid) >= 10
);

CREATE VIEW PVLDB_SIGMOD AS(
    SELECT aid FROM PVLDB
    INTERSECT
    SELECT aid FROM SIGMOD
);

SELECT  name
FROM    author join PVLDB_SIGMOD ON (author.aid = PVLDB_SIGMOD.aid);
```

## Query 4(b)

```sql
DROP VIEW IF EXISTS PVLDB;
DROP VIEW IF EXISTS KDD;
DROP VIEW IF EXISTS PVLDB_KDD;

CREATE VIEW PVLDB AS(
    SELECT      authored.aid
    FROM        authored
    JOIN        publication ON authored.pid = publication.pub_id
    WHERE       publication.name = "PVLDB"
    GROUP BY    aid
    HAVING      COUNT(aid) >= 15
);

CREATE VIEW KDD AS(
    SELECT      DISTINCT authored.aid
    FROM        authored
    JOIN        publication ON authored.pid = publication.pub_id
    WHERE       publication.name = "KDD"
);

CREATE VIEW PVLDB_KDD AS(
    SELECT aid FROM PVLDB
    EXCEPT
    SELECT aid FROM KDD
);

SELECT name
FROM author join PVLDB_KDD ON (author.aid = PVLDB_KDD.aid);
```

## Query 5
```sql
DROP VIEW IF EXISTS year7079 CASCADE;
DROP VIEW IF EXISTS year8089 CASCADE;
DROP VIEW IF EXISTS year9099 CASCADE;
DROP VIEW IF EXISTS year0009 CASCADE;
DROP VIEW IF EXISTS year1019 CASCADE;

CREATE VIEW year7079 AS(
    SELECT  pub_id
    FROM    publication
    WHERE   year >=1970 and 
            year <=1979 and 
            publication.type = "inproceedings"
);

CREATE VIEW year8089 AS(
    SELECT  pub_id
    FROM    publication
    WHERE   year >=1980 and 
            year <=1989 and 
            publication.type = "inproceedings"
);

CREATE VIEW year9099 AS(
    SELECT  pub_id
    FROM    publication
    WHERE   year >=1990 and 
            year <=1999 and 
            publication.type = "inproceedings"
);

CREATE VIEW year0009 AS(
    SELECT  pub_id
    FROM    publication
    WHERE   year >=2000 and 
            year <=2009 and 
            publication.type = "inproceedings"
);

CREATE VIEW year1019 AS(
    SELECT  pub_id
    FROM    publication
    WHERE   year >=2010 and 
            year <=2019 and 
            publication.type = "inproceedings"
);
```

## Query 6

```sql
DROP VIEW IF EXISTS collaborators CASCADE;
DROP VIEW IF EXISTS title_containing_data CASCADE;

CREATE VIEW data_containing_data AS (
    SELECT  pub_id
    FROM    publication
    WHERE   (pub_type = inproceeding OR pub_type = article) AND
            title LIKE '%Data%'
)

CREATE VIEW collaborators AS(
    SELECT  DISTINCT a.aid, b.aid
    FROM    authored a, authored b, title_containing_data
    WHERE   NOT a.aid = b.aid AND 
            a.pub_id = b.pub_id AND
            a.pub.id = title_containing_data.pub_id)
);

SELECT      a.aid
FROM        collaborators 
WHERE       MAX(COUNT(b.aid) as Colab)
GROUP BY    a.aid
```

## Query 7

```sql
DROP VIEW IF EXISTS title_containing_data CASCADE;
DROP VIEW IF EXISTS author_list CASCADE;

CREATE VIEW title_containing_data AS (
    SELECT  pub_id
    FROM    publication
    WHERE   (pub_type = inproceeding OR pub_type = article) AND
            title LIKE '%Data%' AND
            year > 2011
)

CREATE VIEW author_list AS (
    SELECT      author.author_name, count(author.aid) as count
    FROM        title_containing_data, authored, author
    WHERE       authored.pid = title_containing_data.pid AND   
                authored.aid = author.aid
    ORDER BY    count DESC
)

SELECT      DISTINCT top 10 
FROM        author_list
```

## Query 8

```sql
DROP VIEW IF EXISTS inproceeding_6_year CASCADE;

CREATE VIEW inproceeding_6_year AS (
SELECT      pub_name, year 
FROM        publication
WHERE       pub_type = inproceeding AND
            m_date = 6
GROUP BY    year
)

SELECT      pub_name 
FROM        inproceeding_6_year
WHERE       count(DISTINCT pub_name) > 100
GROUP BY    
```

## Query 9

```sql
```

## Query 10

```sql
```
