from app.utils import Utils
from app.db.query import RatesQuery

class RatesDb:

    def get_all_subregions(slug, location_name):
        conn = Utils.get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute(RatesQuery.subregion_query, {'slug': slug})
        except:
            raise ValueError(f"Invalid region name for {location_name}")
        regions = []
        for region in cur.fetchall():
            regions.append(region[0])
        regions_tuple = tuple(regions)
        cur.close()
        conn.close()
        return regions_tuple
    
    def get_port_count(port, location_name):
        conn = Utils.get_db_connection()
        cur = conn.cursor()

        try:
            cur.execute(RatesQuery.port_count_query, {'port': port})
        except:
            raise ValueError(f"Invalid port name for {location_name}")

        port_count = cur.fetchone()[0]
        cur.close()
        conn.close()
        return port_count
    
    def get_all_ports(subregions, location_name):
        conn = Utils.get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute(RatesQuery.subregion_ports_query, {'region': subregions})
        except:
            raise ValueError(f"Invalid region name for {location_name}")
        ports = []
        for port in cur.fetchall():
            ports.append(port[0])
        ports_tuple = tuple(ports)
        cur.close()
        conn.close()
        return ports_tuple

    def get_prices(date_from, date_to, origin_ports, destination_ports):
        conn = Utils.get_db_connection()
        cur = conn.cursor()
        cur.execute(RatesQuery.prices_query, {'orig_codes': origin_ports,
                                              'dest_codes': destination_ports,
                                              'start_day': date_from,
                                              'end_day': date_to})
        prices = cur.fetchall()
        cur.close()
        conn.close()
        return prices