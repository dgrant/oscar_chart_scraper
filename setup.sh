#!/bin/bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

rm -rf env
hash pip 2>/dev/null || { echo >&2 "I require pip but it's not installed. Aborting."; exit 1; }
if ! hash virtualenv 2>/dev/null; then
    pip install virtualenv
fi

if [ ! -d "$DIR/env" ]; then
    virtualenv "$DIR/env"
fi

"$DIR/env/bin/pip" install -r "$DIR/requirements.txt"
source "$DIR/env/bin/activate"

export PYTHONPATH="$DIR"
