```SQL
WITH ranked_names_per_decade AS (
    SELECT
        nome,
        COUNT(*) AS quantidade,
        CASE
            WHEN ano < 1960 THEN '1950s'
            WHEN ano < 1970 THEN '1960s'
            WHEN ano < 1980 THEN '1970s'
            WHEN ano < 1990 THEN '1980s'
            WHEN ano < 2000 THEN '1990s'
            WHEN ano < 2010 THEN '2000s'
            WHEN ano < 2020 THEN '2010s'
            ELSE '2020s'
        END AS decada,
        ROW_NUMBER() OVER(PARTITION BY
                              CASE
                                  WHEN ano < 1960 THEN '1950s'
                                  WHEN ano < 1970 THEN '1960s'
                                  WHEN ano < 1980 THEN '1970s'
                                  WHEN ano < 1990 THEN '1980s'
                                  WHEN ano < 2000 THEN '1990s'
                                  WHEN ano < 2010 THEN '2000s'
                                  WHEN ano < 2020 THEN '2010s'
                                  ELSE '2020s'
                              END
                          ORDER BY COUNT(*) DESC) AS ranking
    FROM 
        meubanco.pessoas
    WHERE 
        CAST(ano AS INTEGER) > 1950
    GROUP BY
        CASE
            WHEN ano < 1960 THEN '1950s'
            WHEN ano < 1970 THEN '1960s'
            WHEN ano < 1980 THEN '1970s'
            WHEN ano < 1990 THEN '1980s'
            WHEN ano < 2000 THEN '1990s'
            WHEN ano < 2010 THEN '2000s'
            WHEN ano < 2020 THEN '2010s'
            ELSE '2020s'
        END,
        nome
)
SELECT 
    decada,
    nome,
    quantidade
FROM 
    ranked_names_per_decade
WHERE 
    ranking <= 3
ORDER BY 
    decada,
    ranking;
```