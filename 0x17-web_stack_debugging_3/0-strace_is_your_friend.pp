# Puppet manifest to fix Apache returning the correct page

# Execute commands to fix the issue
exec { 'fix_apache':
  command     => 'service apache2 restart', # Restart Apache service
  path        => '/usr/bin:/usr/sbin:/bin',
  refreshonly => true,                      # Only execute when notified
}

# Notify the command to execute when Apache is restarted
service { 'apache2':
  ensure  => running,
  require => Exec['fix_apache'],  # Ensure Apache is restarted after fix command execution
}

# Define a file resource to ensure the correct page is served
file { '/var/www/html/index.html':
  ensure  => present,
  content => "<html><head><title>Apache is serving the correct page</title></head><body><h1>Welcome to Apache!</h1><p>This is the correct page served by Apache.</p></body></html>",
  mode    => '0644',  # Set appropriate permissions
  require => Service['apache2'],  # Ensure Apache is running before updating the page
}
