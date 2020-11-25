import os, zlib, struct, base64, traceback, blowfish
import xml.dom.minidom as dom

sysname, nodename, release, version, machine = os.uname()
ncpus = open('/proc/cpuinfo').read().count('processor')

def crc32(s):
    return '%X'%struct.unpack('L', struct.pack('l', zlib.crc32(s)))[0]

def Decripta(cipherText, key):
    cipherText = base64.b64decode(cipherText)
    plainText = ''
    bfish = blowfish.Blowfish(key)
    cipherBlock = [37,17,25,118,9,2,25,115]
    while len(cipherText):
        xorPad = map(ord,bfish.encrypt(''.join(map(chr,cipherBlock))))
        cipherBlock = map(ord,cipherText[:8])
        plainText += ''.join([chr(cipherBlock[i]^xorPad[i]) for i in range(len(cipherBlock))])
        cipherText = cipherText[8:]
    if not (plainText[:4] == 'STE!' and plainText[-1] == '\x00'):
        raise ValueError, 'wrong decryption'
    return plainText[4:-1]

cryptkey = crc32('|'.join([sysname, release, str(ncpus)]))
path = os.path.join(os.getenv('HOME'), '.java', '.userPrefs', crc32(cryptkey) ,'prefs.xml')

digests = {}

if os.path.exists(path):
    try:
        uncryptkey = {}
        for key in 'digest1', 'digest2':
            uncryptkey[crc32(key+cryptkey)] = key
        
        elem = dom.parse(open(path))
        for elem in elem.childNodes:
            if elem.nodeName == 'map':
                for elem in elem.childNodes:
                    if elem.nodeName == 'entry':
                        key, value = [elem.attributes[attrname].value for attrname in 'key', 'value']
                        digests[uncryptkey[key]] = Decripta(value, cryptkey)
    except:
        traceback.print_exc()

if len(digests.items()) != 2:
    for key in 'digest1','digest2':
        digests[key] = '%08X'%struct.unpack('L',open('/dev/urandom').read(4))[0]
                    
print("""
var gbasConfig = {
   'digest1': '%s',
   'digest2': '%s'
};
""" % tuple([digests[dig] for dig in 'digest1','digest2']))

    