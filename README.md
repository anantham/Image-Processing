# Image-Processing
IC 040 IMAGE PROCESSING - Code Samples for concepts learned while pursuing this elective

## Homomorphic filtering

I thank Steve Eddins, for his [blog post](http://blogs.mathworks.com/steve/2013/06/25/homomorphic-filtering-part-1/) on this.

In case of homomorphic filtering, I am taking the image into the log domain so as to seperate the illumination and the reflectance of the image (Multiplicative model).

As the irregualar illumination varies slowly and reflectance (property if the object being imaged) varies with a high frequency when we look at it with respect to the spatial domain.

After running my code I get this

![comparison of before and after homomorphic filtering](http://i.imgur.com/INI4d5W.png?1)

As you can see the illumination is regular across the image. Thus we have removed the multiplicative noise.

## DCT

This is the code I got from [here](http://bugra.github.io/work/notes/2014-07-12/discre-fourier-cosine-transform-dft-dct-image-compression/), I used it to get great insight into DCT. I added some comments to understand it better.


## Image Transformations

The plan is to explore the equations relating to the various transforms using actual images - numpy arrays. 

My first attempt is at getting the illumination - from the homomorphic filtered - before and after image. 