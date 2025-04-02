import requests
import csv

# Google Places API key
API_KEY = ""
LOCATION = "Leicester,UK"
SEARCH_TYPE = "car_repair"
RADIUS = 10000  # Search radius in meters
CSV_FILE = "repair.csv"

# Base URL for Google Places API
PLACES_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"

# Function to fetch places

def get_places():
    places = []
    params = {
        "key": API_KEY,
        "location": "52.6369,-1.1398",  # Leicester coordinates
        "radius": RADIUS,
        "type": SEARCH_TYPE
    }
    
    while True:
        response = requests.get(PLACES_URL, params=params)
        data = response.json()
        
        if "results" in data:
            places.extend(data["results"])
        
        # Check if there is another page of results
        if "next_page_token" in data:
            params["pagetoken"] = data["next_page_token"]
        else:
            break
    
    return places

# Function to fetch details of each place
def get_place_details(place_id):
    params = {
        "key": API_KEY,
        "place_id": place_id,
        "fields": "name,formatted_address,formatted_phone_number,rating,website"
    }
    
    response = requests.get(DETAILS_URL, params=params)
    return response.json().get("result", {})

# Main function
def main():
    places = get_places()
    
    # Extract details
    data = []
    for place in places:
        details = get_place_details(place["place_id"])
        data.append([
            details.get("name", "N/A"),
            details.get("formatted_address", "N/A"),
            details.get("formatted_phone_number", "N/A"),
            details.get("rating", "N/A"),
            details.get("website", "N/A")
        ])
    
    # Save to CSV
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Address", "Phone", "Rating", "Website"])
        writer.writerows(data)
    
    print(f"Data saved to {CSV_FILE}")

if __name__ == "__main__":
    main()
