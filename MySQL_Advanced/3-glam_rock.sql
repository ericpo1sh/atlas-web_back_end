-- Write a SQL script that lists all bands with Glam rock as their main style
-- ranked by their longevity
SELECT
  band_name,
  formed - split AS lifespan,
  style
FROM
  metal_bands
WHERE
  style LIKE '%Glam rock%'
GROUP BY
  band_name
ORDER BY
  lifespan DESC;
