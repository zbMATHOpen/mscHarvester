from zbsickle.app import ZbPreviewSickle
from zbsickle.models import ZbPreviewRecord
import csv


def get_record(de: int):
    s = ZbPreviewSickle()
    r: ZbPreviewRecord = s.GetRecord(de=de)
    return r.get_title() + " by " + r.get_author() + " " + 'https://zbmath.org/?q=an:' + str(de)


with open('recommendation.csv') as csvfile:
    r = csv.DictReader(csvfile)
    lastSeed = ''
    position = 0
    for row in r:
        seed = row.get('seed')
        if lastSeed != seed:
            position = 0
            lastSeed = seed
            print("\nRecommendations for: " + get_record(seed))

        position += 1
        rec = row.get('recommendation')
        print(str(position) + ": " + get_record(rec))