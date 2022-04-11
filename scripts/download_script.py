#https://physionet.org/files/vindr-cxr/1.0.0/train/000434271f63a053c4128a0ba6352c7f.dicom?download

pre = 'https://physionet.org/files/vindr-cxr/1.0.0/train/'
append = '.dicom?download'

with open('out.txt', 'w') as out_file:
    with open('aortic_enlargement.txt', 'r') as in_file:
        for line in in_file:
            out_file.write(pre + line.rstrip('\n') + append + '\n')