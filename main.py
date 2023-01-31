from psd_tools import PSDImage

psd = PSDImage.open('test.psd')
psd.composite().save('example.png')
