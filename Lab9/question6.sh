#!/bin/bash

echo $HOME

bc << EOF
23934/44343
EOF

ls $HOME | grep "D"

grep $USER /etc/passwd

