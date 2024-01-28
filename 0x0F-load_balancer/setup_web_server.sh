#!/usr/bin/env bash
# Script to configure a web server

# Install Apache and PHP (assuming a LAMP stack)
sudo apt-get update
sudo apt-get install -y apache2 php

# Create a simple index.php file for testing
echo "<?php phpinfo(); ?>" | sudo tee /var/www/html/index.php

# Restart Apache to apply changes
sudo service apache2 restart
