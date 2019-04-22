from mwapi import Session
from revscoring.extractors import api
from revscoring.features import temporal, wikitext
from revscoring import Feature
import mwparserfromhell as mwp
from revscoring.languages import english
from revscoring import Model

session = Session("https://en.wikipedia.org/w/api.php", user_agent="joe")
extractor = api.Extractor(session)

with open("/home/jospeh/Desktop/code and other stuff/edit-qualities/editquality-master (with cliches)/models/enwiki.damaging.gradient_boosting.model") as f:
	dam_model1 = Model.load(f)

with open("/home/jospeh/Desktop/code and other stuff/edit-qualities/editquality-master (without puffery)/models/enwiki.goodfaith.gradient_boosting.model") as f:
	dam_model2 = Model.load(f)



with open("dam_missIds", "rt") as revs:

	for rev in revs.readlines():
		
		print("--------------------")
     
		print(extractor.extract(int(rev), wikitext.revision.diff.datasources.segments_added))
		feature_values = list(extractor.extract(int(rev), dam_model1.features))
		print(str(dam_model1.score(feature_values)["prediction"]))
		feature_values = list(extractor.extract(int(rev), dam_model2.features))
		print(str(dam_model2.score(feature_values)["prediction"]))
		print(extractor.extract(int(rev), wikitext.revision.diff.datasources.segments_removed))
		print("--------------------")
