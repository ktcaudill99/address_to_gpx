import time
import os
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
from geopy.geocoders import Nominatim

def format_address(address):
    # This function will format the address as per your requirements.
    # Currently, it just strips extra spaces and returns the address.
    # You can add more formatting rules if needed.
    return address.strip()

def geocode_addresses(addresses):
    geolocator = Nominatim(user_agent="geoapiExercises")

    error_addresses = []
    successful_coordinates = []

    for address in addresses:
        try:
            location = geolocator.geocode(address, timeout=10)  # Increase timeout to 10 seconds
            if location:
                print(f"Address: {address}")
                print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
                successful_coordinates.append((address, location.latitude, location.longitude))
            else:
                error_addresses.append(address)
        except (GeocoderTimedOut, GeocoderUnavailable):
            error_addresses.append(address)
            time.sleep(1)  # Wait for 1 second before retrying the next address
            continue
        time.sleep(.001)  # Introduce a delay of 1 millisecond between requests

    return successful_coordinates, error_addresses

def generate_gpx_file(successful_coordinates, filename="addresses.gpx"):
    with open(filename, "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<gpx version="1.1" creator="ChatGPT" xmlns="http://www.topografix.com/GPX/1/1">\n')
        for address, lat, lon in successful_coordinates:
            f.write(f'  <wpt lat="{lat}" lon="{lon}">\n')
            f.write(f'    <name>{address}</name>\n')
            f.write(f'    <desc>{address}</desc>\n')
            f.write('  </wpt>\n')
        f.write('</gpx>\n')

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_filename = os.path.join(script_dir, "addresses.txt")
    
    with open(input_filename, 'r') as f:
        addresses = [format_address(addr.strip()) for addr in f.readlines()]

    successful_coordinates, error_addresses = geocode_addresses(addresses)

    # Print addresses with errors
    if error_addresses:
        print("\nAddresses with Errors:")
        for err_address in error_addresses:
            print(err_address)

    # Generate the GPX file
    generate_gpx_file(successful_coordinates)