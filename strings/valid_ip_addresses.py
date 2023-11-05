from typing import List

from test_framework import generic_test

"""

A decimal string is a string consisting of digits between 0 and 9. Internet Protocol (IP) addresses can be written as 
four decimal strings separated by periods, e.g.,192.168.1.201. A careless programmer mangles a string representing an 
IP address in such away that all the periods vanish.

Write a Program that determines where to add periods to a decimal string so that the resulting string is a valid IP 
address. There may be more than one valid IP address corresponding to a string, in which case you should print all 
possibilities.
For example, if the mangled string is "19216811" then two corresponding IP addresses are 192.168.1.1 and 19.216.81.1. 
(There are seven other possible IP addresses for this string.)

"""

def get_valid_ip_address(s: str) -> List[str]:
    valid_ip_address_list = []

    """
    def get_valid_ip_address_helper(partial_ip_address, start_index):
        if len(partial_ip_address) == 4:
            if start_index == len(s) and len((ip_address := '.'.join(partial_ip_address))) == len(s) + 3:
                valid_ip_address_list.append(ip_address)
        else:
            index = start_index
            while index < len(s) and (number := int(s[start_index:index + 1])) <= 255:
                get_valid_ip_address_helper(partial_ip_address + [(str(number))], index + 1)
                if s[start_index] == '0':
                    break
                index += 1
    """
    def is_valid_part(part: str):
        return (len(part) == 1 or
                (part[0] != '0' and
                int(part) <= 255))

    def get_valid_ip_address_helper(partial_ip_address, start_index):
        if len(partial_ip_address) == 4:
            if start_index == len(s):
                valid_ip_address_list.append('.'.join(partial_ip_address))
        else:
            index = start_index
            while index < len(s):
                address_part = s[start_index: index + 1]
                if not is_valid_part(address_part):
                    break
                get_valid_ip_address_helper(partial_ip_address + [address_part], index + 1)
                index += 1

    get_valid_ip_address_helper([], 0)

    return valid_ip_address_list


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
    # # get_valid_ip_address("11111111")
    # # get_valid_ip_address("333333333333")
    # get_valid_ip_address("111111119199")