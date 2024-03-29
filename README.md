# Keep up to date with the new reasearch calls from MINCIENCIAS

The aim of this repository is to send an mail with the new calls for research projects from [MINCIENCIAS Colombia](https://minciencias.gov.co). 


## Description of files in this repository:

It has a main module called `minciencias_convoc.py` which read the calls from [MINCIENCIAS webpage](https://minciencias.gov.co/convocatorias/todas) each period of time. It sends a mail if there is new calls with respect to the last read. 


## Installation

**NOTE:** *This project was made in* ***Python 3.10.6***

0. Create a folder to put the project and the virtual enviroment

1. Clone the repository inside the folder
   ```sh 
   git clone https://github.com/LinaMRuizG/minciencias_convocatorias.git
   ```
2. Create the virtual enviroment inside the same folder 
   ```sh 
   virtualenv venv
   ```
3. Activate the virtual environment
   ```sh 
   source /path/to/venv/bin/activate
   ```
3. Install the required libraries 
   ```sh 
   pip install -r requirements.txt
   ```
4. Use the `exexution.py` to run the code and set the receiver mails and other attributes

## Running

### Running once 

Use the `exexution.py` to run the code 

### Running multiple times automatically

You can use the following command to run the code automatically from bash every certain period of time:

   ```sh 
   source execution.sh
   ```

### Running in a server

1. Review the `screen` version 

   ```sh 
   screen --version
   ```

2. Create a screen 
   
   ```sh 
   screen -S nameOfTheScreen
   ```

3. Run the file

   ```sh 
   source execution.sh
   ```

4. Get out of the screen session

   ```sh 
   Ctrl + a + d
   ```
5. List the screen in memory

```sh 
   screen -ls
```

6. Get into the screen session 

```sh
   screen -x nameOfTheScreen
```

7. Delete the screen

```sh 
   screen -X -S nameOfTheScreen quit
```


## Contributing

This project is in progress and it requires some improvments. Therefore, if you have any suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/improvments`)
3. Commit your Changes (`git commit -m 'Add some improvment`)
4. Push to the Branch (`git push origin feature/improvments`)
5. Open a Pull Request

## Contact

* [Lina M Ruiz G](https://co.linkedin.com/in/lina-marcela-ruiz-galvis-465896209) - lina.ruiz2@udea.edu.co

## Acknowledgments
* [Anderson Alexis Ruales Barbosa](https://co.linkedin.com/in/anderson-alexis-ruales-b27638199?original_referer=https%3A%2F%2Fwww.google.com%2F)

    
    
    
    
   




