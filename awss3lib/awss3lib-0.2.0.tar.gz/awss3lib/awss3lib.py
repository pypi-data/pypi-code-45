#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 16:51:15 2018

@author: antony
"""

import boto3

class AWSS3File(object):
    """
    Wrap S3 IO in a file like object
    """
    
    def __init__(self, bucket, file):
        """
        Construct AWS S3 File
        
        Parameters
        ----------
        bucket : AWSS3Bucket
            Parent bucket.
        file : str
            File name in bucket.
        """
        self.__bucket = bucket
        self.__file = file
        self.__seek = 0
    
    def seek(self, seek):
        """
        Set the seek position.
        
        Parameters
        ----------
        seek : int
            File offset in bytes
        """
        self.__seek = seek
    
    def read(self, n=0):
        """
        Read bytes from file.
        
        Parameters
        ----------
        n : int, optional
            Read n bytes from file. Default is 0 which reads the whole file.
            If n is not specified, seek as no effect as the whole file will
            be read.
            
        Returns
        -------
        bytearray
            Bytes from file.
        """
        return self.__bucket.read(self.__file, seek=self.__seek, n=n)
    
    def close(self):
        pass
            

class AWSS3Bucket(object):
    def __init__(self, bucket):
        self.__bucket = bucket
        self.__s3 = boto3.resource('s3')
        
    def open(self, file):
        """
        Return a file like object for reading from AWS S3 object.
        
        Parameters
        ----------
        file : str
            File name.
        
        Returns
        -------
        AWSS3File
            File object
        """
        return AWSS3File(self, file)
    
    def read(self, file, seek=0, n=0):
        """
        Read from a file in a bucket.
        
        Parameters
        ----------
        file : str
            File to read
        seek : int, optional
            File offset in bytes.
        n : int, optional
            Number of bytes to read.
        """
        
        # Prevent negative indices
        n = max(0, n)
        seek = max(0, seek)
        
        obj = self.__s3.Object(self.__bucket, file)
        
        if n > 0:
            body = obj.get(Range='bytes={}-{}'.format(seek, seek + n))['Body']
        else:
            body = obj.get()['Body']
            
        data = body.read()
        #data = io.BytesIO(data)
        return data