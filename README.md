# MSC harvester

The MSC harvester obtains Open [Mathematics Subject Classification (MSC)](https://zbmath.org/classification/) data from the [zbMATH Open](https://zbmath.org) [OAI-PMH](https://www.openarchives.org/pmh/)-[API](https://en.wikipedia.org/wiki/API) using the [Sickle client](https://github.com/mloesch/sickle).
The data is written to a csv file.
See [sample.csv](sample.csv) for an example.

The meaning of the columns is the following:

*de*: Internal zbMATH identifier (not to confuse with the zbl identifier)

*msc*: MSC of the article

*keywors*: keywords of the article

*title*: title of the article

*refs*: MSCs occouring in the references

By default only colums are exported with all values present.

### Notes on the de indentifier

One can navigate to the corresponding article in the zbMATH open webinterface by prefixing the string `https://zbmath.org/?an=0` to it.
For example for `de=1209934` navigate to https://zbmath.org/?an=01209934.
In rare cases there are de values below 1000000, if so as manny zeros have to be prefixed so that the final number in the url has eight digits.
