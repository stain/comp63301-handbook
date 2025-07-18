---
title: Extra challenges (optional)
weight: 11
---


> [!primary] Objectives
> - Extra challenges to practice creating SQL queries.

> [!secondary] Questions
> - Are there extra challenges to practice translating plain English queries to SQL queries?



## Extra challenges (optional)

SQL queries help us *ask* specific *questions* which we want to answer about our data. The real skill with SQL is to know how to translate our questions into a sensible SQL queries (and subsequently visualise and interpret our results).

Have a look at the following questions; these questions are written in plain English. Can you translate them to *SQL queries* and give a suitable answer?

Also, if you would like to learn more SQL concepts and try additional challenges, see the [Software Carpentry Databases and SQL](https://swcarpentry.github.io/sql-novice-survey/) lesson.



> [!note]- Challenge 1
> > [!accent] 
> > How many `articles` are there from each `First_author`? Can you make an alias for the number of articles? Can you order the results by articles?
>
> > [!INFO]- Solution 1
> > ```sql
> > SELECT First_Author, COUNT(*) AS n_articles
> > FROM articles
> > GROUP BY First_Author
> > ORDER BY n_articles DESC;
> > ```



> [!note]- Challenge 2
> > [!accent] 
> > How many papers have a single author? How many have 2 authors? How many 3? etc?
>
> > [!INFO]- Solution 2
> > ```sql
> > SELECT Author_Count, COUNT(*)
> > FROM articles
> > GROUP BY Author_Count;
> > ```


> [!note]- Challenge 3
> > [!accent] 
> >  How many articles are published for each `Language`? Ignore articles where language is unknown.
>
> > [!INFO]- Solution 3
> > ```sql
> > SELECT Language, COUNT(*)
> > FROM articles
> > JOIN languages
> > ON articles.LanguageId = languages.id
> > WHERE Language != ''
> > GROUP BY Language;
> > ```





> [!note]- Challenge 4
> > [!accent] 
> > How many articles are published for each `Licence` type, and what is the average number of citations for that `Licence` type?
>
> > [!INFO]- Solution 4
> > ```sql
> > SELECT Licence, AVG(Citation_Count), COUNT(*)
> > FROM articles
> > JOIN licences
> > ON articles.LicenceId = licences.id
> > WHERE Licence != ''
> > GROUP BY Licence;
> > ```


> [!note]- Challenge 5
> > [!accent] 
> >  Write a query that returns `Title, First_Author, Author_Count, Citation_Count, Month, Year, Journal_Title and Publisher` for articles in the database.
>
> > [!INFO]- Solution 5
> > ```sql
> > SELECT Title, First_Author, Author_Count, Citation_Count,
> >        Month, Year, Journal_Title, Publisher
> > FROM articles
> > JOIN journals
> > ON articles.issns = journals.ISSNs
> > JOIN publishers
> > ON publishers.id = journals.PublisherId;
> > ```



> [!TIP] Keypoints
> - It takes time and practice to learn how to translate plain English queries into SQL queries.



