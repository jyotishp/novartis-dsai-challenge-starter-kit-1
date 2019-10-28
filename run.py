#!/usr/bin/env python
import random
import json
import numpy as np
import pandas as pd
import argparse
import base64

import aicrowd_helpers
import time
import traceback

import glob
import os
import json

import tqdm


"""
################################################################################################################
################################################################################################################
## Expected ENVIRONMENT Variables
################################################################################################################

* AICROWD_TEST_DATA_PATH : Absolute Path to the Test CSV file
* AICROWD_PREDICTIONS_OUTPUT_PATH  : path where you are supposed to write the output predictions.csv
"""
AICROWD_TEST_DATA_PATH = os.getenv("AICROWD_TEST_DATA_PATH", "./data/testing_phase2_release.csv")
AICROWD_PREDICTIONS_OUTPUT_PATH = os.getenv("AICROWD_PREDICTIONS_OUTPUT_PATH", "random_prediction.csv")

# Note : These list of snake-species are the ones that are represented in the training set of this round
VALID_CLASSES = ['prob_approval','prob_pipeline','prob_failure']

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0) # only difference

def get_random_prediction(index_id):
    predictions = [np.random.rand() for _ in VALID_CLASSES]
    predictions = softmax(predictions)
    return predictions

def run():
    ########################################################################
    # Register Prediction Start
    ########################################################################
    aicrowd_helpers.execution_start()


    ########################################################################
    # Load Tests Meta Data file
    #       and iterate over all its rows
    #
    #       Each Row contains the following information : 
    #
    #       - `index` : Unique ID of each record
    #       - `intclinicaltrialid` : description to be added
    #       - `intdesignkeywordid` : description to be added
    #       - `strdesignkeyword` : description to be added
    #       - .... and so on 
    ########################################################################    

    OUTPUT_LINES = []
    HEADER = ['index'] + VALID_CLASSES
    OUTPUT_LINES.append(",".join(HEADER))

    tests_df = pd.read_csv(AICROWD_TEST_DATA_PATH, index_col=0)

    for index_id, row in tqdm.tqdm(tests_df.iterrows()):
        index_id = str(index_id)
        intclinicaltrialid = row['intclinicaltrialid']
        intdesignkeywordid = row['intdesignkeywordid']
        ##
        ## ... and so on 
        ## TODO : Provide example re

        predictions = get_random_prediction(index_id)
        PREDICTION_LINE = [index_id] + [str(x) for x in predictions.tolist()]
        OUTPUT_LINES.append(",".join(PREDICTION_LINE))
        
        ########################################################################
        # Register Prediction
        #
        # Note, this prediction register is not a requirement. It is used to
        # provide you feedback of how far are you in the overall evaluation.
        # In the absence of it, the evaluation will still work, but you
        # will see progress of the evaluation as 0 until it is complete
        #
        # Here you simply announce that you completed processing a set of
        # index_ids
        ########################################################################
        aicrowd_helpers.execution_progress({
            "index_ids" : [index_id] ### NOTE : This is an array of index_ids 
        })


    # Write output
    fp = open(AICROWD_PREDICTIONS_OUTPUT_PATH, "w")
    fp.write("\n".join(OUTPUT_LINES))
    fp.close()
    ########################################################################
    # Register Prediction Complete
    ########################################################################
    aicrowd_helpers.execution_success({
        "predictions_output_path" : AICROWD_PREDICTIONS_OUTPUT_PATH
    })


if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        error = traceback.format_exc()
        print(error)
        aicrowd_helpers.execution_error(error)
