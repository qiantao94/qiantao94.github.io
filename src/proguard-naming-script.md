---
layout: post
title: Android Proguard custom naming for obfuscation
slug: typography
date: 2018-01-04 16:50
status: publish
excerpt: A script to generate random characters for naming classes, members and parameters after obfuscation 
---
After using Proguard, names of classes, members and parameters will become characters such as `a b c`.

In fact, **we can specify which characters** are used to replace the display after obfuscation, that is, it can be configured in `proguard-rules.pro`


``` pro
-obfuscationdictionary  dictionary.txt
-classobfuscationdictionary dictionary.txt
-packageobfuscationdictionary dictionary.txt
```

The `dictionary.txt` here is a plain text file similar to this:

``` txt
#dictionary.txt

go
O1
VU
VN
0f
vV
HT
AU
Kd
SX
```

The characters in the above dictionary file are randomly selected from uppercase and lowercase letters and numbers.

To generate such a file, use the following python script

``` python
import string
import random


def rand_string(length):
    return ''.join(random.choice(
        string.ascii_lowercase + string.ascii_uppercase + string.digits)
        for i in range(length)
    )


if __name__ == '__main__':
    FILE = open("proguard-dictionary.txt", 'w')
    WORD_LINES = 40
    FILE.write("#proguard dictionary\n\n")
    for i in range(1, WORD_LINES):
        FILE.write(rand_string(2)+"\n")
    FILE.close()
```

Hope you enjoy it. 🙂