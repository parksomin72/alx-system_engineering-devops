# Puppet manifest to install Flask package
# Ensure the package is installed
package { 'Flask':
  ensure => '2.1.0',
  provider => 'pip3',
}
