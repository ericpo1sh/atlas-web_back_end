-- Write a SQL script that lists all bands with Glam rock as their main style
-- ranked by their longevity
SELECT
  band_name AS band_name,
  formed - split AS lifespan,
  style AS style
FROM
  metal_bands
WHERE
  style="Glam rock"
GROUP BY
  band_name
ORDER BY
  lifespan DESC;
