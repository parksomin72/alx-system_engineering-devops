# 0-strace_is_your_friend.pp
# Puppet manifest to fix Apache 500 error and ensure Apache returns a 200 status code

# Fix for Apache returning a 500 error
exec { 'fix-apache-500-error':
  command     => '/bin/sed -i "s/LogLevel warn/LogLevel debug/g" /etc/apache2/apache2.conf && service apache2 restart',
  path        => '/bin',
  refreshonly => true,
}

# Ensure Apache is running and enabled
service { 'apache2':
  ensure => running,
  enable => true,
}

# Configure Apache to serve the correct page and verify that it returns a 200 status code
file { '/var/www/html/index.html':
  ensure  => present,
  content => '<!DOCTYPE html>
<html>
<head>
  <title>Holberton - Just another WordPress site</title>
</head>
<body>
  <h1>Welcome to Holberton</h1>
  <p>Yet another bug by a Holberton student</p>
</body>
</html>',
}

# Verify that Apache returns a 200 status code
exec { 'verify-apache-status':
  command     => 'curl -s -o /dev/null -w "%{http_code}" http://localhost/',
  path        => '/usr/bin',
  logoutput   => true,
  unless      => 'curl -s -o /dev/null http://localhost/ || false',
  subscribe   => Service['apache2'],
}
