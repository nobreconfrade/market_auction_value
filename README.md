# market_auction_value

Hello, this is the code for the market auction value challenge. Here in the
README are all the instructions needed to run the code on your environment.

## First things first
- Ensure you have [miniconda installed](https://docs.conda.io/en/latest/miniconda.html)
- If on Linux distro, run the following command on your bash terminal: source RUNME.sh
    - The previews command will set up some env vars, but you can do it manually if desired.

## To run the app
With the miniconda installed and with the environment activated (`conda env create -f environment.yml` 
and `conda activate market_auction_value`) simply run on root:
    
    flask run

## To run the unit tests
With environment activated run on root:
  
    pytest -v