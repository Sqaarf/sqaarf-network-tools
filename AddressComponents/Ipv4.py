class Ipv4Addr:
    def __init__(self, addr):
        self.str_addr = addr.split(".")
        self.addr = [int(x) for x in self.str_addr]
        self.bin_addr = ["{:08b}".format(x & 255) for x in self.addr]

        if self.bin_addr[0][:1] == "0":
            self.net_class = 'A'
        elif self.bin_addr[0][:2] == "10":
            self.net_class = 'B'
        elif self.bin_addr[0][:3] == "110":
            self.net_class = 'C'
        elif self.bin_addr[0][:3] == "1110":
            self.net_class = 'D'
        elif self.bin_addr[0][:4] == "1111":
            self.net_class = 'E'

    def __str__(self):
        res = f"IPV4 Address : {'.'.join(self.str_addr)}\n"
        res += f"IPV4 binary address : {' '.join(self.bin_addr)}\n"
        res += f"Network class : {self.net_class}"

        return res

