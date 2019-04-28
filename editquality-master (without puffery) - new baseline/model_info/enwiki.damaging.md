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
		True       673  -->      340       333
		False    18723  -->      647     18076
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
	recall (micro=0.95, macro=0.735):
		  True    False
		------  -------
		 0.505    0.965
	!recall (micro=0.521, macro=0.735):
		  True    False
		------  -------
		 0.965    0.505
	precision (micro=0.96, macro=0.662):
		  True    False
		------  -------
		 0.341    0.982
	!precision (micro=0.363, macro=0.662):
		  True    False
		------  -------
		 0.982    0.341
	f1 (micro=0.954, macro=0.69):
		  True    False
		------  -------
		 0.407    0.974
	!f1 (micro=0.426, macro=0.69):
		  True    False
		------  -------
		 0.974    0.407
	accuracy (micro=0.95, macro=0.95):
		  True    False
		------  -------
		  0.95     0.95
	fpr (micro=0.479, macro=0.265):
		  True    False
		------  -------
		 0.035    0.495
	roc_auc (micro=0.918, macro=0.918):
		  True    False
		------  -------
		 0.917    0.918
	pr_auc (micro=0.976, macro=0.696):
		  True    False
		------  -------
		 0.395    0.996
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'boolean'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'true': {'type': 'number'}, 'false': {'type': 'number'}}}}}

