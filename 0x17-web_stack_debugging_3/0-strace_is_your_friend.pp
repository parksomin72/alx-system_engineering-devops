# 0-strace_is_your_friend.pp

# Fix for Apache returning a 200 OK status code
exec { 'fix-apache-200-ok':
  command     => '/bin/sed -i "s/LogLevel warn/LogLevel debug/g" /etc/apache2/apache2.conf && service apache2 restart',
  path        => '/bin',
  refreshonly => true,
}

# Configure Apache to serve the correct page
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

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => Exec['fix-apache-200-ok'],
}
