DROP INDEX IF EXISTS pub_year_idx;
DROP INDEX IF EXISTS pub_month_idx;
DROP INDEX IF EXISTS pub_class_idx;
DROP INDEX IF EXISTS pub_title_abbrev_idx;
DROP INDEX IF EXISTS pub_type_idx;
DROP INDEX IF EXISTS pub_title_idx;

DROP INDEX IF EXISTS pub_auth_author_idx;

DROP INDEX IF EXISTS pro_booktitle_idx;

DROP INDEX IF EXISTS inpro_booktitle_idx;

DROP INDEX IF EXISTS author_last_name_idx;


CREATE INDEX pub_year_idx ON publication (year);
CREATE INDEX pub_month_idx ON publication (month);
CREATE INDEX pub_class_idx ON publication (pub_class);
CREATE INDEX pub_title_abbrev_idx ON publication (title_abbrev);
CREATE INDEX pub_type_idx ON publication (pub_type);
CREATE INDEX pub_title_idx ON publication (title);

CREATE INDEX pub_auth_author_idx ON pub_auth (author);

CREATE INDEX pro_booktitle_idx ON proceedings (booktitle);

CREATE INDEX inpro_booktitle_idx ON inproceedings (booktitle);

CREATE INDEX author_last_name_idx ON author (last_name);