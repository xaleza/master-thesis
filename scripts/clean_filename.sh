#! /bin/bash
# Rename all *.txt to *.text
for f in *.dicom?download; do 
    mv -- "$f" "${f%.dicom?download}.dicom"
done