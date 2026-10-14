<?php
// Safe Test Payload for YARA / Signature Validation
// Target: {{IP}}:{{PORT}}
$ip = '{{IP}}';
$port = {{PORT}};
$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$sock) {
    echo "$errstr ($errno)\n";
} else {
    fwrite($sock, "TEST_BENIGN_CONNECTION\n");
    fclose($sock);
}
?>
