# Get coordinates of brain regions

Scripts for getting coordinates of Acronym using AllenSDK.
The coordinates are calculated by taking average over injection coordinates of experiments.

## Devleopment Environment

* Python 2.7.9

## Instruction

```
$ git clone https://github.com/kiyomaro927/getcoordinate.git
$ cd getcoordinate/
$ pip install allensdk
```

## Preparation of dataset

Download [this dataset](http://www.nature.com/nature/journal/v508/n7495/extref/nature13186-s2.xlsx),
and save the second sheet __as a csv file__ in the __datasets__ directory.

## Run

```
$ python node_runner.py
```
