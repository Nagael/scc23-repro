# scc23-repro
Additional fils and information for the Reproducibility Challenge of SCC23

This repository contains
* An `sbc.py` script that produces a file describing an SBC distribution 
  with the file format expected by the `--custom` argument of Chameleon
  
* the webinar slides that were presented on September 13th, 2023.

* there is a six-page limit for the report

## Instructions for the Reproducibility Challenge

The Reproducibility Challenge is based on the SC22 paper [Symmetric Block-Cyclic Distribution: Fewer
Communications Leads to Faster Dense Cholesky
Factorization](https://inria.hal.science/hal-03768910/file/final_version_no_copyright.pdf).

The goal of the challenge is to reproduce results from this paper. The challenge will be evaluated
based on a written report, limited to **6 pages**, that should be handed to the SCC committee at the end
of the competition, on **Wednesday November 15th at 5:00pm**. Here are the requirements for this report:

* Provide a description of your hardware.

* Provide a description of the software stack used to perform the experiments.

* From the paper, reproduce **Figure 8** (total communication volume as a function of matrix size,
  for a fixed number of processes), as well as the top plots of **Figures 10 and 12** (performance
  per process and total running time as a function of matrix size, for a fixed number of processes).

  Since your hardware probably does not have P=15 nodes available, you are expected to use a number
  of MPI processes adapted to the scale of your hardware, while being large enough for the
  communication reduction to be meaningful. You should use the version of the SBC distribution that
  is suited to your number of MPI processes: **basic** or **extended**, with the appropriate value of r.

  You do not have to use the same number of processes or the same size of matrices or the same block
  size. All this depends on your machine. Please use something that makes sense for your machine and
  clearly indicate your choices.

  * Provide a description of the experiment(s): the number of MPI processes and their mapping onto
    your hardware, the parameters for the distributions used (2DBC and SBC), any option provided to
    the software stack if applicable, the number of runs for each configuration, the tile size, the
    range of matrix sizes, and any other relevant information.
  * Provide the plots reproducing Figures 8, 10 and 12, with suitable legends and scales on the axis.
  * Provide an interpretation of each figure, and comments on the result of your experiments.

* At the start of the competition (on **Monday November 13th, 7:00pm**), we will release another
  experiment that you will have to do. This will be related to the SC’22 paper. This might or might
  not be a plot present in the paper. We will give precise directions **at 7:00pm on Monday November
  13th**.

* By **5:00pm on Wednesday November 15th**, your report needs to be uploaded on the file server.


Members of the Reproducible Challenge Commitee will visit the teams during the
competition **on Tuesday Monday November 14th from 10:15AM to noon and from
1:30PM to 2:30PM, SCC Booth,** to enquire about your progress, you are expected
to be available to answer their questions.


Please note some information at: 
[https://github.com/nagael/scc23-repro](https://github.com/nagael/scc23-repro).


