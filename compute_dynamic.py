from dynamic_wsmi import computeWSMI
import glob
import os
import re

#we list all mat files in a directory
files = glob.glob('E:\\research\\*.mat')
#this file saves the progress by writing the filename when it finishes. If you run it again it won't process
#files in this list
progress = open('progress.txt', 'r').read()

for subject in files:
    subject_filename = os.path.basename(subject)
    if subject_filename in progress:
        print('Ignoring ' + subject_filename + ' since it was found in progress.txt')
        continue
        
    computeWSMI(
        file_to_compute=subject,
        word_to_compute=subject.split("\\")[-1].split(".mat")[0],    
        output_path='E:/research/result',
        sample_rate=500,            
        channels=32,                
        samples_per_trial=640,      
        tau=8,                      
        total_time=160,             
        window_size=42,             
        window_offset=2             
    )
    f = open("progress.txt", "a").write(subject_filename + ',')

