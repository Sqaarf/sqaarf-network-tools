class Ipv4Addr:
    def __init__(self, addr):
        self.str_addr = addr.split(".")
        self.addr = [int(x) for x in self.str_addr]
        self.bin_addr = ["{:08b}".format(x & 255) for x in self.addr]

        if self.bin_addr[0][:1] == "0":
            self.net_class = 'A'
            self.cidr_mask = '/8'
            self.net_addr = []
            self.brod_addr = []

            for i in range(len(self.str_addr)): #Calculate network/broadcast address
                if i == 0:
                    self.net_addr.append(self.str_addr[0])
                    self.brod_addr.append(self.str_addr[0])
                else:
                    self.net_addr.append('0')
                    self.brod_addr.append('255')

        elif self.bin_addr[0][:2] == "10":
            self.net_class = 'B'
            self.cidr_mask = '/16'
        elif self.bin_addr[0][:3] == "110":
            self.net_class = 'C'
            self.cidr_mask = '/24'
        elif self.bin_addr[0][:3] == "1110":
            self.net_class = 'D'
            self.cidr_mask = None
        elif self.bin_addr[0][:4] == "1111":
            self.net_class = 'E'
            self.cidr_mask = None

    def __str__(self):
        res = f"IPV4 Address : {'.'.join(self.str_addr)}\n"
        res += f"IPV4 binary address : {' '.join(self.bin_addr)}\n"
        res += f"Network Address : {'.'.join(self.net_addr)}{self.cidr_maskpà}\n"
        res += f"Broadcast Address : {'.'.join(self.brod_addr)}\n"
        res += f"Network class : {self.net_class}"

        return res

