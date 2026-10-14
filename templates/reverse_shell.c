#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

// Safe Test Payload for Signature Validation
int main() {
    char *ip = "{{IP}}";
    int port = {{PORT}};
    printf("Initializing safe socket test to %s:%d\n", ip, port);
    return 0;
}
