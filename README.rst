Insight Extractor
=================


.. image:: https://pepy.tech/badge/insight-extractor
    :target: https://pepy.tech/project/insight-extractor
.. image:: https://travis-ci.com/NoahFinberg/insight_extractor.svg?branch=main
    :target: https://travis-ci.com/NoahFinberg/insight_extractor

The Insight Extractor was the ML model that `Considdr <https://medium.com/considdr-history>`_ used to idenitfy abstractive sentences in full text documents on the web. Considdr closed in the summer of 2020 and now we're making our model freely available to all. We'd love to hear the interesting ways people apply this model. All we ask is that you cite this repo.

Abstractive sentences are of particular value when it comes to understanding the key insights in adjacent documents. For more on this summarization approach see `"Summarization by Adjacent Document." <https://medium.com/considdr-history>`_

Install
-------

.. code-block::

   pip install insight_extractor


**Notes:** 


* We use Tensorflow 2.X and recommend using Python 3.6 or higher.
* Python 2 is not supported

Using insight_extractor
-----------------------

v0.1.0 of insight_extractor exposes one primary function --\ ``extract_insights`` -- which takes a list of candidate insight sentences and returns  a list of prediction scores ``[prob(not an insight), prob(yes an insight)]``.`

**Input:**

.. code-block::

   # given a list of input sentences
   sentences = [
       'According to the most recent statistics, more than a million people a year are arrested for simple drug possession in the United States -- and more than half a million of those arrests are for marijuana possession.',
       'One study found that for cancer patients considering experimental chemotherapy, trust in their physician was one of the most important reasons they enrolled in a clinical trial -- on par with the belief that the treatment would be effective.',
       'Senate leaders were working to agree on a dual track to try the departing president at the same time it considered the agenda of the incoming one, an exercise never tried before.',
   ]


**Insight Extraction**

.. code-block::

   # import
   from insight_extractor.pipeline import extract_insights

   # get insight predictions
   predictions = extract_insights(sentences)

   # print predictions
   print(predictions)


**Output:**

.. code-block::

   array([[0.28326818, 0.7167318 ],
      [0.3710433 , 0.6289567 ],
      [0.9886193 , 0.01138071]], dtype=float32)


**Notes on Interpretation**

Of the three sample input sentences, we would define the first two as an "insight", but not the last sentence. As you can see our model predicts that the first and second sample sentences are insights with a probability of ~72% and ~63% respectively. 

Generally most sentences in a given article are not insight sentences. However, some sentences are more "abstractive" than others. In practice, we found that most sentences predicted with >10% probability of being an insight often have at least some abstractive value. You may want to fiddle with the threshold given your use-case and tolerance for False Positives. 

Notes
-----

v0.1.0 is really the bare minimum functionality of the Considdr insight model. 


#. In the actual production implementation we took as inputs entire articles (html pages) and returned insight sentences from that article.
#. We leveraged the fact that multiple documents often abstract the same works and built a second much more complex model to cluster similar insights together.
#. We also trained various versions of our model on academic documents when we built out proof of concepts for academic search engines that were interested in our technology. Citation structure enables a very clear extension of our summarization by adjacent document approach.

Over time, we plan to update this package to better reflect the robustness of the Considdr product. Collaborators and contributors are welcome. 

Acknowledgements
----------------

This insight extraction model benefitted from the hard work of many of our team members at Considdr. In particular, hand labeling thousands and thousands of sentences and cross-validating those labels across members of our team was an especially grueling effort. Thank you to Hailey Wahl, Kevin Lane, Derek Yau, and Eddie Korando for all your help here.

We also heavily utilized the following resources in build our CNN model.


* The fantastic paper by Yoon Kim `"Convolutional Neural Networks for Sentence Classification" <https://arxiv.org/abs/1408.5882>`_
* The TF 1 implementation of Dr. Kim's work by `Denny Britz <http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/>`_
* The TF 2 implementation by `Christopher Masch <https://github.com/cmasch/cnn-text-classification>`_

Authors
-------

Noah Finberg and Marcus Christiansen

License
-------

The package is released under the `MIT License. <https://opensource.org/licenses/MIT>`_
