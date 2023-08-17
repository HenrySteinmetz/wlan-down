#!/bin/python3
import subprocess
for i in range(20): subprocess.run(["wget", "https://mirror.cmt.de/archlinux/iso/2023.08.01/archlinux-2023.08.01-x86_64.iso", ">", "/dev/null"])
