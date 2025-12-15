SELECT DISTINCT author
FROM books
WHERE genre = 'Fiction'
GROUP BY author
HAVING AVG(user_rating) >= 4.5
  AND AVG(reviews) >= ALL(SELECT AVG(reviews) FROM books WHERE genre = 'Fiction')
  AND COUNT(*) > 1
ORDER BY author ASC;