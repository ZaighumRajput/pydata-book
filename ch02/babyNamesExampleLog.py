# IPython log file

get_ipython().magic(u'ls ')
get_ipython().magic(u'log')
get_ipython().magic(u'logstart')
get_ipython().system(u'head -n 10 names/yob1880.txt')
import pandas as pd
names1880 = pd.read_csv('names/yob1880.txt', names = ['name', 'tsex', 'births'])
names1880
names1880.groupby('sex').births.sum()
names1880.groupby('sex').births.sum()
names1880 = pd.read_csv('names/yob1880.txt', names = ['name', 'sex', 'births'])
names1880.groupby('sex').births.sum()
years = range(1880, 2011)
pieces = []
columns = ['names', 'sex', 'births']
for year in years:
    path = 'names/yob%d.txt' % year
    frame = pd.read_csv(path, names = columns)
    
for year in years:
    path = 'names/yob%d.txt' % year
    frame = pd.read_csv(path, names = columns)
    
pieces
frame['year'] = year
pieces.append(frame)
names = pd.concat(pieces, ignore_index=True)
names
names
total_births = names.pivot_table('births', rows='year', cols='sex', aggfunc=sum)
total_births
years = range(1880, 2011)
years
columns
for year in years:
    path = 'names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year']=year
    pieces.append(frame)
    names = pd.concat(pieces, ignore_index=True)
    
names
get_ipython().magic(u'pinfo names')
total_births = names.pivot_table('births', rows='year', cols='sex', aggfunc=sum)
total_births.tail()
total_births.head()
total_births.plot(title = 'Total births by sex and year')
total_births.tail()
get_ipython().magic(u'ls ')
get_ipython().magic(u'who')
delete total_births
get_ipython().magic(u'del total_births')
del total_births
get_ipython().magic(u'who')
frame
del frames
del frame
for year in years:
    path = 'names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year']=year
    pieces.append(frame)
    names = pd.concat(pieces, ignore_index=True)
    
total_births = names.pivot_table('births', rows='year', cols='sex', aggfunc=sum)
total_births
total_births.head()
total_births.tail()
total_births.plot(title = 'Total births by sex and year')
get_ipython().magic(u'who')
del names1880
del pieces
del total_births
del frame
del names
get_ipython().magic(u'ls ')
get_ipython().magic(u'who')
columns
years
get_ipython().magic(u'who')
path
del path
years = range(1880, 2011)
for year in years:
    path = 'names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)
    
pieces =[]
for year in years:
    path = 'names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)
    
pieces
pieces.head
pieces.head()
pieces[:10]
names = pd.concat(pieces, ignore_index=True)
names
total_births = names.pivot_table('births', rows = 'years', cols = 'sex', aggfunc=sum)
total_births = names.pivot_table('births', rows = 'year', cols = 'sex', aggfunc=sum)
total_births.tail()
total_births.plot(title='Total births by sex and year')
get_ipython().magic(u'ls ')
quit()
