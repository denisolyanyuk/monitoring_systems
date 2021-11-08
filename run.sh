#!/bin/bash

# Upload Dashboard to Grafana
grafanaDashboard=$(<./init/grafana-dashboards.json)
curl -X POST http://admin:admin@localhost:3000/api/dashboards/db -H 'Accept: application/json' -H 'Content-Type: application/json' -d "{\"dashboard\":$grafanaDashboard}"

echo "Dashboard created"

# Upload Datasource to Grafana
grafanaDatasource=$(<./init/grafana-sources.json)
curl -X POST http://admin:admin@localhost:3000/api/datasources -H 'Accept: application/json' -H 'Content-Type: application/json' -d "$grafanaDatasource"

echo "Datasource created"
echo "======="


# Init data for the app
curl --request GET --url http://localhost:8000/create_users

