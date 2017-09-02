# Import necessary packages
import os
from image_model.im_model import evaluate_model_2

# Obtain the environment variables to determine the parameters
slurm_id = int(os.environ['SLURM_ARRAY_JOB_ID'])
slurm_parameter = int(os.environ['SLURM_ARRAY_TASK_ID'])

checkpoint_dir = 'image_model/fine_tuned_model'
log_dir = 'image_model/model_eval'
num_evals = 10
if slurm_parameter == 0:
	mode = 'train'
else:
	mode = 'validation'
evaluate_model_2(checkpoint_dir, log_dir, mode, num_evals)

# Save output and parameters to text file in the localhost node, which is where the computation is performed.
#with open('/data/localhost/not-backed-up/ahu/jobname_' + str(slurm_id) + '_' + str(slurm_parameter) + '.txt', 'w') as text_file:
	#text_file.write('Parameters: {0} Result: {1}\n'.format(parameter, output))