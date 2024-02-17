# 0-strace_is_your_friend.pp

# Fix for Apache returning a 500 error
exec { 'fix-apache-500-error':
  command     => '/bin/sed -i "s/LogLevel warn/LogLevel debug/g" /etc/apache2/apache2.conf',
  path        => '/bin',
  refreshonly => true,
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => Exec['fix-apache-500-error'],
}
