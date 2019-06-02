Model Information:
	 - type: GradientBoosting
	 - version: 0.5.0
	 - params: {'scale': True, 'center': True, 'labels': [True, False], 'multilabel': False, 'population_rates': None, 'criterion': 'friedman_mse', 'init': None, 'learning_rate': 0.01, 'loss': 'deviance', 'max_depth': 7, 'max_features': 'log2', 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 700, 'presort': 'auto', 'random_state': None, 'subsample': 1.0, 'verbose': 0, 'warm_start': False, 'label_weights': OrderedDict([(False, 10)])}
	Environment:
	 - revscoring_version: '2.3.4'
	 - platform: 'Linux-4.15.0-50-generic-x86_64-with-Ubuntu-18.04-bionic'
	 - machine: 'x86_64'
	 - version: '#54-Ubuntu SMP Mon May 6 18:46:08 UTC 2019'
	 - system: 'Linux'
	 - processor: 'x86_64'
	 - python_build: ('default', 'Sep 12 2018 18:26:19')
	 - python_compiler: 'GCC 8.0.1 20180414 (experimental) [trunk revision 259383'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.6.6'
	 - release: '4.15.0-50-generic'
	
	Statistics:
	counts (n=19396):
		label        n         ~True    ~False
		-------  -----  ---  -------  --------
		True     18855  -->    18484       371
		False      541  -->      278       263
	rates:
		              True    False
		----------  ------  -------
		sample       0.972    0.028
		population   0.967    0.033
	match_rate (micro=0.934, macro=0.5):
		  True    False
		------  -------
		 0.965    0.035
	filter_rate (micro=0.066, macro=0.5):
		  True    False
		------  -------
		 0.035    0.965
	recall (micro=0.964, macro=0.733):
		  True    False
		------  -------
		  0.98    0.486
	!recall (micro=0.502, macro=0.733):
		  True    False
		------  -------
		 0.486     0.98
	precision (micro=0.965, macro=0.719):
		  True    False
		------  -------
		 0.983    0.456
	!precision (micro=0.473, macro=0.719):
		  True    False
		------  -------
		 0.456    0.983
	f1 (micro=0.965, macro=0.726):
		  True    False
		------  -------
		 0.981    0.471
	!f1 (micro=0.487, macro=0.726):
		  True    False
		------  -------
		 0.471    0.981
	accuracy (micro=0.964, macro=0.964):
		  True    False
		------  -------
		 0.964    0.964
	fpr (micro=0.498, macro=0.267):
		  True    False
		------  -------
		 0.514     0.02
	roc_auc (micro=0.92, macro=0.919):
		  True    False
		------  -------
		  0.92    0.919
	pr_auc (micro=0.978, macro=0.723):
		  True    False
		------  -------
		 0.996     0.45
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'boolean'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'true': {'type': 'number'}, 'false': {'type': 'number'}}}}}

