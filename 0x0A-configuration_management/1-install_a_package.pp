# Using Puppet, install flask from pip3.
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/bin',
  creates => '/path/to/some/file/that/exists/when/flask/is/installed',
}
