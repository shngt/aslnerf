#!/usr/bin/env bash

SUBJECT=$1
if [ -z "${SUBJECT}" ]
then
    SUBJECT=sample3F_176
fi

python run.py \
    --type tpose \
    --cfg ./configs/human_nerf/wild/${SUBJECT}/adventure.yaml \
    load_net latest
