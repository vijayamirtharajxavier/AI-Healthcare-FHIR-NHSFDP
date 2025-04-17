import requests

# Sample FHIR endpoint (HAPI FHIR public test server)
FHIR_BASE_URL = "https://hapi.fhir.org/baseR4"
RESOURCE = "Patient"

def fetch_fhir_resource(resource_type=RESOURCE, count=5):
    url = f"{FHIR_BASE_URL}/{resource_type}?_count={count}"
    print(f"Fetching {count} records from: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("Successfully fetched FHIR data:")
        for entry in data.get("entry", []):
            print(entry.get("resource", {}))
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_fhir_resource()
