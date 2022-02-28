# PyART Data Demo
Test out pooch for test data with examples

## Installation
1. Clone this repository
1. Run `pip install -e .` within the base directory

## How to Use this Package
There are two methods of accessing the test data!

### Using `get_test_data()` - Easy if You Know What File
The easiest way to grab test data is by using `get_test_data()`, with the
caveat being that you need to know what file you are looking for.

For example, say we are looking for the file ``... we could use something like the following:

```bash
In [1]: from pyart_datasets import get_test_data

In [2]: get_test_data('110041.mdv')
Downloading file '110041.mdv' from 'https://engineering.arm.gov/~jhelmus/pyart_example_data/110041.mdv' to '/Users/mgrover/Library/Caches/pyart-datasets'.
Out[2]: '/Users/mgrover/Library/Caches/pyart-datasets/110041.mdv'
```

Since we have not downloaded that data yet, it will access the server (https://engineering.arm.gov/~jhelmus/pyart_example_data), download the data, and store it our Cache Directory.


### Use the Pooch `.fetch()` Method Directly
You could also use the `DATASETS` object to get an idea of what datasets are there, and grab those datasets using `.fetch()`. For example, let's say we are looking to find _*what datasets are available*_...

```bash
In [1]: from pyart_datasets import DATASETS

In [2]: DATASETS.registry_files
Out[2]: 
['034142.mdv',
 '095636.mdv',
 '110041.mdv',
 '110635.mdv',
 '20110520100000_nex_3d.nc',
 '20110520100000_nexrad_grid.nc',
 '220629.mdv',
 'KATX20130717_195021_V06',
 'Level2_KATX_20130717_1950.ar2v',
 'XSW110520105408.RAW7HHF',
 'XSW110520113537.RAW7HHL',
 'narr-a_221_20110520_0000_000.nc',
 'nsaxsaprppiC1.a1.20140201.184802.nc',
 'preprocessed.nc',
 'pvcwsacrhsrhiM1.b1.20121105.201200_modified.nc',
 'sex_20120520_0641.nc',
 'sgpcsaprsurcmacI7.c0.20110520.095101.nc',
 'sgpinterpolatedsondeC1.c1.20110510.000000.cdf',
 'sgpxsaprrhicmacI5.c0.20110524.015604_NC4.nc',
 'swx_20120520_0641.nc']
```

Now, to retrieve that data, you would use the `.fetch()` method. If the file is already downloaded, it will retrieve the path. Otherwise, that file will be downloaded and to default directory and the path is returned.

```bash
In [3]: file = DATASETS.fetch('034142.mdv')

In [4]: file
Out[4]: '/Users/mgrover/Library/Caches/pyart-datasets/034142.mdv'
```
