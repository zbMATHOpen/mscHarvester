# MSC harvester

The MSC harvester obtains Open [Mathematics Subject Classification (MSC)](https://zbmath.org/classification/) data from the [zbMATH Open](https://zbmath.org) [OAI-PMH](https://www.openarchives.org/pmh/)-[API](https://en.wikipedia.org/wiki/API) using the [Sickle client](https://github.com/mloesch/sickle).
The data is written to a csv file.
See [sample.csv](sample.csv) for an example.

The meaning of the columns is the following:

*de*: Eight digit internal zbMATH identifier (not to confuse with the public zbl identifier in the form  Zbl 0910.34036)

*msc*: MSC of the article

*keywors*: keywords of the article

*title*: title of the article

*refs*: MSCs occouring in the references

By default only colums are exported with all values present.

### Notes on the de indentifier

One can navigate to the corresponding article in the zbMATH open webinterface by prefixing the string `https://zbmath.org/?an=0` to it.
For example for `de=1209934` navigate to https://zbmath.org/?an=01209934.
In rare cases there are de values below 1000000, if so as manny zeros have to be prefixed so that the final number in the url has eight digits.
To retrive the de from the zbMATH Open website a little trick is required:
One can obtain the de this by clicking on the BibTeX button below the article.
For this example, a BibTeX entry with key `zbMATH01209934` will be downloaded.
The last digits after the word zbMATH, i.e., 1209934, are the DE number. 

### Links and references

* [zbMATH OAI-PMH Api](https://oai.zbmath.org/)

* [M. Schubotz and O. Teschke, zbMATH Open: Towards standardized machine interfaces to expose bibliographic metadata. EMS Magazine 119, 50–53 (2021)](https://euromathsoc.org/magazine/2021/119/mag-12)

* [M. Petrera, I. Beckenbach, D. Ehsani, F. Müller, O. Teschke, B. Gipp, and M. Schubotz, zbMATH Open: API Solutions and Research Challenges. ArXiv, abs/2106.04664 (2021)](https://arxiv.org/abs/2106.04664)

* [M. Schubotz, P. Scharpf, O. Teschke, A. Kühnemund, C. Breitinger, B. Gipp, AutoMSC: Automatic Assignment of Mathematics Subject Classification Labels, Intelligent Computer Mathematics - 13thInternational Conference, CICM 2020, Bertinoro, Italy, July 26-31, 2020, Proceedings](https://arxiv.org/pdf/2005.12099.pdf) [DOI](https://doi.org/10.1007/978-3-030-53518-6_15)
