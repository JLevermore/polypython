# polypython
Python library for the spectroscopic identification of plastic particulates in Raman spectral images. This python library consists of four spectral normalisation equations, a x and y pixel dimension estimator, and spectral image analysis function. Load the polypython library using the following:

```
* pip install polypython
import polypython as pp
```
## Spectral normalisation
The three spectral normalisation questions include max, area, interval, and standard normal variate (SNV). All spectral images should be loaded in .txt format with rows representing Raman spectrums, and columns being the Raman shifts (cm-1). The four normalisation codes can be called using the following:

```
pp.snv(data)
pp.norm(data, mode='max')
pp.norm(data, mode='area')
pp.norm(data, mode='01')
```

## xy pixel estimation
The x and y pixel number can be estimated from the spectral data number using prime factorisation by running the following code on your Raman data set:
```
#data shape: [Raman spectrum number, Raman shifts (cm-1)
pp.xy(data)
```

## File_locator
To save plastic analysed spectral images in an appropriate location, the user can define where to save the spectral images using the following:
```
#data shape: [Raman spectrum number, Raman shifts (cm-1)
location = pp.file_locator()
Where would you like to save your data and graphs? i.e. "/home/Desktop/DataFolder"/home/Desktop/DataFolder/
```

## Polyrsi analysis
The polyrsi function can be used to identify the presence of plastic related spectra in a Raman spectral image, using the following:
```
#data shape: [Raman spectrum number, Raman shifts (cm-1)
#xy: xy image pixel dimension
#location: file location saver
pp.polyrsi(data,xy,location)
```
