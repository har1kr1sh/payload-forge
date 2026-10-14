# Safe Test File for YARA / Signature Validation
# Target: {{IP}}:{{PORT}}

require 'socket'

ip = '{{IP}}'
port = {{PORT}}

begin
  puts "[+] Initializing safe socket connection test to #{ip}:#{port}"
  socket = TCPSocket.new(ip, port)
  socket.puts("TEST_BENIGN_CONNECTION")
  socket.close
  puts "[+] Connection test completed successfully."
rescue => e
  puts "[-] Socket test finished: #{e.message}"
end
