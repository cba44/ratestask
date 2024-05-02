from app.utils import Utils
from app.db.query import RatesQuery

class RatesDb:

    def get_all_subregions(slug):
        conn = Utils.get_db_connection()
        cur = conn.cursor()
        cur.execute(RatesQuery.subregion_query, {'slug': slug})
        regions = []
        for region in cur.fetchall():
            regions.append(region[0])
        regions_tuple = tuple(regions)
        cur.close()
        conn.close()
        return regions_tuple
    
    def get_port_count(port):
        conn = Utils.get_db_connection()
        cur = conn.cursor()
        cur.execute(RatesQuery.port_count_query, {'port': port})
        port_count = cur.fetchone()[0]
        cur.close()
        conn.close()
        return port_count
    
    def get_all_ports(subregions):
        conn = Utils.get_db_connection()
        cur = conn.cursor()
        cur.execute(RatesQuery.subregion_ports_query, {'region': subregions})
        ports = []
        for port in cur.fetchall():
            ports.append(port[0])
        ports_tuple = tuple(ports)
        cur.close()
        conn.close()
        return ports_tuple

    def get_prices():
        pass