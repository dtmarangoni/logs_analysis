-- Author, Article and grouped Log table are joined to make it easier to
-- answer the first and second report questions.

CREATE VIEW author_article_log AS
SELECT articles.title, authors.name, views
FROM articles JOIN (
    SELECT path, COUNT(*) AS views
    FROM log
    GROUP BY log.path
    ) AS log_view
    ON '/article/' || articles.slug = log_view.path
    JOIN authors
    ON articles.author = authors.id;