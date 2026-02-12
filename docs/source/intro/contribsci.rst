Getting Started Part II | Contributing Science
================================================================================

Proposed Workflow : Step by Step Guide
######################################

After you have cloned the repository and set up your conda environment, you can start solving different task on the project. For examples, you a have an analysis "re-analysis_comparisson" on the task "global_mean_analysis" and wonder how to proceed:

Start from scratch
------------------

#. `Open a new issue <https://gitlab.dkrz.de/m300901/base_gitpage/-/issues>`_ for your analysis in the GitLab respository if one does not already exist for it.

#. In your local branch, create a directory for your task if one does not already exist for it, e.g., ``tasks/global_mean_analysis``.

   * This directory is the place for your (Python) scripts for each analysis to be done.

#. Create reStructuredText (.rst) files(s) to document your analysis and results, e.g., ``docs/source/tasks/global_mean_analysis/re-analysis_comparisson.rst``.

   * The .rst files(s) you create are the space for your notes e.g., to explain what you've done with its respective plot.

   * To help you, we provide a template file which you may use as a reference, :ref:`docs/source/tasks/general_task/analysis_notes_template.rst<analysis_notes_template>`.

#. Add your reStructuredText file(s) to the "toctree" for your task and analysis, e.g., in ``docs/source/tasks/global_mean_analysis/index.rst``

   * This step is required to link the page(s) for your analysis and track advances for people outside/inside the project.

Working on your Analysis
------------------------

#.  Do analysis in your local git branch:

    * write a notebook or code, e.g., in ``tasks/global_mean_analysis/re-analysis_comparisson.rst``.

    * create the documentation required, e.g., in ``docs/source/tasks/global_mean_analysis/re-analysis_comparisson.rst``.

#. Via the issues interface, discuss doubts or reach of each analysis.

#. Upload your code and notes via merge requests within your analysis's issue.

   * Use this often to avoid problems in the future, the more you let time pass the more problems you might have. :ref:`See here for more guidance<making_merges>`.

#. When you finish your analysis once-and-for-all, upload clean scripts for plotting all your figures with their respective documentation.

   * Once it is approved, the issue is solved and closed.

.. _making_merges:

Making Merge Requests
---------------------
**Every time a new plot is added to documentation or in its respective issue, this should happen first.** Work in progress codes can be part of the merge request. Since each analysis is worked in a branch, the branch will only be ready to merge to the master when it's ready.

#. Create a merge request within the issue on GitLab. This will generate a remote branch using the name of your issue, e.g., ```111-re-analysis-comparisson```.

#. Push the changes you made in your local branch to this remote branch.

   * There are many ways to do this, any doubt encountered don't doubt to ask.

   #. Sync with remote changes: ``git swithc main && git pull``

   #. Make your branch up-to-date: ``git switch [my_local_branch] && git rebase main``. Since your local repository might not be updated, you might need to resolve conflicts.

   #. Rename your branch: ``git branch -m [remote_branch_name]`` to match the name of the remote one you want to push to (e.g. ``[remote_branch_name] = 111-re-analysis-comparisson``).

   #. Push your changes: ``git push --set-upstream origin [remote_branch_name]``, or ``git push`` if you've already ``set-upstream``

#. Whenever you're ready to merge to the main branch, click "ready" on the merge request in GitLab to signal you want this branch to be merged into the main branch of the repository.

Don't Forget
############

- If you make a new .rst file, don't forget to add them to the toctree in your task's ``index.rst`` file.

- If your analysis requires another package / dependency add it to `environment.yml <https://gitlab.dkrz.de/m300901/base_gitpage/-/blob/main/environment.yml?ref_type=heads>`_.

- If there is a new dependency / package required for GitLab CI add it to `requirements.txt <https://gitlab.dkrz.de/m300901/base_gitpage/-/blob/main/requirements.txt?ref_type=heads>`_.

Extra-tasks / ideal
###################
- If you create general function to be used within different analysis, you should write a test for your code, see :ref:`our tests <ourtests>`. This can be added in the GitLab CI/CD.
