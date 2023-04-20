- Some people worry about privacy
- Data is a form of power, and it can be considered as money
- Ethics are moral principles that govern a person's behaviour or the conducting of an activity

Prof Fleischer's view: Data sci pursued in a manner so that is equitable, with respect for privacy and consent, so as to ensure that it does not cause undue harm.

Intent and Objectivity
- intent is not required for harmful practices to occur
- data, algo, and analysis are not objective
	- it is collected and implemented by people, who have biases
- bias & discrimination driven by data & algorithms can give new scale to pre-existing inequities

# Nine things to consider to not ruin people's lives with data science
### Question
- what is the question? is it well-posed?
- do you know something about the context and background of the question?
- scope of investigation? What correlations are we inadvertently tracking? possible to answer this question well?
### Implication
- who are the stakeholders? how does this affect them?
- could the information you will gain and/or the tool you are building be co-opted for nefarious purposes?
	- can you protect them from that?
- have you considered potential unintended consequences?
### Data
- is there data available? is this data directly related to your question or only potentially through proxies?
- who do you have data fram?
- do you have enough data to make reliable inferences?
- what biases do the data have?
- might have to stop if conditions fail...
### Informed Consent
- the voluntary agreement to participate in research, in which the subject has an understanding of the research and its risks
- this consent can be withdrawn at any point in time
### Privacy
- can you guarantee privacy?
- what is the level of risk of your data? are all subjects equally vulnerable?
- anonymization: process of removing personally identifiable infromation from datasets (PII)
- secure data storage, with appropriate access rights
### Evaluation
- is there a metric of success?
- goodhart's law: when a measure becomes a target, it ceases to be a good measure. 
### Analysis
- Do your analyses reflect spurious correlations? Tease apart causation?
- Tracking covariates?
	- Inferring latent variables from proxies?
	- Spurious Correlations
### Transparency & Appeal
- Is the model a black box? interpretable as to how it came to any particular decision?
- is there a way to appeal a model decision? what kind of evidence would you need to refute a decision?
### Continuous Monitoring
- healthy models maintain a back and forth with the things in the world they are trying to understand.
- tracking changes related to data, assumptions, and evaluation metric?
- proactively looking for portential unintended side effects of the model itself or harmful outputs?
- is there a mechanism to fix and update your algorithm?