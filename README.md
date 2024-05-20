# MPLS Routing Automation Dashboard

A Django-based network automation dashboard for configuring Cisco IOS routers through SSH. The project centralizes common routing and MPLS L3VPN tasks behind a web interface, using Netmiko and Paramiko to push commands to routers and retrieve operational output.

## Project Overview

This application was built to simplify repetitive router configuration tasks in a lab or controlled network environment. Instead of manually opening SSH sessions and typing the same command sequences, an authenticated user can submit forms from the dashboard and trigger automated configuration workflows.

The dashboard supports interface setup, hostname changes, routing protocol configuration, VRF creation, customer-side routing integration, cleanup actions, and route verification.

## Key Features

- User authentication with signup, login, logout, and password change flows.
- Cisco IOS SSH automation with Netmiko and Paramiko.
- Interface provisioning with description, IP address, subnet mask, and `no shutdown`.
- Hostname change workflow with configuration save.
- Routing protocol setup for RIP, OSPF, and EIGRP.
- MPLS L3VPN helper workflows:
  - VRF creation.
  - Route distinguisher and route-target configuration.
  - PE interface binding to VRF.
  - Customer routing integration for RIP, OSPF, and EIGRP.
- Cleanup tools for removing VRFs and routing protocol configuration.
- Route verification page for collecting `show ip route` output.
- Docker Compose setup with a PostgreSQL database.
- Bootstrap-based admin dashboard UI.

## Tech Stack

- Python
- Django
- PostgreSQL
- Docker and Docker Compose
- Netmiko
- Paramiko
- Bootstrap admin template assets

## Repository Structure

```text
.
├── app1/                 # Main Django application
│   ├── forms.py          # Dashboard forms for router and protocol inputs
│   ├── functions.py      # SSH automation logic
│   ├── templates/        # Dashboard pages
│   └── urls.py           # App routes
├── pfe/                  # Django project settings and root URLs
├── Dockerfile            # Web application image
├── docker-compose.yml    # Django + PostgreSQL services
├── requirements.txt      # Python dependencies
└── .env.example          # Example environment configuration
```

## Getting Started

1. Create an environment file from the example:

```bash
cp .env.example .env
```

2. Update `.env` with your Django secret, database values, and router SSH credentials.

3. Start the application:

```bash
docker compose up --build
```

4. Open the dashboard:

```text
http://localhost:8011
```

5. Run database migrations and create a user if needed:

```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

## Environment Variables

| Variable | Purpose |
| --- | --- |
| `DJANGO_SECRET_KEY` | Django signing key |
| `DJANGO_DEBUG` | Enables or disables debug mode |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated host allowlist |
| `POSTGRES_DB` | PostgreSQL database name |
| `POSTGRES_USER` | PostgreSQL user |
| `POSTGRES_PASSWORD` | PostgreSQL password |
| `POSTGRES_HOST` | PostgreSQL host, usually `db` in Docker |
| `POSTGRES_PORT` | PostgreSQL port |
| `ROUTER_USERNAME` | SSH username for Cisco routers |
| `ROUTER_PASSWORD` | SSH password for Cisco routers |
| `ROUTER_SECRET` | Cisco enable secret |

## Example Workflows

### Configure OSPF

From the OSPF page, provide the router IP, OSPF process ID, network and wildcard mask, and area ID. The app connects to the router and applies the corresponding `router ospf` and `network ... area ...` commands.

### Create a VRF

From the L3VPN flow, provide the PE router IP, VRF name, route distinguisher values, route-target values, PE interface, and PE-side IP address. The app creates the VRF, configures RD/RT values, binds the interface, and applies the interface IP address.

### Verify Routes

Use the results page to connect to a router and retrieve routing table output for quick validation after configuration changes.

## Work Completed

- Built a Django dashboard for router automation workflows.
- Added authenticated access around the main configuration views.
- Implemented SSH-based Cisco IOS automation using Netmiko and Paramiko.
- Added Docker Compose orchestration for the web app and PostgreSQL.
- Moved Django, database, and router credentials to environment variables.
- Added `.env.example` to make local setup clearer.
- Updated dependencies to match the Django 4.2 project structure.
- Renamed the Docker build file to `Dockerfile` for Linux/GitHub compatibility.
- Fixed beginner issues including a duplicated form class, a password placeholder typo, incorrect router command strings, inconsistent enable secret handling, and generated-file ignore rules.

## Notes

This project is intended for lab, learning, and controlled network environments. Always test command workflows on non-production routers before using them against real infrastructure.
