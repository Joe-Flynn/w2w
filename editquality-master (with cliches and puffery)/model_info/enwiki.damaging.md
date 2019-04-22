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
	counts (n=19396):
		label        n         ~True    ~False
		-------  -----  ---  -------  --------
		True       673  -->      342       331
		False    18723  -->      656     18067
	rates:
		              True    False
		----------  ------  -------
		sample       0.035    0.965
		population   0.034    0.966
	match_rate (micro=0.918, macro=0.5):
		  True    False
		------  -------
		 0.051    0.949
	filter_rate (micro=0.082, macro=0.5):
		  True    False
		------  -------
		 0.949    0.051
	recall (micro=0.949, macro=0.737):
		  True    False
		------  -------
		 0.508    0.965
	!recall (micro=0.524, macro=0.737):
		  True    False
		------  -------
		 0.965    0.508
	precision (micro=0.96, macro=0.661):
		  True    False
		------  -------
		 0.339    0.982
	!precision (micro=0.361, macro=0.661):
		  True    False
		------  -------
		 0.982    0.339
	f1 (micro=0.954, macro=0.69):
		  True    False
		------  -------
		 0.407    0.974
	!f1 (micro=0.426, macro=0.69):
		  True    False
		------  -------
		 0.974    0.407
	accuracy (micro=0.949, macro=0.949):
		  True    False
		------  -------
		 0.949    0.949
	fpr (micro=0.476, macro=0.263):
		  True    False
		------  -------
		 0.035    0.492
	roc_auc (micro=0.918, macro=0.917):
		  True    False
		------  -------
		 0.916    0.918
	pr_auc (micro=0.976, macro=0.698):
		  True    False
		------  -------
		 0.399    0.996
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'boolean'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'true': {'type': 'number'}, 'false': {'type': 'number'}}}}}

