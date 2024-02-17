# Puppet manifest to fix Apache returning the correct page

# Execute commands to fix the issue
exec { 'fix-apache-error':
  command     => '/bin/sed -i "s/AllowOverride None/AllowOverride All/g" /etc/apache2/apache2.conf',
  path        => '/bin',
  refreshonly => true,
}

# Notify the command to execute when Apache is restar
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => Exec['fix-apache-error'],
}

# Define a file resource to ensure the correct page is served
file { '/var/www/html/index.html':
  ensure  => present,
  content => "<html><head><title>Apache is serving the correct page</title></head><body><h1>Welcome to Apache!</h1><p>This is the correct page served by Apache.</p></body></html>",
  mode    => '0644',  # Set appropriate permissions
  require => Service['apache2'],  # Ensure Apache is running before updating the page
}
