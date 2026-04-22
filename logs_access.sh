#!/bin/bash

BASE="/var/log/centralizacion"

case "$SSH_ORIGINAL_COMMAND" in
    "list-hosts")
        ls "$BASE"
        ;;
    "list-logs "*)
        HOST=$(echo "$SSH_ORIGINAL_COMMAND" | cut -d' ' -f2)
        ls "$BASE/$HOST"
        ;;
    "read-log "*)
        HOST=$(echo "$SSH_ORIGINAL_COMMAND" | cut -d' ' -f2)
        FILE=$(echo "$SSH_ORIGINAL_COMMAND" | cut -d' ' -f3)
        tail -n 200 "$BASE/$HOST/$FILE"
        ;;
    *)
        echo "Comando no permitido"
        exit 1
        ;;
esac
