import mwapi
from revscoring import Model
from revscoring.extractors.api.extractor import Extractor
from revscoring.features import temporal, wikitext
from revscoring.languages import english

with open("models/enwiki.damaging.gradient_boosting.model") as f:
	scorer_model = Model.load(f)

extractor = Extractor(mwapi.Session(host="https://en.wikipedia.org",
                                  user_agent="revscoring demo"))

#with puffery
feature_values = list(extractor.extract(886029951, scorer_model.features))
print(scorer_model.score(feature_values));

#without puffery
feature_values = list(extractor.extract(886029699, scorer_model.features))
print(scorer_model.score(feature_values));

with open("models/enwiki.goodfaith.gradient_boosting.model") as f:
	scorer_model = Model.load(f)

extractor = Extractor(mwapi.Session(host="https://en.wikipedia.org",
                                  user_agent="revscoring demo"))
#with puffery
feature_values = list(extractor.extract(886029951, scorer_model.features))
print(scorer_model.score(feature_values));

#without puffery
feature_values = list(extractor.extract(886029699, scorer_model.features))
print(scorer_model.score(feature_values));
