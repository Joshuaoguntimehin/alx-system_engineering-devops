#!/usr/bin/env bash
file { '/home/your_username/.ssh':
  ensure => directory,
  mode   => '0700',
}

file { '/home/your_username/.ssh/config':
  ensure => file,
  mode   => '0644',
  content => "
Host your_server_alias
    HostName 3.83.245.5  # Replace with your server's IP or hostname
    User ubuntu          # Replace with your server's username
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
",
}
