from app.db.rates import RatesDb

class RatesService:

    def get_prices(date_from, date_to, origin, destination):
        price_list = []
        origin_ports = RatesService.get_ports(origin, "origin")
        destination_ports = RatesService.get_ports(destination, "destination")
        prices = RatesDb.get_prices(date_from, date_to, origin_ports, destination_ports)
        for price in prices:
            price_list.append({
                "day": price[0].strftime("%Y-%m-%d"),
                "average_price": price[1]
            })
        return price_list
    
    def get_ports(location, location_name):
        ports = []

        # Check if it's a single port or a region
        if len(location) == 5:
            port_count = -1
            port_count = RatesDb.get_port_count(location, location_name)

            if port_count == 1:
                ports = (location,)
                return ports
        
        subregions = RatesDb.get_all_subregions(location, location_name)
        ports = RatesDb.get_all_ports(subregions, location_name)

        return ports
    
