DROP TABLE author;
DROP TABLE pub_auth;
DROP TABLE publication;
DROP TABLE article;
DROP TABLE book;
DROP TABLE incollection;
DROP TABLE proceedings;
DROP TABLE inproceedings;

CREATE TABLE author(
    name VARCHAR(500) PRIMARY KEY,
    last_name VARCHAR(100)
);

CREATE TABLE pub_auth(
    pub_key VARCHAR(100),
    author VARCHAR(500),
    PRIMARY KEY(pub_key, author)
);

CREATE TABLE publication(
    pub_key VARCHAR(100) PRIMARY KEY,
    pub_class VARCHAR(100),
    pub_type VARCHAR(100),
    title_abbrev VARCHAR(100),
    title VARCHAR(1000),
    year INTEGER,
    month INTEGER
);

CREATE TABLE article(
    pub_key VARCHAR(100) PRIMARY KEY,
    volume VARCHAR(100),
    journal VARCHAR(500),
    number VARCHAR(100)
);

CREATE TABLE book(
    pub_key VARCHAR(100) PRIMARY KEY,
    publisher VARCHAR(500),
    series VARCHAR(100),
    volume VARCHAR(100)
);

CREATE TABLE incollection(
    pub_key VARCHAR(100) PRIMARY KEY,
    booktitle VARCHAR(500)
);

CREATE TABLE proceedings(
    pub_key VARCHAR(100) PRIMARY KEY,
    booktitle VARCHAR(500),
    publisher VARCHAR(500)
);

CREATE TABLE inproceedings(
    pub_key VARCHAR(100) PRIMARY KEY,
    booktitle VARCHAR(500)
);