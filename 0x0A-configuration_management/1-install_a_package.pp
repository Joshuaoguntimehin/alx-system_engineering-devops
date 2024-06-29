# Puppet manifest to install Flask version 2.1.0 using pip3

class install_flask {
  package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
  }
}

include install_flask
