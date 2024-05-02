from app.utils import Utils
from app.db.query import RatesQuery

class RatesDb:

    def get_all_subregions(slug, location_name):
        conn = Utils.get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute(RatesQuery.subregion_query, {'slug': slug})
            regions = []
            for region in cur.fetchall():
                regions.append(region[0])
            regions_tuple = tuple(regions)
            return regions_tuple
        except:
            raise ValueError(f"Invalid region name for {location_name}")
        finally:
            cur.close()
            conn.close()
        
    
    def get_port_count(port, location_name):
        conn = Utils.get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute(RatesQuery.port_count_query, {'port': port})
            port_count = cur.fetchone()[0]
            return port_count
        except:
            raise ValueError(f"Invalid port name for {location_name}")
        finally:
            cur.close()
            conn.close()
        
    
    def get_all_ports(subregions, location_name):
        conn = Utils.get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute(RatesQuery.subregion_ports_query, {'region': subregions})
            ports = []
            for port in cur.fetchall():
                ports.append(port[0])
            ports_tuple = tuple(ports)
            return ports_tuple
        except:
            raise ValueError(f"Invalid region name for {location_name}")
        finally:
            cur.close()
            conn.close()
        

    def get_prices(date_from, date_to, origin_ports, destination_ports):
        conn = Utils.get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute(RatesQuery.prices_query, {'orig_codes': origin_ports,
                                              'dest_codes': destination_ports,
                                              'start_day': date_from,
                                              'end_day': date_to})
            prices = cur.fetchall()
            return prices
        except:
            raise ValueError("Invalid value entered")
        finally:
            cur.close()
            conn.close()
        