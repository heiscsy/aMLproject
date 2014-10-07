import faceclass
import re


class FeatureExtraction:

    @staticmethod
    def __openFile(infile,outfile):
        #Open input/output file, static method
        facelist = open(infile,'r');
        featuredata = open(outfile,'w');

    @staticmethod
    def __closeFile(infile,outfile):
        #close input/output file,static method
        facelist.close();
        featuredata.close();

    @staticmethod
    def parseFacefile():
        for line in facelist:
            newface = Facedata();
            
            elts=re.split(r'[\_.]',line);
            last_index= len(elts);
            if elts[last_index-3]=="open":#-3 for *_4 data, -2 for original data
                newface.withglass = "1";
            else
                newface.withglass = "0";

            pixeldata = open(line.strip('[\n]'),'rb');
            type=pixeldata.readline(); #P2 OR P5
            if type
