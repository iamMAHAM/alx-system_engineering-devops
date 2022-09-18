exec { 'pkill':
  command  => 'pip3 install flask=2.1.0',
  provider => 'python3',
}