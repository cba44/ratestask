from app.utils import Utils

class RatesDb:

    subregion_query = '''
        WITH RECURSIVE subregions AS (
        SELECT slug, name, parent_slug 
        FROM regions 
        WHERE slug = %(slug)s
        UNION 
        SELECT r.slug, r.name, r.parent_slug 
        FROM regions r
        INNER JOIN subregions s ON s.slug = r.parent_slug
        )
        SELECT * FROM subregions;
        '''

    def get_all_subregions(slug):
        conn = Utils.get_db_connection()
        cur = conn.cursor()
        print(RatesDb.subregion_query)
        cur.execute(RatesDb.subregion_query, {'slug': slug})
        regions = cur.fetchall()
        cur.close()
        conn.close()
        return regions