# Cloudflare Python DynDNS

This script provides a way to implement a self-hosted Dynamic DNS (DynDNS) service that automatically updates your Cloudflare DNS record with your current public IP address whenever it changes.

## Setup

1. **Create a Subdomain**: Set up a subdomain like `dyndns.your-domain.com` in your Cloudflare account. All other DNS records should be `CNAME` records that resolve to `dyndns.your-domain.com`.

2. **Retrieve Cloudflare Details**: In your Cloudflare dashboard, find the following details for the subdomain you created:
    - **Zone ID**
    - **DNS Record Name**
    - **DNS Record ID**

   Set these values in the script configuration.

3. **How It Works**: The script checks your current public IP address. If it has changed, it updates the DNS record for `dyndns.your-domain.com` to reflect the new IP address.

## Deployment

### Step 1: Create Virtual Environment

```bash
python3 -m venv /opt/cloudflare-python-dyndns/venv
/opt/cloudflare-python-dyndns/venv/bin/activate
```

### Step 2: Install Dependencies

Clone the repository and install required Python packages:
```bash
pip install -r /path/to/requirements.txt
```
### Step 3: Set Up Cron Job

To run the script periodically, open your crontab and add the following line to check for IP address changes every 15 minutes:
```bash
crontab -e
```
Then add this line:
```bash
*/15 * * * * /opt/cloudflare-python-dyndns/venv/bin/python /opt/cloudflare-python-dyndns/cloudflare-python-dyndns/main.py >/dev/null 2>&1
```
## Environment Variables

Make sure to create a .env file in the project directory and add the following environment variables:

    CLOUDFLARE_API_TOKEN: Your Cloudflare API token with permission to edit DNS records.`
    CLOUDFLARE_ZONE_ID: The Zone ID of your domain in Cloudflare.
    CLOUDFLARE_DNS_RECORD_NAME: The DNS record name (e.g., dyndns.your-domain.com).
    CLOUDFLARE_DNS_RECORD_ID: The DNS record ID for the dyndns record.

## Roadmap

    Support for IPv6 addresses.
    Automate the process of fetching the DNS Record Name and ID.

## Authors

- [@lucashahmann](https://www.github.com/lucashahmann)
## License

[MIT](https://choosealicense.com/licenses/mit/)