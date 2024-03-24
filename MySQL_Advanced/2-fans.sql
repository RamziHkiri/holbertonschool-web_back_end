-- SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT origin AS origin, SUM(fans) as nb_fans
From metal_bands ORDER BY nb_fans DESC;