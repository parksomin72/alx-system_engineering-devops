# 0-strace_is_your_friend.pp

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
