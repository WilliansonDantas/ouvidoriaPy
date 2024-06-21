#!/usr/bin/env bash
# Use this script to wait for a service to be available
set -e

host="$1"
shift
port="$1"
shift

while ! nc -z "$host" "$port"; do
  sleep 0.1
done

exec "$@"
