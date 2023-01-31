# Example Experiment - Single Sentence Reading

## Experiment

This repo provides an example PsychPy experiment (reading of single sentences) that includes various code snippets for running a basic eye-tracking experiment with SR-Research equipment.

## Update: January 2023

The example experiment already includes two routines for the transfer of EDF files from the host to the presentation PC. Either transfer and renaming of the temporary EDF file is done automatically after the experiment runs through as intended. Or, for cases in which an experiment must be interrupted through pressing "q" files are transferred and renamed with the addition "_aborted" to the file name.

Unfortunately, there were cases in which experiments crashed and neither of these two transfer routines worked. If these cases stayed unnoticed, potentially useful EDF files would have been overwritten by the next run of the experiment, because the temporary EDF file on the host PC was always initiated using the same Name (i.e., tempName.EDF). 

To avoid data loss, I have added a small function that creates a string of eight randomly chosen letters, which serves as the temporary file name for the EDF file on the host PC. Note, the host PC runs under the operation system DOS, which cannot handle file names longer than eight characters.

The following code elements were added to the first routine (i.e., "ET_setup"). First, in the tab "Before experiment" we make sure that two modules for creating the name for the temporary file are loaded:

``` python
import random
import string
```

In the same routine under the tab "Begin experiment" we a) define the function that creates the string of random letters, b) use this name to initiate the temporary EDF file and c) add the name to the PsychoPy log file so it can be assigned to a participant when it becomes necessary to transfer the file manually via the file manager.

```python
def get_random_string(length):
   letters = string.ascii_lowercase
   result_str = ''.join(random.choice(letters) for i in range(length))
   return result_str

# Writes temp file name into PsychPy log file 
logging.log(level=logging.EXP, msg=dataFileName)

# Opens an EDF data file on the host and writes a file header
# The file name should not exceed 8 characters
dataFileName = get_random_string(8) + '.EDF'
```
