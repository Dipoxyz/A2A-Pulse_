# A2A Pulse ⚡

**A live-feed dashboard and activity explorer built on the A2A Family API.**

A2A Pulse turns raw A2A feed data into a clear, searchable interface for exploring agent activity, transaction records, and network statistics.

## Features

- **Network overview:** Calls, settled volume, agent counts, and median latency.
- **Live activity feed:** Browse transaction records, agents, assets, timestamps, and block numbers.
- **Search and filters:** Search feed records and filter by agent or transaction type.
- **Transaction explorer:** Open available transaction links in the blockchain explorer.
- **Automatic refresh:** Refreshes feed data every 30 seconds, with manual refresh available.
- **Responsive interface:** Designed for desktop and mobile screens.
- **Error handling:** Displays API connection status and handles failed requests.

## Data Sources

- Feed: https://api.a2a.family/feed
- Statistics: https://api.a2a.family/stats

The dashboard retrieves data from these endpoints through a lightweight Python server.

## Requirements

- Python 3.9 or later
- Internet access

No database or API key is required for the current implementation.

## Run Locally

Clone the repository:

```bash
git clone https://github.com/Dipoxyz/A2A-Pulse_.git
cd A2A-Pulse_
```

Start the server:

```bash
python server.py
```

Open http://localhost:8000 in your browser.

## How It Works

1. The Python server serves the dashboard.
2. Requests to `/api/feed` and `/api/stats` are forwarded to the A2A Family API.
3. The frontend renders returned statistics and activity records.
4. The dashboard refreshes automatically every 30 seconds.

## Project Status

Built for the A2A Family live-feed bounty.

## License

No license has been specified yet.
