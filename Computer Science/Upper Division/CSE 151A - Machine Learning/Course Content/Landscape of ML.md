#Machine-Learning 
# The 3 Learning Modalities
### Supervised Learning
- For solving **prediction problems**.
- For prediction problems, we consider **inputs and outputs**.
	- The input space is $\mathcal{X}$ and the output space is $\mathcal{Y}$, as before.
- After seeing a bunch of examples $(x, y)$, pick a mapping $f : \mathcal{X} \rightarrow \mathcal{Y}$ that accurately recovers the input-output pattern of the examples.
- Furthermore, prediction problems can be categorized by the type of output space: 
	- *Discrete* classification
		- Binary classification, like spam detection
		- Multiclass, like new article classification
		- Structured Outputs, like parsing sentences
	- *Continuous* regression
		- e.g. pollution level prediction or insurance company calculations
		- The key difference is that the outputs lie on a scale, so if one makes a wrong prediction, one knows how bad the prediction was, relatively speaking.
	- *Probability Values*
		- e.g. credit card transactions (probability of fraud)
		- Not a binary classification, because the ML outcome is simply a part of a larger decision making process that takes other numbers and inputs into account.
		- This actually is a kind of regression. *But*, we don't allow values outside $[0,1]$.

### Unsupervised Learning
- For finding good **representations**.
- Examples include clustering, projection, manifold learning, embedding, and generative modeling.

### Learning through Interaction
- e.g. reinforcement learning