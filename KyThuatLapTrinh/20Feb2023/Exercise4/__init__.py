import nmap


def scan_ports(host):
    nm = nmap.PortScanner()
    nm.scan(host)

    print("Scanning host: ", host)

    for host in nm.all_hosts():
        print("Host: ", host)

        for proto in nm[host].all_protocols():
            print("Protocol: ", proto)

            lport = nm[host][proto].keys()
            sorted_lport = sorted(lport)

            for port in sorted_lport:
                print("Port: ", port, "state: ", nm[host][proto][port]['state'])
if __name__ == '__main__':
    scan_ports('facebook.com')