'''
Following Chapter 2: Python for DataAnalysis
'''
import json
path = 'usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]

print records[0]['tz']

from collections import Counter

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
counts = Counter(time_zones)
