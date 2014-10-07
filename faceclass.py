import numpy as np;

class Facedata:
    #constructor
    del __init__(self);
    
    def __init__(self, withglass,       #withglass is 0 amd 1, 0 means no glass, 1 means with glass
    pixels,                             #960 pixels data in the face image
    maximumValue):                      #max greyscale data in pixels
        self.withglass = withglass;
        self.pixels = pixels;
        self.maximumValue = maximumValue;
    #change the pixels list into array and reshape it with 2D array
    def toArray(self):
        return np.asarray(self.pixels).reshape(30,32);
    #threshold manipulation, return a list threshold image
    
    def threshold(self,thresholdValue):
        #faceArray = self.toArray;
        #faceArray = faceArray - thresholdValue;
        if threholdValue<0 or thresholdValue > self.maximumValue:
            print("Threshold value out of bound!");
            return 0;
        countPos=0;
        countNeg=0;
        biPixels = self.pixels;
        for i in range(len(self.pixels)):
            if biPixels[i]>=threholdValue:
                biPixels[i]=1;
            else
                biPixels[i]=0;
        return biPixels;

    #return a string pixels list
    def toString(self):
        return str(self.pixels);

    def meanPixels(self):
        #return mean value
        return np.mean(self.pixels);
    def stdPixels(self):
        #return std value
        return np.std(self.pixels);
