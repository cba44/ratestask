class RatesQuery:

    # Recursive query to get all subregions of a given region
    subregion_query = '''
                WITH RECURSIVE subregions AS (
                SELECT slug 
                FROM regions 
                WHERE slug = %(slug)s
                UNION 
                SELECT r.slug
                FROM regions r
                INNER JOIN subregions s ON s.slug = r.parent_slug
                )
                SELECT * FROM subregions;
                '''
    
    port_count_query = 'SELECT count(*) from ports WHERE code = %(port)s'

    subregion_ports_query = 'SELECT code FROM ports WHERE parent_slug IN %(region)s'

    # Getting all prices for a day between ports/regions
    # Then the result is joined with a date range betweeen given dates
    # Result will give the null value when there is less than 3 price values for a day
    prices_query = '''
                select d.day, p.average_price from
                (SELECT day, ROUND(AVG(price)) as average_price
                FROM prices
                WHERE orig_code IN %(orig_codes)s
                AND
                dest_code in %(dest_codes)s
                AND
                day BETWEEN %(start_day)s AND %(end_day)s
                GROUP BY day
                HAVING COUNT(day) > 2) p

                RIGHT JOIN

                (SELECT t.day::DATE
                FROM generate_series(timestamp %(start_day)s,
                timestamp %(end_day)s,
                INTERVAL '1 day')
                AS t(day)) d

                ON p.day = d.day;
                '''