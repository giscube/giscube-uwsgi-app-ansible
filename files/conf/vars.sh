#!/bin/bash
if [ "$(uname)" == "Darwin" ]; then
  SED="sed -E"
else
  SED="sed -r"
fi

eval $(
  cat "./vars.ini" | grep '^\w.*=' | while read -r line; do
    echo $line |
    $SED 's/'"'"'/'"'\"'\"'"'/g' |  # escape single quotes (s/'/'"'"'/g but scaped correctly)
    $SED 's/^(.+)=(.*)$/export'" '\1'='\2'/"
  done
)
