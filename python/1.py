import string

def mapper(strg):
    shift = 26
    newchar = strg
    if strg in string.ascii_lowercase:
        char_no = string.ascii_lowercase.index(strg)
        shifted = (char_no + 2) % 26
        newchar = string.ascii_lowercase[shifted]
    return (newchar)


# strg = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
strg = 'map'
print (''.join(list(map(mapper, strg))))