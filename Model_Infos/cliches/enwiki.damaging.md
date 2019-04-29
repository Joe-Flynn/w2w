Model Information:
	 - type: GradientBoosting
	 - version: 0.5.0
	 - params: {'scale': True, 'center': True, 'labels': [True, False], 'multilabel': False, 'population_rates': None, 'criterion': 'friedman_mse', 'init': None, 'learning_rate': 0.01, 'loss': 'deviance', 'max_depth': 7, 'max_features': 'log2', 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 700, 'presort': 'auto', 'random_state': None, 'subsample': 1.0, 'verbose': 0, 'warm_start': False, 'label_weights': OrderedDict([(True, 10)])}
	Environment:
	 - revscoring_version: '2.3.4'
	 - platform: 'Linux-4.15.0-47-generic-x86_64-with-Ubuntu-18.04-bionic'
	 - machine: 'x86_64'
	 - version: '#50-Ubuntu SMP Wed Mar 13 10:44:52 UTC 2019'
	 - system: 'Linux'
	 - processor: 'x86_64'
	 - python_build: ('default', 'Sep 12 2018 18:26:19')
	 - python_compiler: 'GCC 8.0.1 20180414 (experimental) [trunk revision 259383'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.6.6'
	 - release: '4.15.0-47-generic'
	
	Statistics:
	counts (n=19398):
		label        n         ~True    ~False
		-------  -----  ---  -------  --------
		True       673  -->      351       322
		False    18725  -->      635     18090
	rates:
		              True    False
		----------  ------  -------
		sample       0.035    0.965
		population   0.034    0.966
	match_rate (micro=0.919, macro=0.5):
		  True    False
		------  -------
		 0.051    0.949
	filter_rate (micro=0.081, macro=0.5):
		  True    False
		------  -------
		 0.949    0.051
	recall (micro=0.951, macro=0.744):
		  True    False
		------  -------
		 0.522    0.966
	!recall (micro=0.537, macro=0.744):
		  True    False
		------  -------
		 0.966    0.522
	precision (micro=0.961, macro=0.668):
		  True    False
		------  -------
		 0.352    0.983
	!precision (micro=0.374, macro=0.668):
		  True    False
		------  -------
		 0.983    0.352
	f1 (micro=0.955, macro=0.697):
		  True    False
		------  -------
		 0.421    0.974
	!f1 (micro=0.439, macro=0.697):
		  True    False
		------  -------
		 0.974    0.421
	accuracy (micro=0.951, macro=0.951):
		  True    False
		------  -------
		 0.951    0.951
	fpr (micro=0.463, macro=0.256):
		  True    False
		------  -------
		 0.034    0.478
	roc_auc (micro=0.918, macro=0.918):
		  True    False
		------  -------
		 0.918    0.918
	pr_auc (micro=0.976, macro=0.698):
		  True    False
		------  -------
		 0.399    0.997
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'boolean'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'true': {'type': 'number'}, 'false': {'type': 'number'}}}}}

