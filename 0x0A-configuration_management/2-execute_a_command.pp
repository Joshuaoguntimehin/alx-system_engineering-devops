exec { 'kill_killmenow':
  command     => 'pkill -f killmenow',
  path        => ['/bin', '/usr/bin', '/usr/sbin'],
  refreshonly => true,
}

# To trigger the exec resource
notify { 'trigger_kill':
  notify => Exec['kill_killmenow'],
}
