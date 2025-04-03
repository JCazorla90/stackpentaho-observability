#!/bin/bash

echo "🚀 Iniciando Pentaho Observability Stack..."

# Construir contenedores
docker-compose build

# Iniciar servicios en segundo plano
docker-compose up -d

echo ""
echo "✅ Stack levantado correctamente."
echo "🌐 Accede a:"
echo "   - Grafana:      http://localhost:3000 (admin / admin)"
echo "   - Prometheus:   http://localhost:9090"
echo "   - Kibana:       http://localhost:5601"
echo "   - Exporter:     http://localhost:9100/metrics"
