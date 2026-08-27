#!/bin/bash

#i)

sed '/and/p' sed.txt

#ii)

sed 's/language/lang/g' sed.txt

#iii)

sed '/is/d' sed.txt

#iv)

sed '=' sed.txt | sed 'N; s/\n/ /'

#v)

sed -n '1,2p' sed.txt

#vi)

sed -n '1~2p' sed.txt

#vii)

sed 's/Python/python/;s/language/lang/' sed.txt
