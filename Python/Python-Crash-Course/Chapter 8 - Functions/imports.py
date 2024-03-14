def make_car(manufacturer, model, **car_info):
    """Make a dictionary of cars, contains manufacture, model, and other info"""
    car_info['manfacturer'] = manufacturer
    car_info['model'] = model
    return car_info