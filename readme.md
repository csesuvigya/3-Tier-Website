# MOVIE SEARCH WEB APPLICATION

## Overview

This is a simple web-based application that allows users to search for movies based on different criteria such as name, release year, and director/author. The application reads data from a locally stored CSV file and provides a user-friendly interface for searching and displaying results.

## Table of Contents

- Directory Structure
- Setup
- CSV File Format
- Usage

# DIRECTORY STRUCTURE

``` 
3 TIER WEBSITE
 -- templates
    |-- index.html          #Page containg a form for user interaction. 
    |-- results.html        #results page, to be redered when user searched something from the index.html
 -- app.py                  #python file containing the search logic
 -- data.csv                #CSV file containing the movies data
 -- readme.md  
``` 

# SETUP

## Install Dependencies

- First make sure that you have python installed. If not, use the below command.

> pip install python

- Install python flask by the following command.

> pip install flask

## Run The Application

- Navigate to the project directory.
- Run the Flask application using the following command from your terminal.

> python app.py

- Open your web browser and go to http://127.0.0.1:5000/ to access the application.

# CSV FILE FORMAT

The CSV file (data.csv) has the following columns:
- Title                 #title of the movie
- Type                  #Media type (in this case all are movies)
- Release Year          #release year of the movie
- Director/Author       #Director of that movie

Example CSV Data:
> The Matrix,Movie,1999,The Wachowskis
> The Lord of the Rings: The Return of the King,Movie,2003,Peter Jackson

# USAGE

## Enter Search Criteria:
- Enter the search keywords in the search box on the page.
- Select the search category from the drop down. Criteria can be any one of the following.
    - Title
    - Release Year
    - Director/Author

## Perform the Search:
- Click the "Search" button.

## View Results:
- The search results are displayed on a new page.

