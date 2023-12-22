# Puppet manifest to create a file in /tmp

# Ensure the file exists
file { '/tmp/school':
  ensure  => present,
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
