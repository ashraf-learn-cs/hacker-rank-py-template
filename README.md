Hacker Rank
===========

Overview
--------
   This project include answers to all python problems found in [hackerrank](
    https://www.hackerrank.com/dashboard) website
    
### Environment Setting

1. **Create python virtual environment**

    ```
        // Open new terminal, select git bash and type following command
        python -m venv .venv
    ````

2. **Activate .venv environment**

   ```
        // type follwoing command
         source .venv/Scripts/activate
   

3. **Install required packages**
   ```
        // type follwoing command
        pip install pytest
   ```
    

4. **create requirements.txt file**
    ```
        // type following command
        pip freeze > requirements.txt
    ```
5. **Run pytest unit testing**
    ```
        // to run all unit test, open terminal and select Git Bash then type
        pytest -v

        // to run specific unit test file, open terminal and select Git Bash then type
        pytest tests/<test-file-name>_test.py -v
    ```

6. **Git commands cheat sheet**  
    https://education.github.com/git-cheat-sheet-education.pdf
