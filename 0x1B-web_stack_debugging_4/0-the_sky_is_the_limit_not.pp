# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Define Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('/alx-system_engineering-devops/0x1B-web_stack_debugging_4/nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Define Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}

# Define an exec resource to reload Nginx configuration
exec { 'reload-nginx':
  command     => '/usr/sbin/service nginx reload',
  refreshonly => true,
}
