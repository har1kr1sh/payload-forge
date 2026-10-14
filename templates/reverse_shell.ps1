# Safe Test File for YARA / Signature Validation
# Target: {{IP}}:{{PORT}}

$IP = "{{IP}}"
$Port = {{PORT}}

Write-Host "[+] Initializing safe socket connection test to $IP`:$Port"

try {
    $Client = New-Object System.Net.Sockets.TcpClient
    $Client.Connect($IP, $Port)
    $Stream = $Client.GetStream()
    
    $Message = [System.Text.Encoding]::UTF8.GetBytes("TEST_BENIGN_CONNECTION`n")
    $Stream.Write($Message, 0, $Message.Length)$Client.Close()
    Write-Host "[+] Connection test completed successfully."
}
catch {
    Write-Host "[-] Socket test finished: $_"
