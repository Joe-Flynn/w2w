import mwapi
from revscoring import Model
from revscoring.extractors.api.extractor import Extractor
from revscoring.features import temporal, wikitext
from revscoring.languages import english

# put your rev_id here 
revId = 886029951

with open("models/enwiki.damaging.gradient_boosting.model") as f:
	scorer_model = Model.load(f)

extractor = Extractor(mwapi.Session(host="https://en.wikipedia.org",
                                  user_agent="revscoring demo"))

feature_values = list(extractor.extract(revId, scorer_model.features))
print("DAMAGING:")
print(scorer_model.score(feature_values));

with open("models/enwiki.goodfaith.gradient_boosting.model") as f:
	scorer_model = Model.load(f)

extractor = Extractor(mwapi.Session(host="https://en.wikipedia.org",
                                  user_agent="revscoring demo"))

feature_values = list(extractor.extract(revId, scorer_model.features))
print("GOODFAITH:")
print(scorer_model.score(feature_values));
