# 2-puppet_custom_http_response_header.pp

node 'default' {
  # Install Nginx package
  package { 'nginx':
    ensure => installed,
  }

  # Configure Nginx with custom HTTP response header
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('2-puppet_custom_http_response_header/default.erb'),  # Update the path here
    notify  => Service['nginx'],
  }

  # Ensure Nginx service is running and enabled
  service { 'nginx':
    ensure  => running,
    enable  => true,
  }
}
