log_func()
{
  fail_code=$1
  name=$2
  echo $fail_code
  echo $name
  if [[ $exit_status -eq ${fail_code} ]] ; then
    MESSAGE1="ERROR - $(date +"%Y-%m-%d %H:%M:%S") - ${name}"
    MESSAGE2="    ${name} failed to complete."
    echo "${MESSAGE1}"
    echo "${MESSAGE1}" >> "${LOG_PATH}"
    echo "${MESSAGE2}"
    echo "${MESSAGE2}" >> "${LOG_PATH}"
  fi
}

CONDA_PATH='/C/Users/ldalan/AppData/Local/Continuum/anaconda3/etc/profile.d/conda.sh'  # '/c/Users/jungkikang/Miniconda3/etc/profile.d/conda.sh'
CONDA_ENV='pipeline_script'

LOG_PATH=error.log

RES=$(python pass_sh.py 2>&1)
exit_status=$?
log_func 1 "pass_sh.py"


RES=$(python fail_sh.py 2>&1)
exit_status=$?
log_func 1 "fail_sh.py"


