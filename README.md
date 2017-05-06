# Get coordinates of brain regions

## Instruction

```
$ pyenv install anaconda-2.3.0
$ pyenv local anaconda-2.3.0
$ pip install allensdk
```

## Preparation of dataset

Download [this dataset](http://www.nature.com/nature/journal/v508/n7495/extref/nature13186-s2.xlsx),
and save it __as a csv file__ in the datasets directory.

## Run

```
$ python node_runner.py 
```

## Runtime option

```
$ python node_runner.py -query QUERY_WORD
```
