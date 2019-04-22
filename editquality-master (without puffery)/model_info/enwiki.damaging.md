Model Information:
	 - type: GradientBoosting
	 - version: 0.5.0
	 - params: {'scale': True, 'center': True, 'labels': [True, False], 'multilabel': False, 'population_rates': None, 'criterion': 'friedman_mse', 'init': None, 'learning_rate': 0.01, 'loss': 'deviance', 'max_depth': 7, 'max_features': 'log2', 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 700, 'presort': 'auto', 'random_state': None, 'subsample': 1.0, 'verbose': 0, 'warm_start': False, 'label_weights': OrderedDict([(True, 10)])}
	Environment:
	 - revscoring_version: '2.3.4'
	 - platform: 'Linux-4.15.0-45-generic-x86_64-with-Ubuntu-18.04-bionic'
	 - machine: 'x86_64'
	 - version: '#48-Ubuntu SMP Tue Jan 29 16:28:13 UTC 2019'
	 - system: 'Linux'
	 - processor: 'x86_64'
	 - python_build: ('default', 'Sep 12 2018 18:26:19')
	 - python_compiler: 'GCC 8.0.1 20180414 (experimental) [trunk revision 259383'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.6.6'
	 - release: '4.15.0-45-generic'
	
	Statistics:
	counts (n=19410):
		label        n         ~True    ~False
		-------  -----  ---  -------  --------
		True       673  -->      345       328
		False    18737  -->      613     18124
	rates:
		              True    False
		----------  ------  -------
		sample       0.035    0.965
		population   0.034    0.966
	match_rate (micro=0.92, macro=0.5):
		  True    False
		------  -------
		 0.049    0.951
	filter_rate (micro=0.08, macro=0.5):
		  True    False
		------  -------
		 0.951    0.049
	recall (micro=0.952, macro=0.74):
		  True    False
		------  -------
		 0.513    0.967
	!recall (micro=0.528, macro=0.74):
		  True    False
		------  -------
		 0.967    0.513
	precision (micro=0.961, macro=0.67):
		  True    False
		------  -------
		 0.357    0.982
	!precision (micro=0.378, macro=0.67):
		  True    False
		------  -------
		 0.982    0.357
	f1 (micro=0.956, macro=0.698):
		  True    False
		------  -------
		 0.421    0.975
	!f1 (micro=0.44, macro=0.698):
		  True    False
		------  -------
		 0.975    0.421
	accuracy (micro=0.952, macro=0.952):
		  True    False
		------  -------
		 0.952    0.952
	fpr (micro=0.472, macro=0.26):
		  True    False
		------  -------
		 0.033    0.487
	roc_auc (micro=0.918, macro=0.917):
		  True    False
		------  -------
		 0.917    0.918
	pr_auc (micro=0.976, macro=0.7):
		  True    False
		------  -------
		 0.404    0.996
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'boolean'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'true': {'type': 'number'}, 'false': {'type': 'number'}}}}}

