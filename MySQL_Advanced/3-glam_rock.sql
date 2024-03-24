-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, YEAR(COALESCE(split, CURDATE())) - YEAR(formed) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
