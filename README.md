# introToMLapps
Any work I have completed from my Intro to Machine Learning Applications Course at RPI

Final Project Overview:
Problem Statement:
   Do external factors affect the stock market, if so, how much is performance affected
   Are the stock prices an indicator of the environment?

   What I define as external factors:
      1. Politics
      2. Economy
      3. Physical environment
         -i.e. pollution
   We will look at the following external factors:
      1. Politics
         *Recent & Significant (2020 to 2023)
         -Russian-Ukranian conflict
         Note: Due to lack of recent data on the CCPI, ECPI, GSCPI, etc we will only look at values from 2010 to early 2023
      2. Economy
         *Recent (2020 to 2023)
         - COVID-19
            a) Supply Chain issues caused
      3. Physical environment
         - Crackdown on combustion engine vehicles and push towards electric vehicles
         - General environmental sentiment moving towards sustainability

   Datasets used:
      U.S. Bureau of Labor Statistics-
      1. Core Consumer Price Index (CCPI)
      2. Environmental Consumer Price Index (ECPI)
      OECD Statistics-
      1. Environmental Policy Stringency Index(EPSI)
      Federal Reserve Bank of New York-
      1. Global Supply Chain Pressure Index (GSCPI)

   Other Resources:
   1. https://towardsdatascience.com/analyzing-world-stock-indices-performance-in-python-610df6a578f?gi=7d0581681a45
   2. https://finance.yahoo.com/world-indices/
   3. ChatGPT
   4. https://stackoverflow.com/questions/26105804/extract-month-from-date-in-python

Author's Thoughts:
   If I were to redo this project with more foreward thinking and more time, I would do many things. First, I would approach the issue of outliers in a more technical manner. The reason I didn't was the fear of losing datapoints that could potentially be valid, despite this I still took a very novice approach. Furthermore, I would attack the issue and redundancy of repeated country-date datapoints. The merged dataset contained many datapoints that had the same country and date but slightly different CCPI, ECPI, etc, so I was again a bit scared to acknowledge this problem in my work. Now for what I consider my largest failure, the models. Honestly, this problem, although simple from a data science perspective, was incredibly difficult for me to incorporate models into due to the inconsistent training sizes, and not intuitive ways of building said models. I tried what I could, however the second question of the problem statement was answered using more data analysis and science esque techniques than a pure model perspective due to my difficulty. Nonetheless, this project taught me so much about the application of models to a complex problem, how to effectively use Python libraries to complete tasks, and follow a workflow (using GitHub). The project 100 percent has it's flaws, but hopefully anyone reading enjoyed or found this useful. Feel free to leave criticism and/or reccomendations, always learning!
