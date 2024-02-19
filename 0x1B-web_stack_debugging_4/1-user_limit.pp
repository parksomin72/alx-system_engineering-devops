# Puppet manifest to adjust OS configuration to resolve "Too many open files" issue for the holberton user

# Define an exec resource to increase the open file limit for the holberton user
exec { 'increase-open-file-limit':
  command  => 'ulimit -n 65535',
  user     => 'holberton',
  unless   => 'ulimit -n | grep 65535',
  provider => shell,
  require  => User['holberton'],
}

# Define the holberton user
user { 'holberton':
  ensure => present,
  # Add any necessary user parameters here
}
