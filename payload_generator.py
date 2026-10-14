#!/usr/bin/env python3
"""
Payload Forge - A simple utility to generate safe benign test payloads
for YARA rule testing and detection engineering validation.
"""

import argparse
import os

TEMPLATES_DIR = "templates"

def generate_payload(lang, ip, port, output):
    template_file = os.path.join(TEMPLATES_DIR, f"reverse_shell.{lang}")
    
    if not os.path.exists(template_file):
        print(f"[!] Error: Template for '{lang}' not found in {TEMPLATES_DIR}/")
        return

    with open(template_file, "r") as f:
        content = f.read()

    # Replace placeholders with target lab variables
    payload = content.replace("{{IP}}", ip).replace("{{PORT}}", str(port))

    with open(output, "w") as f:
        f.write(payload)

    print(f"[+] Successfully generated {lang.upper()} test payload at: {output}")

def main():
    parser = argparse.ArgumentParser(description="Generate safe multi-language test payloads for detection testing.")
    parser.add_argument("-l", "--lang", required=True, choices=["php", "py", "rb", "c", "ps1"], help="Language/format")
    parser.add_argument("-i", "--ip", default="127.0.0.1", help="Target IP (default: 127.0.0.1)")
    parser.add_argument("-p", "--port", type=int, default=4444, help="Target Port (default: 4444)")
    parser.add_argument("-o", "--output", required=True, help="Output filename")

    args = parser.parse_args()
    generate_payload(args.lang, args.ip, args.port, args.output)

if __name__ == "__main__":
    main()
