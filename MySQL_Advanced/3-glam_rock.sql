-- Write a SQL script that lists all bands with Glam rock as their main style
-- ranked by their longevity
SELECT DISTINCT
  band_name,
  formed - split AS lifespan,
FROM
  metal_bands
WHERE
  style LIKE '%Glam rock%'
ORDER BY
  lifespan DESC;
