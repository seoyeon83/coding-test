SELECT artists.name AS artist, artworks.title AS title
FROM artworks_artists aa
JOIN artists ON aa.artist_id = artists.artist_id
JOIN artworks ON aa.artwork_id = artworks.artwork_id
WHERE artists.nationality = 'Korean'
  AND artworks.classification LIKE 'Film%';