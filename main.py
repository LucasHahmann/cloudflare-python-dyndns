# Imports
import os
from cloudflare import Cloudflare
from dotenv import load_dotenv
from requests import get

# Function to retrieve public IPv4 address
def get_public_ipv4():
    ip_v4 = get('https://api.ipify.org').content.decode('utf8')
    return ip_v4

# Function to set the dynamic DNS record in Cloudflare
def set_dyndns_record(client, new_public_ip):
    response = client.dns.records.edit(
        zone_id=zone_id,
        dns_record_id=record_id,
        name=record_name,
        content=new_public_ip,
        type="A"
    )
    return response

# Load environment variables from .env file
load_dotenv()

# Retrieve required environment variables
api_token = os.environ.get("CLOUDFLARE_API_TOKEN")
if not api_token:
    raise ValueError("Cloudflare API token is not set in environment variables.")

zone_id = os.environ.get("CLOUDFLARE_ZONE_ID")
record_name = os.environ.get("CLOUDFLARE_DNS_RECORD_NAME")
record_id = os.environ.get("CLOUDFLARE_DNS_RECORD_ID")

# Set the headers for Cloudflare API request
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

# Main execution
if __name__ == "__main__":
    # Initialize Cloudflare client with the API token and headers
    client = Cloudflare(default_headers=headers)

    # Get the current DNS record for dynamic DNS
    dyndns_record = client.dns.records.get(
        dns_record_id=record_id,
        zone_id=zone_id
    )

    # Retrieve the current public IP address
    public_ip = get_public_ipv4()

    # Check if the current public IP matches the existing DNS record
    if public_ip == dyndns_record.content:
        # Exit if the IP addresses are the same
        exit()
    else:
        # Update the DNS record with the new public IP
        set_dyndns_record(client, public_ip)