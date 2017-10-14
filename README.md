# DBLP Publication Processor

CZ4031 - Database Assignment 1: Querying Databases Efficiently

## Getting Started

### Requirements

- Python 3.6 or above (with pip)
- Postgresql 9.6.5 or above

### Usages

- Install [requirement](requirements.txt) for python library (`pip install -r requirement.txt`)
- Download [dblp.xml](http://dblp.uni-trier.de/xml/) and place it under `scripts/data/`
- [Drop](queries/drop_tables.sql) and [Create](queries/create_tables.sql) tables for publications
- Change [setting](scripts/config.json) for xml parser
- Move to `scripts/`, and run `python start.py`.

## Content

The following are the content of this repository

### Scripts

Contain an xml parser that used to parse [dblp.xml](http://dblp.uni-trier.de/xml/) and stored it in postgresql.

### Queries

Contain the queries that needed for the assignment. Including:

- [Drop](queries/drop_tables.sql) and [Create](queries/create_tables.sql) tables
- Queries to answer question from assignment
- Queries to create index (for optimization)

### Reports

- Schema Design and Data Acquisition
  - E/R Diagram
  - Commands to Create Table
  - Codes to Parse XML
- Queries and Optimizing Queries
  - SQL Queries
  - Result on Full, Half and Quarter Data
  - Figures and Analysis
- Build Index and Study the Effect of Index
  - Create Index Statements
  - Analysis on Performance after and before Index
- Advance Part: Study the Effect of Cache
  - Analysis on The Effect of Cache Size on The Performance