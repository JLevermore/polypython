# polypython
Python library for the spectroscopic identification of plastic particulates in Raman spectral images. This python library consists of four spectral normalisation equations, a x and y pixel dimension estimator and a spectral image analysis function. Load the polypython library using the following:

```python
* pip install polypython
import polypython as pp
```
## Spectral normalisation
The four spectral normalisation equations include max, area, interval, and standard normal variate (SNV). All spectral images should be loaded in .txt format with rows representing Raman spectrums and columns being the Raman shifts (cm-1). The four normalisation codes can be called using the following:

```python
data = pp.norm(data, mode='snv')
data = pp.norm(data, mode='max')
data = pp.norm(data, mode='area')
data = pp.norm(data, mode='01')
```

## xy pixel estimation
An x and y pixel number can be estimated from the spectrum number using prime factorisation by running the following code:
```python
#data shape: [Raman spectrum number, Raman shifts (cm-1)
xy = pp.xy(data)
```

## File_locator
To save plastic analysed spectral images in an appropriate location, the user can define where to save the spectral images using the following:
```python
#data shape: [Raman spectrum number, Raman shifts (cm-1)
location = pp.file_locator()
#which will print: where would you like to save your data and graphs? i.e. "/home/Desktop/DataFolder" 
/home/Desktop/DataFolder/ #an example of your desired file path
```

## Polyrsi analysis
The polyrsi function can be used to identify the presence of plastic related spectra in a Raman spectral image using the following:
```python
#data shape: [Raman spectrum number, Raman shifts (cm-1)
#xy: xy image pixel dimension
#location: file location saver
pp.polyrsi(data,xy,location)
```

If you decide to use Polypython to analyse your Raman spectral images, please reference this academic journal: https://doi.org/10.1021/acs.analchem.9b05445.

