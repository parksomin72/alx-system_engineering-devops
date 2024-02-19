# Puppet manifest to optimize Nginx configuration to handle ApacheBench load

# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Define Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Define Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
}

# Define an exec resource to reload Nginx configuration
exec { 'reload-nginx':
  command     => 'service nginx reload',
  refreshonly => true,
}

# Template for Nginx configuration
# Adjust this template based on your specific configuration needs
file { '/etc/nginx/sites-available/default.erb':
  ensure => present,
  content => template('nginx/default.erb'),
}
