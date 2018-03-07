# Logs Analysis Project

by Igor Oliveira


## Introduction

This code is part of the Udacity Full Stack Web Developer Nanodegree. The project consists on analysis of a given website log database.

The database have 3 tables:
* The `authors` table includes information about the authors of articles.
* The `articles` table includes the articles themselves.
* The `log` table includes one entry for each time a user has accessed the site.

This project implements a single query solution for each of the question in hand.
See [main.py](main.py) for more details.

Three questions should be answered using SQL queries:

1) What are the most popular three articles of all time?
2) Who are the most popular article authors of all time?
3) On which days dis more than 1% of requests lead to errors?

## Requirements

Using the starter code provided by Udacity, create and populate de database with:

```sh
psql -d news -f newsdata.sql
```


## How to Run

```sh
python3 log_analysis.py
```

An example `output` file is provided