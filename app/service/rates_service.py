from app.db.rates import RatesDb

class RatesService:

    def get_prices(date_from, date_to, origin, destination):
        price_list = []
        origin_ports = RatesService.get_ports(origin)
        destination_ports = RatesService.get_ports(destination)
        prices = RatesDb.get_prices(date_from, date_to, origin_ports, destination_ports)
        for price in prices:
            price_list.append({
                "day": price[0].strftime("%Y-%m-%d"),
                "average_price": price[1]
            })
        return price_list
    
    def get_ports(location):
        ports = []

        # Check if it's a single port or a region
        if len(location) == 5 and RatesDb.get_port_count(location) == 1:
            ports = (location,)
        else:
            subregions = RatesDb.get_all_subregions(location)
            ports = RatesDb.get_all_ports(subregions)

        return ports
    
