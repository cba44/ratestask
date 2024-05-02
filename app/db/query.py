class RatesQuery:

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