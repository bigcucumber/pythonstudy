__author__ = 'luowen'
"this is get uuid demo"

import uuid

baseHostAndCurrentTime = uuid.uuid1()
print(baseHostAndCurrentTime)  # base the host id and current time to generate uuid

baseStringMd5Hash = uuid.uuid3(namespace=uuid.NAMESPACE_URL, name="luowen")
print(baseStringMd5Hash)  # base the string md5 value to generate uuid

baseRandom = uuid.uuid4()
print(baseRandom)  # random generate uuid

baseStringShaHash = uuid.uuid5(uuid.NAMESPACE_URL, 'luowen')
print(baseStringShaHash)  # base string sha value to generate value

