from app.db.rates import RatesDb

class RatesService:

    def get_prices(date_from, date_to, origin, destination):
        origin_ports = RatesService.get_ports(origin)
        destination_ports = RatesService.get_ports(destination)
        return origin_ports
    
    def get_ports(location):
        ports = []

        # Check if it's a single port or a region
        if len(location) == 5 and RatesDb.get_port_count(location) == 1:
            ports = (location,)
        else:
            subregions = RatesDb.get_all_subregions(location)
            ports = RatesDb.get_all_ports(subregions)

        return ports
    
