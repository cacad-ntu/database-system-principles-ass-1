DROP VIEW IF EXISTS collaborators;

CREATE VIEW collaborators AS(
    SELECT  a.author as author, count(a.author) as cnt
    FROM    pub_auth a, pub_auth b
    WHERE   a.author <> b.author AND 
            a.pub_key = b.pub_key AND
            a.pub_key IN (
                SELECT  pub_key
                FROM    publication
                WHERE   (pub_class = 'inproceedings' OR pub_class = 'article') AND
                        lower(title) LIKE '%data%' 
            )
    GROUP BY a.author
);

SELECT author, cnt
FROM collaborators
WHERE cnt = (
    SELECT MAX(cnt)
    FROM collaborators
);
