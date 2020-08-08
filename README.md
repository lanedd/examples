[[_TOC_]]

1. Windows OS
    1. Conda working inside of Git Bash terminal.  Allows Linux command line like interface with access to Python.
        - Type this command into Git Bash `echo ". C:\Users\ldalan\AppData\Local\Continuum\anaconda3\etc\profile.d\conda.sh" >> ~/.profile`
            - Might be `/C/Users/ldalan/AppData/Local/Continuum/anaconda3/etc/profile.d/conda.sh` instead?
            - This path is dependent on which version of Conda was installed etc.  Basically find where the `etc/profile.d/conda.sh` is located.
            - Possible way of finding the location is: 
                - Type in `conda info --envs` to Git Bash
                - Possible output: 
                    ```
                    # conda environments:
                    #
                    base                  *  C:\Users\ldalan\AppData\Local\Continuum\anaconda3
                    ```
                - Then add the `etc/profile.d/conda.sh` to find the conda location.
        - The above command will give access to Conda for newly created Git Bash terminals.
        - Close and reopen the Git Bash terminal for the change to take affect.  
            - Type `conda` into the Git Bash terminal to check if it worked 
    2. Run Python from shell script like documents.  Allows you to run Python scripts from a linux like script.
        - See above to get Conda working in Git Bash
        - In shell script (.sh) create and use variables:
            ```
            CONDA_PATH='/C/Users/ldalan/AppData/Local/Continuum/anaconda3/etc/profile.d/conda.sh'
            CONDA_ENV='pipeline_script'
            source ${CONDA_PATH}
            conda activate $CONDA_ENV
            ```
            
                 
        