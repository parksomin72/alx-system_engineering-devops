# Puppet manifest to execute a command to kill a process

# Execute the command to kill the process
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'pgrep -f killmenow',
}
