CONDA_PATH='/C/Users/ldalan/AppData/Local/Continuum/anaconda3/etc/profile.d/conda.sh'  # '/c/Users/jungkikang/Miniconda3/etc/profile.d/conda.sh'
CONDA_ENV='pipeline_script'

LOG_PATH=error.log

RES=$(python pass_sh.py 2>&1)
exit_status=$?
if [[ $exit_status -eq 1 ]] ; then
  MESSAGE1="ERROR - $(date +"%Y-%m-%d %H:%M:%S") - fail_sh.py"
  MESSAGE2="    ${RES}"
  echo "${MESSAGE1}"
  echo "${MESSAGE1}" >> "${LOG_PATH}"
  echo "${MESSAGE2}"
  echo "${MESSAGE2}" >> "${LOG_PATH}"
fi

RES=$(python fail_sh.py 2>&1)
exit_status=$?
if [[ $exit_status -eq 1 ]] ; then
  MESSAGE1="ERROR - $(date +"%Y-%m-%d %H:%M:%S") - fail_sh.py"
  MESSAGE2="    ${RES}"
  echo "${MESSAGE1}"
  echo "${MESSAGE1}" >> "${LOG_PATH}"
  echo "${MESSAGE2}"
  echo "${MESSAGE2}" >> "${LOG_PATH}"
fi


