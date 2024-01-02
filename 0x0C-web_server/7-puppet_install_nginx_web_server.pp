# Puppet manifest to install and configure Nginx web server

# Install Nginx package
package { 'nginx':
  ensure => present,
}

# Create a default index.html file
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
    listen 80;
    server_name _;

    location / {
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    location /redirect_me {
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
      root /usr/share/nginx/html;
      internal;
    }
  }",
}

# Create a symbolic link to enable the configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Create a custom 404 page
file { '/usr/share/nginx/html/custom_404.html':
  ensure  => present,
  content => 'Ceci n\'est pas une page',
}

# Restart Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => [
    Package['nginx'],
    File['/etc/nginx/sites-enabled/default'],
    File['/usr/share/nginx/html/custom_404.html'],
  ],
}
