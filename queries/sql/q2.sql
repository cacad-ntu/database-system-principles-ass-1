    
    SELECT      DISTINCT upper(t.title_abbrev)
    FROM        (
                SELECT      p.title_abbrev, p.year, count(p.title_abbrev) as cnt
                FROM        publication as p
                WHERE       p.pub_class = 'inproceedings' AND 
                            p.month = 7
                GROUP BY    p.title_abbrev, p.year
                ) as t
    WHERE t.cnt > 200