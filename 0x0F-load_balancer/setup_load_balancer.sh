#!/usr/bin/env bash
# Script to configure and set up HAProxy as a load balancer

# Install HAProxy
sudo apt-get update
sudo apt-get install -y haproxy

# Backup the default HAProxy configuration
sudo mv /etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg.bak

# Create a new HAProxy configuration file
echo "global
    daemon
    maxconn 256

defaults
    mode http
    timeout connect 5000ms
    timeout client 50000ms
    timeout server 50000ms

frontend http_front
    bind *:80
    default_backend http_back

backend http_back
    balance roundrobin
    server web-server1 34.198.248.145:80 check
    server web-server2 54.89.38.100:80 check" | sudo tee /etc/haproxy/haproxy.cfg

# Restart HAProxy to apply changes
sudo service haproxy restart
