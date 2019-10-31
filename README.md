![AIcrowd](https://s3.eu-central-1.amazonaws.com/aicrowd-static/misc/AIcrowd-flat.png)
# novartis-dsai-challenge-starter-kit

This is a starter kit for the [Novartis DSAI Challenge](#) (**TODO** : Update Link) on 
[AIcrowd](https://www.aicrowd.com).

# Problem Statement
**TODO** : Add a problem description

# Dataset
The datasets are available in the [Resources section of the challenge](#) (**TODO** Update Link), and on following the links, you will have 4 files : 

* `training_phase2.csv`
* `testing_phase2_release.csv`

Where : 

* `training_phase2.csv` contains `1600649` records, with the following columns : 
```
index,intclinicaltrialid,intdesignkeywordid,strdesignkeyword,intlocationid,strlocation,intregulatorystatusid,strregulatorystatus,intterminationreasonid,strterminationreason,inttherapeuticareaid,strtherapeuticarea,inttrialstatusid,strtrialstatus,intactualaccrual,inttargetaccrual,intdrugnameid,drugname,strsponsor,intsponsorid,introuteid,route_description,intmediumid,medium_description,dataset,intphaseendyear,outcome,intoutcomeyear,intyearlaunched,intmaxendyear
```

With the following columns : 

    - `index` : Unique ID of each record
    - `intclinicaltrialid` : description to be added
    - `intdesignkeywordid` : description to be added
    - `strdesignkeyword` : description to be added
    - .... and so on 


* `testing_phase2_release.csv` is a CSV file with the following columns : 
```
index,intclinicaltrialid,intdesignkeywordid,strdesignkeyword,intlocationid,strlocation,intregulatorystatusid,strregulatorystatus,intterminationreasonid,strterminationreason,inttherapeuticareaid,strtherapeuticarea,inttrialstatusid,strtrialstatus,intactualaccrual,inttargetaccrual,intdrugnameid,drugname,strsponsor,intsponsorid,introuteid,route_description,intmediumid,medium_description,dataset,intphaseendyear,intoutcomeyear,intyearlaunched,intmaxendyear
```

and the task at hand is to predict the probability distribution for the outcome of a trial over the following possibilities : `['approval', 'pipeline', 'failure']`

# Prediction file format
The predictions should be a valid CSV file with the same number of rows as the number of rows in the test file (`testing_phase2_release`), and the following columns are expected : 
- `index` : Unique ID of each record
- `prob_approval` : Probability (`[0, 1]`) that the outcome of this trial would be `approval`
- `prob_pipeline` : Probability (`[0, 1]`) that the outcome of this trial would be `pipeline`
- `prob_failure` : Probability (`[0, 1]`) that the outcome of this trial would be `failure`

The sum of the probabilities across all the columns should be `< 1.0`.

# Random prediction
A sample script which generates a random prediction for the whole test set is included in the [run.py](run.py). The included inline comments better illustrate the structure expected. Please ensure to use the following environment variables : 

* `AICROWD_TEST_DATA_PATH`
* `AICROWD_PREDICTIONS_OUTPUT_PATH`

to get the path to the test data, and the final path where the prediction outputs are to be saved. 


# Submission

To submit to the challenge you'll need to ensure you've set up an appropriate repository structure, create a private git repository at https://gitlab.aicrowd.com with the contents of your submission, and push a git tag corresponding to the version of your repository you'd like to submit.

### Repository Structure

We have created this sample submission repository which you can use as reference.

#### aicrowd.json
Each repository should have a aicrowd.json file with the following fields:

```
{
    "challenge_id" : "novartis_dsai_challenge_2019",
    "grader_id": "novartis_dsai_challenge_2019",
    "authors" : ["aicrowd-user"],
    "description" : "Novartis DSAI Random Predictor",
    "debug": false
}
```

This file is used to identify your submission as a part of the Novartis DSAI Challenge.  You must use the `challenge_id` and `grader_id` specified above in the submission. The `debug` mode runs submission with subset of complete data and can be used for faster debug cycle. 

#### Submission environment configuration

You can specify your software environment by using all the [available configuration options of repo2docker](https://repo2docker.readthedocs.io/en/latest/config_files.html).

For example, to use Anaconda configuration files you can include an **environment.yml** file:
```
conda env export --no-build > environment.yml
```

It is important to include `--no-build` flag, which is important for allowing your Anaconda config to be replicable cross-platform.

#### Code Entrypoint

The evaluator will use `/home/aicrowd/run.sh` as the entrypoint. Please remember to have a `run.sh` at the root which can instantiate any necessary environment variables and execute your code. This repository includes a sample `run.sh` file.

### Submitting 
To make a submission, you will have to create a private repository on [https://gitlab.aicrowd.com](https://gitlab.aicrowd.com).

You will have to add your SSH Keys to your GitLab account by following the instructions [here](https://docs.gitlab.com/ee/gitlab-basics/create-your-ssh-keys.html).
If you do not have SSH Keys, you will first need to [generate one](https://docs.gitlab.com/ee/ssh/README.html#generating-a-new-ssh-key-pair).

Then you can create a submission by making a *tag push* to your repository, adding the correct git remote and pushing to the remote:

```
git clone https://github.com/AIcrowd/novartis-dsai-challenge-starter-kit novartis-dsai-challenge
cd novartis-dsai-challenge

# Add AICrowd git remote endpoint
git remote add aicrowd git@gitlab.aicrowd.com:<YOUR_AICROWD_USER_NAME>/novartis-dsai-challenge.git
git push aicrowd master

# Create a tag for your submission and push
git tag -am "submission-v0.1" submission-v0.1
git push aicrowd master
git push aicrowd submission-v0.1

# Note : If the contents of your repository (latest commit hash) does not change, 
# then pushing a new tag will not trigger a new evaluation.
```
You now should be able to see the details of your submission at : 
[gitlab.aicrowd.com/<YOUR_AICROWD_USER_NAME>/novartis-dsai-challenge/issues](https://gitlab.aicrowd.com/<YOUR_AICROWD_USER_NAME>/novartis-dsai-challenge/issues)

**Best of Luck**

# Author
* Sharada Mohanty (mohanty@aicrowd.com)
* Shivam Khandelwal (shivam@aicrowd.com)
