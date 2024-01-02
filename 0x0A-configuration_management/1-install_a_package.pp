# Puppet manifest to install Flask package with specific Werkzeug version

# Ensure the package is installed
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Ensure the specific version of Werkzeug is installed
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
