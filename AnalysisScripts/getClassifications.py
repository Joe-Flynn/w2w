import mwapi
from revscoring import Model
from revscoring.extractors.api.extractor import Extractor
from revscoring.features import temporal, wikitext
from revscoring.languages import english
from util import read_labels_and_population_rates, read_observations

with open("models/enwiki.damaging.gradient_boosting.model") as f:
	dam_model = Model.load(f)

with open("models/enwiki.goodfaith.gradient_boosting.model") as f:
	gf_model = Model.load(f)

extractor = Extractor(mwapi.Session(host="https://en.wikipedia.org",
                                  user_agent="revscoring demo"))

observations = read_observations(open("./datasets/enwiki.labeled_revisions.w_cache.20k_2015.json"))

with open("damaging.csv", "wt") as dam_out, open("goodfaith.csv", "wt") as gf_out:
	n = 19396.0
	
	for i, ob in enumerate(observations):
		try:
			rev_id = ob["rev_id"]
			feature_values = list(extractor.extract(rev_id, gf_model.features))
			rev_id = str(rev_id)
			print(rev_id + " " + str((i * 1.0) / n))
			dam_out.write(rev_id + "," + str(dam_model.score(feature_values)["prediction"]) + "\n")
			gf_out.write(rev_id + "," + str(gf_model.score(feature_values)["prediction"]) + "\n")
		except:
			print("lost a rev")
