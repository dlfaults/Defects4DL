# Defects4DL

Defects4DL is a dataset of reproducible real faults in deep learning systems. Each fault is contained in a 
separate folder *Fault{i}* where *i* is the corresponding index of the fault. The folder for each fault
has the following structure:

* **buggy** and **fixed** folders which contain the buggy and fixed code of the project correspondingly. In the folder
**test** the test class at least one test case in which exposes the fault (i.e. passes for the fixed version and fails
for the buggy one) is provided.

* **requirements.txt** file which provides information on the required Python and library versions to reproduce the fault.

* **info.txt** file which contains information on the issue that was reported for the fault 
and the corresponding fixing commit.

 
