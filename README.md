# Image-Processing-
IC 040 IMAGE PROCESSING - Code Samples for concepts learned while pursuing this elective

## Homomorphic filtering

In case of homomorphic filtering, I am taking the image into the log domain so as to seperate the illumination and the reflectance of the image (Multiplicative model).

As the irregualar illumination varies slowly and reflectance (property if the object being imaged) varies with a high frequency when we look at it with respect to the spatial domain.

![Image before enhancement](http://read.pudn.com/downloads166/sourcecode/graph/761254/adapt_threshold/page.png)

After running my code I get this

![comparison of before and after homomorphic filtering](http://imgur.com/INI4d5W)

As you can see the illumination is regular across the image. Thus we have removed the multiplicative noise.