# 0-strace_is_your_friend.pp

# Fix for Apache returning a 500 error
exec { 'fix-apache-500-error':
  command     => '/bin/sed -i "s/LogLevel warn/LogLevel debug/g" /etc/apache2/apache2.conf && service apache2 restart',
  path        => '/bin',
  refreshonly => true,
}

# Intentionally cause an error in Apache configuration to return 500 status code
file { '/etc/apache2/sites-available/000-default.conf':
  ensure  => present,
  content => "This is an intentional error to cause Apache to return a 500 status code",
}


# Restart Apache to apply changes
service { 'apache2':
  ensure    => running,
  enable    => true,
  require   => File['/etc/apache2/sites-available/000-default.conf'],
}
