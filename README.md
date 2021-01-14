# InsightExtractor


The Insight Extractor was the ML model that Considdr used to idenitfy abstractive sentences in full text documents on the web. Considdr closed in the summer of 2020 and now we're making our model freely available to all.


## Background ##

What if I told you our insight extraction model was just like having an expert:
- spend a lifetime gaining context in a given discipline
- read through a full text document or any source of information and identify the most important bits
- write a concise abstractive summary statement reflecting the key insights

Pretty great, right? Well, our model isn't that expert, but it does identify the output of the work that an expert (or many) has already done in citing a document. Think about it: when someone cites something they (ideally) have a lot of contextual understanding of the field they are in; have meticulously read the document in question and much of the many relevant related documents; they've done the work of figuring out what is most important in that the document; and then they write a nice concise summary of a key insight in the sentences around where they cite it in their own work.

Instead of repeating these steps as a non-expert and, honestly, do them less well, why can't we just leverage the work that's already been done?

At Considdr, we called this new approach to insight extraction "Summarization by Adjacent Document" because we don't look at Document A to generate a summary for Document A, but instead we look at Documents B, C, and D, which cite Document A, to find one or many insight sentences (places where those authors have abstracted the key points from another work). 

In fact, because we can leverage many documents at once, we can more easily identify variation in citations and understand what insights are most important/most cited. We built a second model to do just that at Considdr. It clusters sentences to figure out when multiple authors are citing the same insight. To do this we tuned the SoTA model that matched Quora Question Pairs (see: https://www.kaggle.com/c/quora-question-pairs). Unfortunately, this model relied on a massive database of more than 3 million extracted insights that we could not longer afford to maintain -- so it's not included in the package here. This package only includes the first model that we used to feed insights into our second clustering model.

Even though our company didn't survive we hope that our work can be of use to someone else. Feel free to borrow and adapt our model and our insight extraction approach for any purpose that might make the world a better place. We just asked that you please cite and link back to this repo.

- Noah and Marcus


### How to run the model ###




### Training Data ###




### Acknowledgements ###

