-- SQL Script that ranks country origins by the num of non-unique fans
SELECT
  origin AS origin,
  SUM(fans) AS nb_fans
FROM
  metal_bands
GROUP BY
  origin
ORDER BY
  nb_fans DESC;
