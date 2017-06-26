Usage:

```
usage: run.py [-h] url phn_input_file output_directory credentials

positional arguments:
  url               OSCAR EMR url
  phn_input_file    input file containing list of PHN numbers to export
  output_directory  output directory
  credentials       comma-delimited credentials, eg. dave:password:pin

optional arguments:
  -h, --help        show this help message and exit
```

How to run:

./run.py https://oscar:8443/oscar input output user:pass:pin
